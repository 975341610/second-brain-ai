import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { FSBridge } from '../../src/main/services/FSBridge';
import fs from 'fs/promises';
import path from 'path';
import os from 'os';

// Mock electron-log to avoid missing dependency issues in test environment
vi.mock('electron-log', () => ({
  default: {
    info: vi.fn(),
    error: vi.fn(),
    warn: vi.fn(),
    debug: vi.fn(),
  }
}));

describe('FSBridge', () => {
  let tempDir: string;
  let fsBridge: FSBridge;

  beforeEach(async () => {
    tempDir = await fs.mkdtemp(path.join(os.tmpdir(), 'novablock-test-'));
    fsBridge = new FSBridge(tempDir);
  });

  afterEach(async () => {
    await fs.rm(tempDir, { recursive: true, force: true });
  });

  it('should save a note with frontmatter', async () => {
    const params = {
      id: 1,
      content: '# Hello World',
      metadata: {
        id: 1,
        title: 'Test Note',
        created_at: '2026-04-03T12:00:00Z',
        updated_at: '2026-04-03T12:00:00Z',
        tags: ['test', 'unit'],
        parent_id: null
      }
    };
    const filePath = 'test.md';
    
    await fsBridge.updateNote(params, filePath);
    
    const savedPath = path.join(tempDir, filePath);
    const content = await fs.readFile(savedPath, 'utf-8');
    
    expect(content).toContain('title: Test Note');
    expect(content).toContain('tags: test,unit');
    expect(content).toContain('# Hello World');
  });

  it('should automatically create subdirectories if they do not exist', async () => {
    const params = {
      id: 2,
      content: 'Nested content',
      metadata: {
        id: 2,
        title: 'Nested Note',
        created_at: '2026-04-03T12:00:00Z',
        updated_at: '2026-04-03T12:00:00Z'
      }
    };
    const filePath = 'subfolder/nested.md';
    
    await fsBridge.updateNote(params, filePath);
    
    const savedPath = path.join(tempDir, filePath);
    const content = await fs.readFile(savedPath, 'utf-8');
    expect(content).toContain('Nested content');
  });

  it('should parse a note with frontmatter correctly', async () => {
    const rawContent = `---
title: Parsed Note
tags: tag1,tag2
---
# Content Here`;
    const filePath = 'parsed.md';
    const targetPath = path.join(tempDir, filePath);
    await fs.writeFile(targetPath, rawContent, 'utf-8');

    const note = await fsBridge.getNote(1, filePath);
    
    expect(note.metadata.title).toBe('Parsed Note');
    expect(note.content).toBe('# Content Here');
  });
});
