import tkinter as tk


def draw_line_plot(canvas: tk.Canvas, xs: list, ys: list, title: str):
    """Draw a simple line plot on the given canvas."""
    width = int(canvas["width"])
    height = int(canvas["height"])
    if not xs or not ys:
        return
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    if min_y == max_y:
        min_y -= 1
        max_y += 1
    scale_x = width / (max_x - min_x)
    scale_y = height / (max_y - min_y)
    points = []
    for x, y in zip(xs, ys):
        cx = (x - min_x) * scale_x
        cy = height - (y - min_y) * scale_y
        points.append((cx, cy))
    # draw axes for better readability
    if min_x <= 0 <= max_x:
        axis_x = (0 - min_x) * scale_x
        canvas.create_line(axis_x, 0, axis_x, height, fill="gray", dash=(2,))
    if min_y <= 0 <= max_y:
        axis_y = height - (0 - min_y) * scale_y
        canvas.create_line(0, axis_y, width, axis_y, fill="gray", dash=(2,))

    for i in range(1, len(points)):
        canvas.create_line(points[i - 1][0], points[i - 1][1], points[i][0], points[i][1], fill="blue")
    canvas.create_text(10, 10, text=title, anchor="nw")
