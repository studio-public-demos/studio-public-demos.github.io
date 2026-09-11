from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "frames"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
MARGIN = 132
LEFT_X = MARGIN
LEFT_W = 690
RIGHT_X = 890
RIGHT_W = 900
TOP_Y = 150

INK = "#071b3a"
TEXT = "#334155"
MUTED = "#64748b"
LINE = "#dbe3ef"
BLUE = "#1d4ed8"
TEAL = "#155e75"
GREEN = "#15803d"
ORANGE = "#9a3412"
PURPLE = "#6d28d9"

SCREENSHOTS = {
    "dashboard": ROOT / "screenshots" / "investor-dashboard.png",
    "checks": ROOT / "screenshots" / "model-checks.png",
    "funding": ROOT / "screenshots" / "funding-deployment.png",
    "pnl": ROOT / "screenshots" / "profit-and-loss.png",
}


def font(name, size, bold=False):
    if name == "serif":
        candidates = [
            "C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf",
            "C:/Windows/Fonts/timesbd.ttf" if bold else "C:/Windows/Fonts/times.ttf",
        ]
    else:
        candidates = [
            "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
            "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default(size=size)


F = {
    "logo": font("serif", 22),
    "nav": font("sans", 22, True),
    "eyebrow": font("sans", 21, True),
    "title": font("serif", 64, True),
    "subtitle": font("sans", 32),
    "body": font("sans", 28),
    "body_bold": font("sans", 28, True),
    "small": font("sans", 20),
    "small_bold": font("sans", 20, True),
    "pill": font("sans", 21, True),
    "metric": font("sans", 42, True),
    "caption": font("sans", 22),
    "footer": font("sans", 18),
}


def rgb(value):
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def rounded_shadow(base, box, radius=10, fill="#ffffff", outline=LINE, shadow=True):
    x1, y1, x2, y2 = box
    if shadow:
        layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        d.rounded_rectangle((x1, y1, x2, y2), radius=radius, fill=(15, 23, 42, 34))
        layer = layer.filter(ImageFilter.GaussianBlur(18))
        base.alpha_composite(layer, (0, 10))
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=1)


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


def draw_wrapped(draw, text, x, y, fnt, fill, width, line_height):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_height
    return y


def base_slide(step, label):
    img = Image.new("RGBA", (W, H), "#f8fafc")
    pixels = img.load()
    start = rgb("#fbfdff")
    end = rgb("#edf5ff")
    for y in range(H):
        for x in range(W):
            t = min(1, (x / W) * 0.58 + (y / H) * 0.42)
            pixels[x, y] = tuple(int(start[i] * (1 - t) + end[i] * t) for i in range(3)) + (255,)

    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W, 92), fill="#ffffff")
    draw.line((0, 92, W, 92), fill=LINE, width=1)
    draw.text((MARGIN, 34), "STUDIO DEMOS", font=F["logo"], fill="#0f172a")
    draw.text((1428, 32), "nebulacloud.studio", font=F["nav"], fill=BLUE)

    rail_x, rail_y, rail_w = MARGIN, 995, W - (MARGIN * 2)
    draw.rounded_rectangle((rail_x, rail_y, rail_x + rail_w, rail_y + 6), radius=3, fill="#dbeafe")
    draw.rounded_rectangle((rail_x, rail_y, rail_x + int(rail_w * step / 9), rail_y + 6), radius=3, fill=TEAL)
    draw.text((MARGIN, 1020), f"{step:02d} / 09  {label}", font=F["footer"], fill=MUTED)
    draw.text((1400, 1020), "Generated outputs only | IP-safe public showcase", font=F["footer"], fill=MUTED)
    return img, draw


def header(draw, eyebrow, title, subtitle):
    draw.text((LEFT_X, TOP_Y), eyebrow.upper(), font=F["eyebrow"], fill=TEAL)
    title_y = TOP_Y + 56
    for line in wrap(draw, title, F["title"], LEFT_W):
        draw.text((LEFT_X, title_y), line, font=F["title"], fill=INK)
        title_y += 72
    return draw_wrapped(draw, subtitle, LEFT_X + 2, title_y + 10, F["subtitle"], TEXT, LEFT_W, 44)


