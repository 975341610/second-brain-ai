import * as Y from 'yjs';
import { IndexeddbPersistence } from 'y-indexeddb';

/**
 * Yjs IndexedDB 持久化管理器
 * 用于将 Tiptap 编辑器的 YDoc 状态同步到浏览器的 IndexedDB。
 */
export class IndexedDBProvider {
  private persistence: IndexeddbPersistence | null = null;
  private doc: Y.Doc;
  private name: string;

  constructor(name: string, doc: Y.Doc) {
    this.name = name;
    this.doc = doc;
    this.init();
  }

  private init() {
    // 为每个笔记 ID 创建一个独立的 IndexedDB 命名空间
    this.persistence = new IndexeddbPersistence(this.name, this.doc);

    this.persistence.on('synced', () => {
      console.log(`[Yjs] IndexedDB synced for doc: ${this.name}`);
    });
  }

  public destroy() {
    if (this.persistence) {
      this.persistence.destroy();
      this.persistence = null;
    }
  }

  public onSynced(callback: () => void) {
    if (this.persistence) {
      this.persistence.on('synced', callback);
    }
  }

  public get isSynced(): boolean {
    return this.persistence?.synced || false;
  }

  /**
   * 清除该文档在本地的所有数据 (谨慎使用)
   */
  public async clearLocalData() {
    if (this.persistence) {
      await this.persistence.clearData();
    }
  }
}
