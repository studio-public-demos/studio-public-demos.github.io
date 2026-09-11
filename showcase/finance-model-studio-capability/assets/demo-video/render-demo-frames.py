from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "frames"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
INK = "#071b3a"
TEXT = "#334155"
MUTED = "#64748b"
LINE = "#dbe3ef"
BLUE = "#1d4ed8"
TEAL = "#155e75"

SCREENSHOTS = {
    "dashboard": ROOT / "screenshots" / "investor-dashboard.png",
    "checks": ROOT / "screenshots" / "model-checks.png",
    "funding": ROOT / "screenshots" / "funding-deployment.png",
    "pnl": ROOT / "screenshots" / "profit-and-loss.png",
}


def font(name, size, bold=False):
    candidates = []
    if name == "serif":
        candidates = [
            "C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf",
            "C:/Windows/Fonts/timesbd.ttf" if bold else "C:/Windows/Fonts/times.ttf",
        ]
    else:
        candidates = [
            "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default(size=size)


F = {
    "logo": font("serif", 24),
    "eyebrow": font("sans", 24, True),
    "title": font("serif", 76, True),
    "body": font("sans", 34),
    "body_sm": font("sans", 30),
    "pill": font("sans", 22, True),
    "caption": font("sans", 24),
    "footer": font("sans", 20),
}


def wrap(draw, text, fnt, width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, text, xy, fnt, fill, width, line_height):
    x, y = xy
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_height
    return y


def background():
    img = Image.new("RGB", (W, H), "#f8fafc")
    pix = img.load()
    for y in range(H):
        for x in range(W):
            t = (x / W * 0.45) + (y / H * 0.55)
            r = int(248 * (1 - t) + 238 * t)
            g = int(250 * (1 - t) + 246 * t)
            b = int(252 * (1 - t) + 255 * t)
            pix[x, y] = (r, g, b)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W, 98), fill="#ffffff")
    draw.line((0, 98, W, 98), fill=LINE, width=1)
    draw.text((150, 38), "STUDIO DEMOS", font=F["logo"], fill="#0f172a")
    draw.text((1470, 38), "nebulacloud.studio", font=font("sans", 28, True), fill=BLUE)
    draw.text((150, 1018), "NebulaCloud Studio | Generated outputs only | IP-safe public showcase", font=F["footer"], fill=MUTED)
    return img, draw


def pill(draw, text, x, y, w, tone="blue"):
    palette = {
        "blue": ("#eff6ff", "#bfdbfe", BLUE),
        "teal": ("#ecfeff", "#a5f3fc", TEAL),
        "orange": ("#fff7ed", "#fed7aa", "#9a3412"),
        "purple": ("#f5f3ff", "#ddd6fe", "#6d28d9"),
    }
    fill, stroke, color = palette[tone]
    draw.rounded_rectangle((x, y, x + w, y + 52), radius=8, fill=fill, outline=stroke, width=2)
    draw.text((x + 22, y + 14), text, font=F["pill"], fill=color)


def bullets(draw, items, x, y, size="body"):
    fnt = F[size]
    for item in items:
        draw.text((x, y), "-", font=fnt, fill=TEAL)
        draw_wrapped(draw, item, (x + 28, y), fnt, TEXT, 760, 48 if size == "body_sm" else 54)
        y += 62 if size == "body_sm" else 70


def image_panel(base, src, x, y, w, h, caption):
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle((x, y, x + w, y + h), radius=16, fill="#ffffff", outline=LINE, width=2)
    shot = Image.open(src).convert("RGB")
    max_w, max_h = w - 48, h - 110
    shot.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    sx = x + (w - shot.width) // 2
    sy = y + 26
    base.paste(shot, (sx, sy))
    draw.text((x + 26, y + h - 58), caption, font=F["caption"], fill="#475569")


def slide(index, eyebrow, title, subtitle, left_fn, right_fn):
    img, draw = background()
    draw.text((150, 168), eyebrow, font=F["eyebrow"], fill=TEAL)
    draw.text((150, 222), title, font=F["title"], fill=INK)
    draw_wrapped(draw, subtitle, (154, 330), F["body"], TEXT, 830, 48)
    left_fn(img, draw)
    right_fn(img, draw)
    img.save(OUT / f"slide-{index:02d}.png", quality=95)


slide(
    1,
    "NEW STUDIO CAPABILITY",
    "Finance Model Studio",
    "A narrated product demonstration for CFOs, founders, finance teams, analysts, and investors.",
    lambda img, draw: (pill(draw, "Solution Architect Walkthrough", 150, 520, 360, "teal"), bullets(draw, ["From business brief to working model", "Built for finance decision-makers", "Excel output with dashboard and checks"], 150, 640)),
    lambda img, draw: image_panel(img, SCREENSHOTS["dashboard"], 1030, 190, 700, 720, "Investor dashboard generated from the brief"),
)

slide(
    2,
    "WHAT WE STARTED WITH",
    "Narrative Becomes Numbers",
    "Studio ingests business context and turns planning language into model structure.",
    lambda img, draw: bullets(draw, ["Seed-stage funding brief", "Acquisition and conversion assumptions", "Pricing, revenue, costs, hiring, runway", "Compliance and funding deployment milestones"], 150, 540),
    lambda img, draw: (pill(draw, "Input", 1050, 300, 130, "orange"), pill(draw, "Assumptions", 1210, 300, 210, "blue"), pill(draw, "Schedules", 1450, 300, 180, "purple"), pill(draw, "Workbook", 1325, 430, 190, "teal"), draw.rounded_rectangle((1040, 580, 1660, 800), radius=16, fill="#ffffff", outline=LINE, width=2), bullets(draw, ["Editable assumptions", "Linked formulas", "Executive dashboard", "Automated validation"], 1090, 630, "body_sm")),
)