def pill(draw, text, x, y, w, tone="blue"):
    palette = {
        "blue": ("#eff6ff", "#bfdbfe", BLUE),
        "teal": ("#ecfeff", "#a5f3fc", TEAL),
        "orange": ("#fff7ed", "#fed7aa", ORANGE),
        "purple": ("#f5f3ff", "#ddd6fe", PURPLE),
        "green": ("#f0fdf4", "#bbf7d0", GREEN),
    }
    fill, stroke, color = palette[tone]
    draw.rounded_rectangle((x, y, x + w, y + 52), radius=8, fill=fill, outline=stroke, width=1)
    draw.text((x + 20, y + 14), text, font=F["pill"], fill=color)


def bullet_list(draw, items, x, y, width=650, gap=58):
    for item in items:
        draw.rounded_rectangle((x, y + 11, x + 8, y + 19), radius=2, fill=TEAL)
        draw_wrapped(draw, item, x + 28, y, F["body"], TEXT, width, 38)
        y += gap


def metric_card(draw, label, value, x, y, w=205, tone=TEAL):
    draw.rounded_rectangle((x, y, x + w, y + 118), radius=10, fill="#ffffff", outline=LINE, width=1)
    draw.text((x + 22, y + 22), value, font=F["metric"], fill=tone)
    draw_wrapped(draw, label, x + 22, y + 73, F["small"], MUTED, w - 44, 25)


def product_panel(base, src, title, caption, x=RIGHT_X, y=166, w=RIGHT_W, h=760):
    rounded_shadow(base, (x, y, x + w, y + h), radius=12, fill="#ffffff", outline=LINE)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle((x, y, x + w, y + 52), radius=12, fill="#f8fafc", outline=LINE, width=1)
    draw.ellipse((x + 22, y + 18, x + 34, y + 30), fill="#ef4444")
    draw.ellipse((x + 44, y + 18, x + 56, y + 30), fill="#f59e0b")
    draw.ellipse((x + 66, y + 18, x + 78, y + 30), fill="#22c55e")
    draw.text((x + 104, y + 15), title, font=F["small_bold"], fill="#334155")

    shot = Image.open(src).convert("RGB")
    max_w, max_h = w - 76, h - 154
    shot.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    sx = x + (w - shot.width) // 2
    sy = y + 78
    base.paste(shot, (sx, sy))
    draw.line((x, y + h - 72, x + w, y + h - 72), fill=LINE, width=1)
    draw.text((x + 32, y + h - 48), caption, font=F["caption"], fill="#475569")


def workflow_panel(base, items):
    draw = ImageDraw.Draw(base)
    rounded_shadow(base, (RIGHT_X, 210, RIGHT_X + RIGHT_W, 784), radius=12, fill="#ffffff", outline=LINE)
    cx = RIGHT_X + 84
    for idx, (title, text, tone) in enumerate(items):
        y = 270 + idx * 118
        color = {"blue": BLUE, "teal": TEAL, "orange": ORANGE, "purple": PURPLE, "green": GREEN}[tone]
        draw.rounded_rectangle((cx, y, cx + 52, y + 52), radius=8, fill=color)
        draw.text((cx + 18, y + 13), str(idx + 1), font=F["pill"], fill="#ffffff")
        draw.text((cx + 82, y - 1), title, font=F["body_bold"], fill=INK)
        draw.text((cx + 82, y + 35), text, font=F["small"], fill=MUTED)
        if idx < len(items) - 1:
            draw.line((cx + 26, y + 60, cx + 26, y + 102), fill="#bfdbfe", width=3)


def audience_grid(base):
    draw = ImageDraw.Draw(base)
    rounded_shadow(base, (RIGHT_X, 230, RIGHT_X + RIGHT_W, 760), radius=12, fill="#ffffff", outline=LINE)
    cells = [
        ("CFOs", "Scenario planning, board packs, runway", "blue"),
        ("Founders", "Investor-ready narrative and numbers", "teal"),
        ("FP&A Teams", "Repeatable forecasts and checks", "purple"),
        ("Analysts", "Transparent model logic", "orange"),
        ("Investors", "Diligence-ready assumptions", "green"),
        ("VC Teams", "Portfolio review and capital use", "blue"),
    ]
    for idx, (title, text, tone) in enumerate(cells):
        col, row = idx % 2, idx // 2
        x = RIGHT_X + 54 + col * 405
        y = 290 + row * 140
        color = {"blue": BLUE, "teal": TEAL, "orange": ORANGE, "purple": PURPLE, "green": GREEN}[tone]
        draw.rounded_rectangle((x, y, x + 350, y + 100), radius=10, fill="#f8fafc", outline=LINE, width=1)
        draw.rounded_rectangle((x + 18, y + 20, x + 28, y + 80), radius=4, fill=color)
        draw.text((x + 48, y + 20), title, font=F["body_bold"], fill=INK)
        draw_wrapped(draw, text, x + 48, y + 55, F["small"], MUTED, 260, 24)
    draw.text((RIGHT_X + 58, 690), "One shared model. Many better decisions.", font=font("sans", 30, True), fill=TEAL)


