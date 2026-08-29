import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./tests/e2e",
  use: {
    baseURL: "http://127.0.0.1:4178",
    viewport: { width: 1440, height: 1000 },
  },
  webServer: {
    command: "npx http-server . -p 4178 -c-1",
    url: "http://127.0.0.1:4178",
    reuseExistingServer: true,
    timeout: 120000,
  },
});
