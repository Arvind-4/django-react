import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

let baseUrl = process.env.NODE_ENV === "production" ? "/static/" : "/";

const isDjango = process.env.DJANGO === "true";

if (isDjango) {
  baseUrl = "/static/";
} else {
  baseUrl = "/";
}

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: baseUrl,
  build: {
    minify: true,
  },
});
