from mss import mss, tools


def sct(box: tuple[int, int, int, int], output: str = "screenshot.png") -> str:
    """Capture a screenshot of the selected box and save it to disk."""
    x1, y1, x2, y2 = box
    width = x2 - x1
    height = y2 - y1

    if width <= 0 or height <= 0:
        raise ValueError("Selection box must have positive width and height")

    with mss() as sct:

        monitor = {"top": y1, "left": x1, "width": width, "height": height}

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return output