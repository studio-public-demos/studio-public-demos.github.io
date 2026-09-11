import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const here = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const root = path.resolve(here, "..");
const framesDir = path.join(here, "frames");
const slidesDir = path.join(here, "slides");
const audioPath = path.join(here, "finance-model-studio-demo-kajal.mp3");
const outputPath = path.join(here, "finance-model-studio-demo.mp4");
const useExistingFrames = process.argv.includes("--use-existing-frames");

fs.mkdirSync(framesDir, { recursive: true });
fs.mkdirSync(slidesDir, { recursive: true });

const screenshots = {
  dashboard: path.join(root, "screenshots", "investor-dashboard.png"),
  checks: path.join(root, "screenshots", "model-checks.png"),
  funding: path.join(root, "screenshots", "funding-deployment.png"),
  pnl: path.join(root, "screenshots", "profit-and-loss.png"),
  architecture: path.join(root, "diagrams", "conceptual-architecture.svg"),
};

const durations = [14, 17, 17, 18, 18, 16, 18, 17, 18];

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function fileUrl(filePath) {
  return `file:///${filePath.replaceAll("\\", "/").replace(/^([A-Za-z]:)/, "$1")}`;
}

function bullets(items, x, y, color = "#334155", size = 34, line = 54) {
  return items.map((item, idx) => {
    const yy = y + idx * line;
    return `<text x="${x}" y="${yy}" font-family="Arial, Helvetica, sans-serif" font-size="${size}" fill="${color}"><tspan fill="#155e75">•</tspan> ${esc(item)}</text>`;
  }).join("\n");
}

function pill(text, x, y, width, tone = "blue") {
  const fills = { blue: "#eff6ff", teal: "#ecfeff", orange: "#fff7ed", purple: "#f5f3ff" };
  const strokes = { blue: "#bfdbfe", teal: "#a5f3fc", orange: "#fed7aa", purple: "#ddd6fe" };
  const colors = { blue: "#1d4ed8", teal: "#155e75", orange: "#9a3412", purple: "#6d28d9" };
  return `<rect x="${x}" y="${y}" width="${width}" height="52" rx="8" fill="${fills[tone]}" stroke="${strokes[tone]}"/>
  <text x="${x + 22}" y="${y + 34}" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="${colors[tone]}">${esc(text)}</text>`;
}

function imagePanel(src, x, y, width, height, caption) {
  return `<rect x="${x}" y="${y}" width="${width}" height="${height}" rx="14" fill="#ffffff" stroke="#dbe3ef"/>
  <image href="${fileUrl(src)}" x="${x + 20}" y="${y + 20}" width="${width - 40}" height="${height - 96}" preserveAspectRatio="xMidYMid meet"/>
  <text x="${x + 24}" y="${y + height - 34}" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#475569">${esc(caption)}</text>`;
}

function layout({ eyebrow, title, subtitle, left, right, footer = "NebulaCloud Studio | Generated outputs only | IP-safe public showcase" }) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">
  <defs>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="58%" stop-color="#f3f8ff"/>
      <stop offset="100%" stop-color="#eef6ff"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="24" stdDeviation="26" flood-color="#0f172a" flood-opacity=".14"/>
    </filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg)"/>
  <rect x="0" y="0" width="1920" height="98" fill="#ffffff" opacity=".92"/>
  <line x1="0" y1="98" x2="1920" y2="98" stroke="#dbe3ef"/>
  <text x="150" y="61" font-family="Georgia, serif" font-size="24" letter-spacing="4" fill="#0f172a">STUDIO DEMOS</text>
  <text x="1470" y="62" font-family="Arial, Helvetica, sans-serif" font-size="26" font-weight="700" fill="#1d4ed8">nebulacloud.studio</text>
  <text x="150" y="184" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="800" letter-spacing="3" fill="#155e75">${esc(eyebrow)}</text>
  <text x="150" y="282" font-family="Georgia, serif" font-size="74" font-weight="700" fill="#071b3a">${esc(title)}</text>
  <foreignObject x="154" y="316" width="820" height="170">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Arial, Helvetica, sans-serif;font-size:34px;line-height:1.45;color:#334155">${esc(subtitle)}</div>
  </foreignObject>
  ${left}
  ${right}
  <text x="150" y="1032" font-family="Arial, Helvetica, sans-serif" font-size="20" fill="#64748b">${esc(footer)}</text>
