import '@testing-library/jest-dom';
import { expect, afterEach, vi } from 'vitest';
import { cleanup } from '@testing-library/react';
import * as matchers from '@testing-library/jest-dom/matchers';

// Extends Vitest's expect method with methods from react-testing-library
expect.extend(matchers as any);

// Mock IndexedDB for testing environment
if (typeof window !== 'undefined') {
  (window as any).IDBRequest = class {};
  (window as any).IDBTransaction = class {};
  (window as any).IDBDatabase = class {};
  (window as any).IDBFactory = class {};
  (window as any).IDBIndex = class {};
  (window as any).IDBObjectStore = class {};
  (window as any).IDBCursor = class {};
  (window as any).IDBKeyRange = class {};

  (window as any).indexedDB = {
    open: vi.fn().mockReturnValue({
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
      onupgradeneeded: null,
      onsuccess: null,
      onerror: null,
      then: vi.fn().mockReturnValue(Promise.resolve()),
    }),
  };
}

// Cleanup after each test case (e.g. clearing jsdom)
afterEach(() => {
  cleanup();
});
