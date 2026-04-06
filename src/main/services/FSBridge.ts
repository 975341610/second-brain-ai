import fs from 'fs/promises';
import path from 'path';
import log from 'electron-log';
import { NoteMetadata, SaveNoteParams, NoteData } from '../../common/types';

export class FSBridge {
  private dataDir: string;
  private watcher: any | null = null; // Typing later to avoid circular dependency

  constructor(dataDir: string, watcher: any | null = null) {
    this.dataDir = dataDir;
    this.watcher = watcher;
  }

  public async getNote(id: number, filePath: string): Promise<NoteData> {
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

    // Ensure directory exists
    const dir = path.dirname(targetPath);
    await fs.mkdir(dir, { recursive: true });

    try {
      const finalMetadata = {
        ...params.metadata,
        updated_at: new Date().toISOString()
      };
      
      const fileString = this.stringifyNote(finalMetadata, params.content);
      
      // If it's a silent save, record to watcher to ignore this change
      if (params.silent && this.watcher && typeof this.watcher.recordInternalWrite === 'function') {
        this.watcher.recordInternalWrite(targetPath);
      }

      await fs.writeFile(targetPath, fileString, 'utf-8');
      log.info(`[FSBridge] Note updated: ${targetPath}`);
    } catch (err) {
      log.error(`[FSBridge] Failed to update note:`, err);
      throw err;
    }
  }

  private parseNote(raw: string, id: number): NoteData {
    const lines = raw.split('\n');
    let metadata: any = { id };
    let contentStart = 0;

    if (lines[0] === '---') {
      const endIdx = lines.indexOf('---', 1);
      if (endIdx !== -1) {
        const fm = lines.slice(1, endIdx).join('\n');
        fm.split('\n').forEach(line => {
          const splitIdx = line.indexOf(':');
          if (splitIdx !== -1) {
            const key = line.slice(0, splitIdx).trim();
            const val = line.slice(splitIdx + 1).trim();
            metadata[key] = val;
          }
        });
        contentStart = endIdx + 1;
      }
    }

    return {
      content: lines.slice(contentStart).join('\n').trim(),
      metadata: metadata as NoteMetadata
    };
  }

  private stringifyNote(metadata: NoteMetadata, content: string): string {
    const fmLines = ['---'];
    for (const [key, val] of Object.entries(metadata)) {
      if (key !== 'id' && val !== undefined && val !== null) {
        if (Array.isArray(val)) {
          fmLines.push(`${key}: ${val.join(',')}`);
        } else {
          fmLines.push(`${key}: ${val}`);
        }
      }
    }
    fmLines.push('---');
    return fmLines.join('\n') + '\n' + content;
  }
}
