import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://0.0.0.0:5000',
      },
    },
    host: '0.0.0.0',
    port: 80
  },
});
