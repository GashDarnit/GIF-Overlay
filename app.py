import tkinter as tk
from PIL import Image, ImageSequence, ImageTk

speed = {
    "toothless": 50
}

class GIFOverlay:
    def __init__(self, parent, gif_path, name, x=100, y=100):
        self.window = tk.Toplevel(parent)
        self.window.overrideredirect(True)
        self.window.attributes("-topmost", True)
        self.window.attributes("-transparentcolor", "white")
        self.window.geometry(f"+{x}+{y}")

        self.name = name

        self.gif = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.convert("RGBA")) for frame in ImageSequence.Iterator(self.gif)]
        self.label = tk.Label(self.window, bg="white")
        self.label.pack()
        
        self.frame_idx = 0
        self.update_animation()
        
        self.label.bind("<ButtonPress-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.do_move)

    def update_animation(self):
        self.label.configure(image=self.frames[self.frame_idx])
        self.frame_idx = (self.frame_idx + 1) % len(self.frames)
        self.window.after(speed[self.name], self.update_animation)

    def start_move(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def do_move(self, event):
        x = self.window.winfo_x() + event.x - self.start_x
        y = self.window.winfo_y() + event.y - self.start_y
        self.window.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    gifs = [GIFOverlay(root, "gifs/toothless.gif", 'toothless', 100, 100)]
    
    root.mainloop()
