import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    outDir: 'build',
    assetsInlineLimit: 0,
    manifest: false,
    rollupOptions: {
      output: {
        entryFileNames: 'js/[name].js',
        chunkFileNames: 'js/[name].js',
        assetFileNames: 'assets/[name].[ext]',
      },
    },
  },
  server: {
    proxy: {
      '/api': {
          target: 'http://localhost:8000',
          changeOrigin: true,
          secure: false,      
          ws: true,
      },
      '/django-static': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,      
        ws: true,
      },
      '/media': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,      
        ws: true,
      }
    },
  },
})