def use_case_matrix(base):
    draw = ImageDraw.Draw(base)
    rounded_shadow(base, (RIGHT_X, 210, RIGHT_X + RIGHT_W, 800), radius=12, fill="#ffffff", outline=LINE)
    rows = [
        ("Fundraising", "CAC, burn, runway, revenue build"),
        ("Board Planning", "Monthly operating plan and KPI pack"),
        ("SaaS Revenue", "MRR, ARR, churn, expansion revenue"),
        ("Diligence", "Assumption review and capital efficiency"),
        ("Runway", "Cash bridge, deployment, downside cases"),
    ]
    draw.text((RIGHT_X + 54, 262), "Use Case", font=F["small_bold"], fill=MUTED)
    draw.text((RIGHT_X + 370, 262), "Generated Finance Output", font=F["small_bold"], fill=MUTED)
    draw.line((RIGHT_X + 54, 300, RIGHT_X + RIGHT_W - 54, 300), fill=LINE, width=1)
    for idx, (left, right) in enumerate(rows):
        y = 330 + idx * 84
        draw.text((RIGHT_X + 54, y), left, font=F["body_bold"], fill=INK)
        draw_wrapped(draw, right, RIGHT_X + 370, y + 2, F["body"], TEXT, 440, 34)


def cta_panel(base):
    draw = ImageDraw.Draw(base)
    rounded_shadow(base, (RIGHT_X, 192, RIGHT_X + RIGHT_W, 840), radius=12, fill="#ffffff", outline=LINE)
    product_panel(base, SCREENSHOTS["dashboard"], "Sample workbook", "Download the sample workbook from the showcase", RIGHT_X + 58, 248, RIGHT_W - 116, 500)
    draw.rounded_rectangle((RIGHT_X + 58, 780, RIGHT_X + 354, 838), radius=8, fill=BLUE)
    draw.text((RIGHT_X + 88, 797), "Watch Demo Video", font=F["pill"], fill="#ffffff")
    draw.rounded_rectangle((RIGHT_X + 380, 780, RIGHT_X + 690, 838), radius=8, fill="#ffffff", outline=LINE, width=1)
    draw.text((RIGHT_X + 410, 797), "Download Workbook", font=F["pill"], fill=INK)


def slide(step, label, eyebrow, title, subtitle, left, right):
    img, draw = base_slide(step, label)
    start_y = header(draw, eyebrow, title, subtitle)
    left(img, draw, max(start_y + 44, 520))
    right(img, draw)
    img.convert("RGB").save(OUT / f"slide-{step:02d}.png", quality=95)


slide(
    1,
    "Positioning",
    "New Studio Capability",
    "Finance Model Studio",
    "A polished product demonstration for CFOs, founders, finance teams, analysts, and investors.",
    lambda img, draw, y: (pill(draw, "Solution Architect Walkthrough", LEFT_X, y, 360, "teal"), bullet_list(draw, ["From business brief to working model", "Designed for decision-ready finance", "Excel output with dashboard and checks"], LEFT_X, y + 110)),
    lambda img, draw: product_panel(img, SCREENSHOTS["dashboard"], "Investor dashboard", "Studio-generated executive finance view"),
)

slide(
    2,
    "Input To Model",
    "What We Started With",
    "Narrative Becomes Numbers",
    "Studio turns planning language, fundraising assumptions, and operating detail into model structure.",
    lambda img, draw, y: bullet_list(draw, ["Seed-stage business brief", "Acquisition and conversion assumptions", "Pricing, revenue, costs, hiring, runway", "Compliance and funding deployment milestones"], LEFT_X, y),
    lambda img, draw: workflow_panel(img, [("Business brief", "Narrative, assumptions, and goals", "orange"), ("Structured logic", "Funnels, schedules, and scenarios", "blue"), ("Validation", "Checks for confidence before sharing", "purple"), ("Workbook output", "Editable Excel model and dashboard", "teal")]),
)

