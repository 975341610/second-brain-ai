import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'
import { defineConfig as defineVitestConfig, mergeConfig } from 'vitest/config'

// https://vite.dev/config/
const viteConfig = defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': resolve(__dirname, './src'),
      'react': resolve(__dirname, 'node_modules/react'),
      'react-dom': resolve(__dirname, 'node_modules/react-dom')
    }
  },
  server: {
    host: '0.0.0.0',
    port: 5173,
    allowedHosts: true,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8765',
        changeOrigin: true,
      }
    },
    // 根据环境变量动态配置 HMR，避免写死导致本地和云端环境冲突
    hmr: process.env.HMR_CLIENT_PORT 
      ? {
          clientPort: Number(process.env.HMR_CLIENT_PORT),
          protocol: process.env.HMR_PROTOCOL || 'wss',
        }
      : true,
  },
})

export default mergeConfig(
  viteConfig,
  defineVitestConfig({
    test: {
      environment: 'jsdom',
      globals: true,
      setupFiles: ['./src/test/setup.ts'],
    },
  })
)
