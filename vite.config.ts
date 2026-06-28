import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: 'src/pages',
  build: {
    outDir: '../../public',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'src/pages/index.html'),
        servicios: resolve(__dirname, 'src/pages/servicios.html'),
        contacto: resolve(__dirname, 'src/pages/contacto.html'),
        nosotros: resolve(__dirname, 'src/pages/nosotros.html'),
        flota: resolve(__dirname, 'src/pages/flota.html'),
        rastreo: resolve(__dirname, 'src/pages/rastreo.html'),
        acceso: resolve(__dirname, 'src/pages/acceso.html'),
        landing: resolve(__dirname, 'src/pages/landing.html'),
      },
    },
  },
});