slide(
    3,
    "Output Scope",
    "Generated Output",
    "One Integrated Workbook",
    "The output is an editable Excel model with connected schedules and decision-ready views.",
    lambda img, draw, y: (metric_card(draw, "Monthly forecast periods", "24", LEFT_X, y, 205, BLUE), metric_card(draw, "Workbook sheets", "11", LEFT_X + 232, y, 205, TEAL), metric_card(draw, "Validation status", "PASS", LEFT_X + 464, y, 205, GREEN), bullet_list(draw, ["Editable assumptions", "Acquisition and revenue funnels", "P&L, balance sheet, cash runway", "Funding deployment and dashboard"], LEFT_X, y + 170)),
    lambda img, draw: product_panel(img, SCREENSHOTS["pnl"], "Profit and loss", "Linked monthly P&L schedule"),
)

slide(
    4,
    "Audience Value",
    "Why It Matters",
    "Built For Finance Leaders",
    "Different stakeholders get the same thing they need most: clarity, speed, and traceability.",
    lambda img, draw, y: bullet_list(draw, ["CFOs: faster planning cycles", "Founders: stronger investor conversations", "Finance teams: repeatable model structure", "Analysts: transparent assumptions and checks", "Investors: clearer diligence signals"], LEFT_X, y),
    lambda img, draw: audience_grid(img),
)

slide(
    5,
    "Dashboard View",
    "Dashboard View",
    "Investor-Ready Summary",
    "Studio creates management-ready charts and KPIs so stakeholders can inspect the business quickly.",
    lambda img, draw, y: bullet_list(draw, ["Users, revenue, gross margin, EBITDA", "Acquisition channel contribution", "Funding allocation and CAC", "Runway and cash visibility"], LEFT_X, y),
    lambda img, draw: product_panel(img, SCREENSHOTS["dashboard"], "Investor dashboard", "Board and investor KPI summary"),
)

slide(
    6,
    "Model Assurance",
    "Quality Controls",
    "Checks Built In",
    "A good model should be auditable. Studio adds validation views that support review before sharing.",
    lambda img, draw, y: bullet_list(draw, ["Reconciliation checks", "Forecast sanity checks", "PASS, WARNING, and FAIL indicators", "Clearer review before publishing"], LEFT_X, y),
    lambda img, draw: product_panel(img, SCREENSHOTS["checks"], "Validation checks", "Automated model checks"),
)

slide(
    7,
    "Use Cases",
    "Use Cases",
    "More Than Fundraising",
    "The same capability supports a broad set of finance and investment workflows.",
    lambda img, draw, y: bullet_list(draw, ["Startup fundraising models", "Board operating plans", "SaaS revenue and ARR planning", "Investor diligence packs", "Capital allocation and runway analysis"], LEFT_X, y),
    lambda img, draw: use_case_matrix(img),
)

slide(
    8,
    "Studio Workflow",
    "How Teams Create With Studio",
    "Brief. Review. Generate.",
    "Studio handles the heavy structure while teams keep control of business judgement.",
    lambda img, draw, y: bullet_list(draw, ["Bring the business brief", "Clarify assumptions and scenarios", "Generate linked schedules and dashboards", "Review checks, iterate, and publish"], LEFT_X, y),
    lambda img, draw: workflow_panel(img, [("Brief", "Describe the business and planning goal", "orange"), ("Review", "Confirm assumptions and scenarios", "blue"), ("Generate", "Create model, dashboard, and checks", "teal"), ("Publish", "Share a polished finance deliverable", "purple")]),
)

slide(
    9,
    "CTA",
    "Call To Action",
    "Bring Your Brief",
    "NebulaCloud Studio turns it into a working financial model for planning, fundraising, diligence, and growth decisions.",
    lambda img, draw, y: (pill(draw, "CFOs", LEFT_X, y, 120, "blue"), pill(draw, "Founders", LEFT_X + 150, y, 170, "teal"), pill(draw, "Finance Teams", LEFT_X + 350, y, 240, "purple"), pill(draw, "Analysts", LEFT_X, y + 84, 170, "orange"), pill(draw, "Investors", LEFT_X + 200, y + 84, 180, "green"), draw.text((LEFT_X, y + 238), "nebulacloud.studio", font=font("sans", 44, True), fill=TEAL)),
    lambda img, draw: cta_panel(img),
)

print(f"Rendered polished frames to {OUT}")
