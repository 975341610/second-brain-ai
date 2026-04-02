import fs from 'fs/promises';
import path from 'path';
import log from 'electron-log';
import { SSOTWatcher } from './fs-watcher';

export interface NoteMetadata {
  id: number;
  title: string;
  created_at: string;
  updated_at: string;
  tags?: string[];
  parent_id?: number | null;
  [key: string]: any;
}

export interface SaveNoteParams {
  id: number;
  content: string;
  metadata: NoteMetadata;
  silent?: boolean;
}

/**
 * 极简 FS Bridge (Node.js 原生读写)
 */
export class FSBridge {
  private dataDir: string;
  private watcher: SSOTWatcher | null = null;

  constructor(dataDir: string, watcher: SSOTWatcher | null = null) {
    this.dataDir = dataDir;
    this.watcher = watcher;
  }

  public async getNote(id: number, filePath: string): Promise<{ content: string; metadata: NoteMetadata }> {
    const targetPath = path.isAbsolute(filePath) 
      ? filePath 
      : path.join(this.dataDir, filePath);
    
    const fileContent = await fs.readFile(targetPath, 'utf-8');
    return this.parseNote(fileContent, id);
  }

  public async updateNote(params: SaveNoteParams, filePath: string): Promise<void> {
    const targetPath = path.isAbsolute(filePath) 
      ? filePath 
      : path.join(this.dataDir, filePath);

    try {
      const finalMetadata = {
        ...params.metadata,
        updated_at: new Date().toISOString()
      };
      
      const fileString = this.stringifyNote(finalMetadata, params.content);
      
      // 如果是静默保存，记录到监听器以忽略此次变更通知
      if (params.silent && this.watcher) {
        this.watcher.recordInternalWrite(targetPath);
      }

      await fs.writeFile(targetPath, fileString, 'utf-8');
      log.info(`[FSBridge] Note updated: ${targetPath}`);
    } catch (err) {
      log.error(`[FSBridge] Failed to update note:`, err);
      throw err;
    }
  }

  private parseNote(raw: string, id: number): { content: string; metadata: NoteMetadata } {
    const lines = raw.split('\n');
    let metadata: any = { id };
    let contentStart = 0;

    if (lines[0] === '---') {
      const endIdx = lines.indexOf('---', 1);
      if (endIdx !== -1) {
        const fm = lines.slice(1, endIdx).join('\n');
        fm.split('\n').forEach(line => {
          const [key, ...rest] = line.split(':');
          if (key && rest.length) {
            metadata[key.trim()] = rest.join(':').trim();
          }
        });
        contentStart = endIdx + 1;
      }
    }

    return {
      content: lines.slice(contentStart).join('\n'),
      metadata: metadata as NoteMetadata
    };
  }

  private stringifyNote(metadata: NoteMetadata, content: string): string {
    const fmLines = ['---'];
    for (const [key, val] of Object.entries(metadata)) {
      if (key !== 'id' && val !== undefined) {
        fmLines.push(`${key}: ${val}`);
      }
    }
    fmLines.push('---');
    return fmLines.join('\n') + '\n' + content;
  }
}