</svg>`;
}

const slides = [
  layout({
    eyebrow: "NEW STUDIO CAPABILITY",
    title: "Finance Model Studio",
    subtitle: "A narrated product demonstration for CFOs, founders, finance teams, analysts, and investors.",
    left: `${pill("Solution Architect Walkthrough", 150, 520, 360, "teal")}
      ${bullets(["From business brief to working model", "Built for finance decision-makers", "Excel output with dashboard and checks"], 150, 640)}`,
    right: imagePanel(screenshots.dashboard, 1030, 190, 700, 720, "Investor dashboard generated from the brief"),
  }),
  layout({
    eyebrow: "WHAT WE STARTED WITH",
    title: "Narrative Becomes Numbers",
    subtitle: "Studio ingests business context and turns planning language into model structure.",
    left: bullets(["Seed-stage funding brief", "Acquisition and conversion assumptions", "Pricing, revenue, costs, hiring, runway", "Compliance and funding deployment milestones"], 150, 540),
    right: `${pill("Input", 1050, 260, 130, "orange")}
      ${pill("Assumptions", 1210, 260, 210, "blue")}
      ${pill("Schedules", 1450, 260, 180, "purple")}
      ${pill("Workbook", 1325, 380, 190, "teal")}
      <path d="M1180 286 C1220 310, 1230 320, 1278 286" stroke="#155e75" stroke-width="5" fill="none"/>
      <path d="M1420 286 C1450 312, 1455 326, 1488 286" stroke="#155e75" stroke-width="5" fill="none"/>
      <path d="M1510 315 C1485 370, 1450 395, 1408 405" stroke="#155e75" stroke-width="5" fill="none"/>
      <rect x="1040" y="500" width="620" height="270" rx="14" fill="#ffffff" stroke="#dbe3ef" filter="url(#shadow)"/>
      ${bullets(["Editable assumptions", "Linked formulas", "Executive dashboard", "Automated validation"], 1090, 585, "#334155", 30, 48)}`,
  }),
  layout({
    eyebrow: "GENERATED OUTPUT",
    title: "One Integrated Workbook",
    subtitle: "The output is an editable Excel financial model with connected schedules and decision-ready views.",
    left: `${pill("24 monthly periods", 150, 530, 260, "blue")}
      ${pill("11 workbook sheets", 430, 530, 250, "teal")}
      ${pill("Validation: PASS", 700, 530, 230, "purple")}
      ${bullets(["Assumptions", "Acquisition and revenue funnels", "P&L, balance sheet, cash runway", "Funding deployment and dashboard"], 150, 660)}`,
    right: imagePanel(screenshots.pnl, 1040, 190, 680, 720, "Linked monthly P&L schedule"),
  }),
  layout({
    eyebrow: "WHY IT MATTERS",
    title: "Built For Finance Leaders",
    subtitle: "Different stakeholders get the same thing they need most: clarity, speed, and traceability.",
    left: bullets(["CFOs: faster planning cycles", "Founders: stronger investor conversations", "Finance teams: repeatable model structure", "Analysts: transparent assumptions and checks", "Investors: clearer diligence signals"], 150, 520),
    right: `<rect x="1040" y="260" width="650" height="490" rx="16" fill="#ffffff" stroke="#dbe3ef" filter="url(#shadow)"/>
      ${pill("CFO", 1090, 330, 130, "blue")}
      ${pill("Founder", 1250, 330, 160, "teal")}
      ${pill("FP&A", 1440, 330, 130, "purple")}
      ${pill("Analyst", 1090, 430, 170, "orange")}
      ${pill("Investor", 1290, 430, 180, "blue")}
      ${pill("VC Team", 1500, 430, 170, "teal")}
      <text x="1092" y="610" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#0f172a">One shared model.</text>
      <text x="1092" y="662" font-family="Arial, Helvetica, sans-serif" font-size="30" fill="#475569">Many better decisions.</text>`,
  }),
  layout({
    eyebrow: "DASHBOARD VIEW",
    title: "Investor-Ready Summary",
    subtitle: "Studio creates management-ready charts and KPIs so stakeholders can inspect the business quickly.",
    left: bullets(["Users, revenue, gross margin, EBITDA", "Acquisition channel contribution", "Funding allocation and CAC", "Runway and cash visibility"], 150, 540),
    right: imagePanel(screenshots.dashboard, 970, 170, 760, 760, "Board and investor dashboard"),
  }),
  layout({
    eyebrow: "QUALITY CONTROLS",
    title: "Checks Built In",
    subtitle: "A good model should be auditable. Studio adds validation views that help catch structural and business-rule issues.",
    left: bullets(["Reconciliation checks", "Forecast sanity checks", "PASS, WARNING, and FAIL indicators", "Clearer review before sharing"], 150, 540),
    right: imagePanel(screenshots.checks, 1000, 180, 720, 740, "Automated model checks"),
  }),
  layout({
    eyebrow: "USE CASES",
    title: "More Than Fundraising",
    subtitle: "The same capability supports many finance and investment workflows.",
    left: bullets(["Startup fundraising models", "Board operating plans", "SaaS revenue and ARR planning", "Investor diligence packs", "Capital allocation and runway analysis"], 150, 520),
    right: imagePanel(screenshots.funding, 1010, 190, 700, 720, "Funding deployment by purpose and phase"),
  }),
  layout({
    eyebrow: "HOW TEAMS CREATE WITH STUDIO",
    title: "Brief. Review. Generate.",
    subtitle: "Studio handles the heavy structure while teams keep control of business judgement.",
    left: bullets(["Bring the business brief", "Clarify assumptions and scenarios", "Generate linked schedules and dashboards", "Review checks, iterate, and publish"], 150, 540),
    right: `${pill("Business Brief", 1050, 300, 230, "orange")}
      ${pill("Studio Workflow", 1330, 300, 260, "blue")}
      ${pill("Excel Model", 1190, 455, 220, "teal")}
      ${pill("Decision Pack", 1460, 455, 240, "purple")}
      <path d="M1280 326 L1330 326" stroke="#155e75" stroke-width="5"/>
      <path d="M1440 352 C1420 410, 1370 430, 1310 455" stroke="#155e75" stroke-width="5" fill="none"/>
      <path d="M1410 481 L1460 481" stroke="#155e75" stroke-width="5"/>
      <rect x="1040" y="650" width="610" height="130" rx="14" fill="#ffffff" stroke="#dbe3ef"/>
      <text x="1085" y="724" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#0f172a">Beautiful, useful projects with ease.</text>`,
  }),
  layout({
    eyebrow: "CALL TO ACTION",
    title: "Bring Your Brief",
    subtitle: "NebulaCloud Studio turns it into a working financial model for planning, fundraising, diligence, and growth decisions.",
    left: `${pill("CFOs", 150, 540, 120, "blue")}
      ${pill("Founders", 300, 540, 170, "teal")}
      ${pill("Finance Teams", 500, 540, 240, "purple")}
      ${pill("Analysts", 770, 540, 170, "orange")}
      ${pill("Investors", 150, 625, 180, "blue")}
      <text x="150" y="780" font-family="Arial, Helvetica, sans-serif" font-size="44" font-weight="800" fill="#155e75">nebulacloud.studio</text>`,
    right: imagePanel(screenshots.dashboard, 1000, 190, 720, 720, "Download the sample workbook from the showcase"),
    footer: "Finance Model Studio Capability | Public demo showcase | generated outputs only",
  }),
];

