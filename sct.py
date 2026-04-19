from mss import mss, tools

def screenshot(box: tuple[int, int, int, int], output: str = "screenshot.png") -> str:
    """Capture a screenshot of the selected box and save it."""
    print("screenshot function called!")
    x1, y1, x2, y2 = box
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1) 
    height = abs(y2 - y1)

    if width <= 0 or height <= 0:
        raise ValueError("Selection box must have positive width and height")

    with mss() as sct:

        monitor = {"top": top, "left": left, "width": width, "height": height}
        
        sct_img = sct.grab(monitor)

        tools.to_png(sct_img.rgb, sct_img.size, output=output)
        
        return output