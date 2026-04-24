import tkinter as tk

class BoxSelector:
    """Track the mouse drag used to draw a screen selection box."""

    def __init__(self, root: tk.Tk) -> None:
        """Set up the transparent canvas and input bindings."""
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
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        root.bind("<Escape>", self.quit)
        root.bind("<Return>", self.confirm)


    def on_press(self, event: tk.Event) -> None:
        """Start a new selection rectangle."""
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
        """Update the selection rectangle while dragging."""
        self.end_x = event.x
        self.end_y = event.y

        if self.rect_id is not None:
            self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_release(self, event: tk.Event) -> None:
        """Store the final selection point when the mouse is released."""
        self.end_x = event.x
        self.end_y = event.y

    def get_box(self) -> tuple[int, int, int, int]:
        """Return the selected box coordinates."""
        return (self.start_x, self.start_y, self.end_x, self.end_y)
        
    def confirm(self, _event: tk.Event | None = None) -> None:
        """Close the overlay after confirming the selection."""
        self.confirmed = True
        self.root.destroy()

    def quit(self, _event: tk.Event | None = None) -> None:
        """Close the overlay without using the selection."""
        self.cancelled = True
        self.root.destroy()
