import { defineConfig } from 'vite';

export default defineConfig({
  root: 'src/pages',
  build: {
    outDir: '../../public',
    emptyOutDir: true,
  },
});
