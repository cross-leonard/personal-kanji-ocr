import tkinter as tk


class BoxSelector:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.rect_id = None
        self.confirmed = False
        self.cancelled = False

        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0, cursor="cross")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Mouse>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        root.bind("<Escape>", self.quit)
        root.bind("<Return>", self.confirm)


    def on_press(self, event: tk.Event) -> None:
        self.start_x = event.x
        self.start_y = event.y
        self.end_x = event.x
        self.end_y = event.y

        if self.rect_id is not None:
            self.canvas.delete(self.rect_id)

        self.rect_id = self.canvas.create_rectangle(
            self.start_x,
            self.start_y,
            self.end_x,
            self.end_y,
            outline="red",
            width=2,
        )

    def on_drag(self, event: tk.Event) -> None:
        self.end_x = event.x
        self.end_y = event.y

        if self.rect_id is not None:
            self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_release(self, event: tk.Event) -> None:
        self.end_x = event.x
        self.end_y = event.y

    def get_box(self) -> tuple[int, int, int, int]:
        x1 = min(self.start_x, self.end_x)
        y1 = min(self.start_y, self.end_y)
        x2 = max(self.start_x, self.end_x)
        y2 = max(self.start_y, self.end_y)
        return (x1, y1, x2, y2)
        
    def confirm(self, _event: tk.Event | None = None) -> None:
        self.confirmed = True
        self.root.destroy()

    def quit(self, _event: tk.Event | None = None) -> None:
        self.cancelled = True
        self.root.destroy()


# add to main later
def select_box() -> tuple[int, int, int, int] | None:
    root = tk.Tk()
    root.title("Draw Selection Box")
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.25)
    root.configure(bg="black")

    selector = BoxSelector(root)
    root.mainloop()

    if selector.cancelled:
        return None

    x1, y1, x2, y2 = selector.get_box()
    if x1 == x2 or y1 == y2:
        return None

    return (x1, y1, x2, y2)
