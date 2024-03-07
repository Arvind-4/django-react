import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

const baseUrl = process.env.NODE_ENV === "production" ? "/static/" : "";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: baseUrl,
  build: {
    minify: true,
  },
});