slide(
    3,
    "GENERATED OUTPUT",
    "One Integrated Workbook",
    "The output is an editable Excel financial model with connected schedules and decision-ready views.",
    lambda img, draw: (pill(draw, "24 monthly periods", 150, 530, 260, "blue"), pill(draw, "11 workbook sheets", 430, 530, 250, "teal"), pill(draw, "Validation: PASS", 700, 530, 230, "purple"), bullets(draw, ["Assumptions", "Acquisition and revenue funnels", "P&L, balance sheet, cash runway", "Funding deployment and dashboard"], 150, 660)),
    lambda img, draw: image_panel(img, SCREENSHOTS["pnl"], 1040, 190, 680, 720, "Linked monthly P&L schedule"),
)

slide(
    4,
    "WHY IT MATTERS",
    "Built For Finance Leaders",
    "Different stakeholders get the same thing they need most: clarity, speed, and traceability.",
    lambda img, draw: bullets(draw, ["CFOs: faster planning cycles", "Founders: stronger investor conversations", "Finance teams: repeatable model structure", "Analysts: transparent assumptions and checks", "Investors: clearer diligence signals"], 150, 520),
    lambda img, draw: (draw.rounded_rectangle((1040, 260, 1690, 750), radius=16, fill="#ffffff", outline=LINE, width=2), pill(draw, "CFO", 1090, 330, 130, "blue"), pill(draw, "Founder", 1250, 330, 160, "teal"), pill(draw, "FP&A", 1440, 330, 130, "purple"), pill(draw, "Analyst", 1090, 430, 170, "orange"), pill(draw, "Investor", 1290, 430, 180, "blue"), pill(draw, "VC Team", 1500, 430, 170, "teal"), draw.text((1092, 610), "One shared model.", font=font("sans", 36, True), fill="#0f172a"), draw.text((1092, 662), "Many better decisions.", font=F["body_sm"], fill="#475569")),
)

slide(
    5,
    "DASHBOARD VIEW",
    "Investor-Ready Summary",
    "Studio creates management-ready charts and KPIs so stakeholders can inspect the business quickly.",
    lambda img, draw: bullets(draw, ["Users, revenue, gross margin, EBITDA", "Acquisition channel contribution", "Funding allocation and CAC", "Runway and cash visibility"], 150, 540),
    lambda img, draw: image_panel(img, SCREENSHOTS["dashboard"], 970, 170, 760, 760, "Board and investor dashboard"),
)

slide(
    6,
    "QUALITY CONTROLS",
    "Checks Built In",
    "A good model should be auditable. Studio adds validation views that help catch structural and business-rule issues.",
    lambda img, draw: bullets(draw, ["Reconciliation checks", "Forecast sanity checks", "PASS, WARNING, and FAIL indicators", "Clearer review before sharing"], 150, 540),
    lambda img, draw: image_panel(img, SCREENSHOTS["checks"], 1000, 180, 720, 740, "Automated model checks"),
)

slide(
    7,
    "USE CASES",
    "More Than Fundraising",
    "The same capability supports many finance and investment workflows.",
    lambda img, draw: bullets(draw, ["Startup fundraising models", "Board operating plans", "SaaS revenue and ARR planning", "Investor diligence packs", "Capital allocation and runway analysis"], 150, 520),
    lambda img, draw: image_panel(img, SCREENSHOTS["funding"], 1010, 190, 700, 720, "Funding deployment by purpose and phase"),
)

slide(
    8,
    "HOW TEAMS CREATE WITH STUDIO",
    "Brief. Review. Generate.",
    "Studio handles the heavy structure while teams keep control of business judgement.",
    lambda img, draw: bullets(draw, ["Bring the business brief", "Clarify assumptions and scenarios", "Generate linked schedules and dashboards", "Review checks, iterate, and publish"], 150, 540),
    lambda img, draw: (pill(draw, "Business Brief", 1050, 300, 230, "orange"), pill(draw, "Studio Workflow", 1330, 300, 260, "blue"), pill(draw, "Excel Model", 1190, 455, 220, "teal"), pill(draw, "Decision Pack", 1460, 455, 240, "purple"), draw.rounded_rectangle((1040, 650, 1650, 780), radius=16, fill="#ffffff", outline=LINE, width=2), draw.text((1085, 694), "Beautiful, useful projects", font=font("sans", 34, True), fill="#0f172a"), draw.text((1085, 738), "with ease.", font=font("sans", 34, True), fill=TEAL)),
)

slide(
    9,
    "CALL TO ACTION",
    "Bring Your Brief",
    "NebulaCloud Studio turns it into a working financial model for planning, fundraising, diligence, and growth decisions.",
    lambda img, draw: (pill(draw, "CFOs", 150, 540, 120, "blue"), pill(draw, "Founders", 300, 540, 170, "teal"), pill(draw, "Finance Teams", 500, 540, 240, "purple"), pill(draw, "Analysts", 770, 540, 170, "orange"), pill(draw, "Investors", 150, 625, 180, "blue"), draw.text((150, 780), "nebulacloud.studio", font=font("sans", 44, True), fill=TEAL)),
    lambda img, draw: image_panel(img, SCREENSHOTS["dashboard"], 1000, 190, 720, 720, "Download the sample workbook from the showcase"),
)

print(f"Rendered frames to {OUT}")