slides.forEach((svg, index) => {
  const slidePath = path.join(slidesDir, `slide-${String(index + 1).padStart(2, "0")}.svg`);
  const framePath = path.join(framesDir, `slide-${String(index + 1).padStart(2, "0")}.png`);
  fs.writeFileSync(slidePath, svg, "utf8");
  if (!useExistingFrames) {
    execFileSync("ffmpeg", ["-y", "-hide_banner", "-loglevel", "error", "-i", slidePath, "-frames:v", "1", framePath], { stdio: "inherit" });
  } else if (!fs.existsSync(framePath)) {
    throw new Error(`Missing rendered frame: ${framePath}`);
  }
});

if (!fs.existsSync(audioPath)) {
  throw new Error(`Missing audio file: ${audioPath}`);
}

const inputs = [];
const filters = [];
for (let index = 0; index < slides.length; index += 1) {
  inputs.push("-loop", "1", "-t", String(durations[index]), "-i", path.join(framesDir, `slide-${String(index + 1).padStart(2, "0")}.png`));
  filters.push(`[${index}:v]scale=1920:1080,format=yuv420p,setpts=PTS-STARTPTS[v${index}]`);
}
inputs.push("-i", audioPath);

const concatInputs = slides.map((_, index) => `[v${index}]`).join("");
const filterGraph = `${filters.join(";")};${concatInputs}concat=n=${slides.length}:v=1:a=0[v]`;

execFileSync("ffmpeg", [
  "-y",
  "-hide_banner",
  ...inputs,
  "-filter_complex", filterGraph,
  "-map", "[v]",
  "-map", `${slides.length}:a`,
  "-c:v", "libx264",
  "-preset", "medium",
  "-crf", "18",
  "-c:a", "aac",
  "-b:a", "192k",
  "-shortest",
  "-movflags", "+faststart",
  outputPath,
], { stdio: "inherit" });

console.log(outputPath);
