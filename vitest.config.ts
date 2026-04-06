import { defineConfig } from 'vitest/config';
import path from 'path';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['tests/unit/**/*.{test,spec}.ts', 'src/**/*.{test,spec}.ts'],
    alias: {
      '@common': path.resolve(__dirname, './src/common'),
      '@main': path.resolve(__dirname, './src/main'),
    },
  },
});
