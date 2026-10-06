from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "media"
SOURCE = ROOT / "assets" / "generated"


def cell(sheet, cols, rows, index):
    width, height = sheet.size
    col, row = index % cols, index // cols
    x0, x1 = round(col * width / cols), round((col + 1) * width / cols)
    y0, y1 = round(row * height / rows), round((row + 1) * height / rows)
    return sheet.crop((x0, y0, x1, y1))


def cover(image, size, zoom=1.0, pan=0.0):
    target_w, target_h = size
    ratio = max(target_w / image.width, target_h / image.height) * zoom
    resized = image.resize((round(image.width * ratio), round(image.height * ratio)), Image.Resampling.LANCZOS)
    extra_x, extra_y = resized.width - target_w, resized.height - target_h
    x = max(0, min(extra_x, round(extra_x * (0.5 + pan))))
    y = max(0, min(extra_y, round(extra_y * 0.47)))
    return resized.crop((x, y, x + target_w, y + target_h))


def save_loop(image, output, size, direction=1):
    output.parent.mkdir(parents=True, exist_ok=True)
    base = ImageEnhance.Color(image.convert("RGB")).enhance(0.96)
    poster = cover(base, size, 1.025, -0.05 * direction)
    poster.save(output.with_suffix(".jpg"), quality=84, optimize=True, progressive=True)
    frames = []
    count = 20
    for frame_no in range(count):
        progress = frame_no / (count - 1)
        smooth = progress * progress * (3 - 2 * progress)
        frames.append(cover(base, size, 1.02 + 0.10 * smooth, (-0.08 + 0.16 * smooth) * direction))
    frames[0].save(output, save_all=True, append_images=frames[1:], duration=120, loop=0, quality=68, method=4)


def main():
    theme_sheet = Image.open(SOURCE / "theme-sheet.png").convert("RGB")
    region_sheet = Image.open(SOURCE / "region-sheet.png").convert("RGB")
    line_sheet = Image.open(SOURCE / "line-sheet.png").convert("RGB")

    theme_names = ["kids", "parents", "far", "near", "nature", "heritage", "city", "rest", "food", "first"]
    region_names = ["east-med", "west-med", "alaska", "east-caribbean", "west-caribbean", "southeast-asia", "northeast-asia", "other"]
    line_names = ["royal", "ncl", "disney", "msc", "princess"]

    for index, name in enumerate(theme_names):
        target = DIST / "themes" / f"{name}.jpg"
        target.parent.mkdir(parents=True, exist_ok=True)
        cover(cell(theme_sheet, 5, 2, index), (640, 420), 1.02).save(target, quality=85, optimize=True, progressive=True)

    for index, name in enumerate(region_names):
        save_loop(cell(region_sheet, 4, 2, index), DIST / "regions" / f"{name}.webp", (560, 340), 1 if index % 2 == 0 else -1)

    for index, name in enumerate(line_names):
        save_loop(cell(line_sheet, 3, 2, index), DIST / "lines" / f"{name}.webp", (480, 620), -1 if index % 2 == 0 else 1)


if __name__ == "__main__":
    main()
