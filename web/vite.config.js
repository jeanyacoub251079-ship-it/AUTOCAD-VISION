import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// L'app complète est servie par FastAPI sur :8000 ; ce proxy ne sert qu'au
// développement (`npm run dev`).
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    proxy: { '/api': { target: 'http://127.0.0.1:8000', changeOrigin: true } }
  },
  build: { outDir: 'dist' }
})
