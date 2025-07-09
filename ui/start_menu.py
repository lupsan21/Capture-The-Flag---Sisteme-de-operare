import tkinter as tk
from PIL import Image, ImageTk
from ui.theme import PALETTE

class StartMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=PALETTE["background"])
        self.controller = controller

        title = tk.Label(
            self,
            text="Capture the flag\nSisteme de operare",
            font=("Helvetica", 24, "bold"),
            fg=PALETTE["foreground"],
            bg=PALETTE["background"]
        )
        title.pack(pady=(40, 10))

        btn_width = 20  

        lab_btn = tk.Button(
            self,
            text="Laboratoare",
            command=self.controller.show_lab_selector,
            font=("Segoe UI", 14, "bold"),
            width=btn_width,
            bg=PALETTE["button_bg"],
            fg=PALETTE["button_fg"],
            activebackground=PALETTE["accent"],
            activeforeground=PALETTE["button_fg"],
            bd=0,
            highlightthickness=0,
            cursor="hand2"
        )
        lab_btn.pack(pady=(40, 5))

        tutorial_btn = tk.Button(
            self,
            text="Tutorial",
            command=self.controller.show_tutorial,
            font=("Segoe UI", 14, "bold"),
            width=btn_width,
            bg=PALETTE["button_bg"],
            fg=PALETTE["button_fg"],
            activebackground=PALETTE["accent"],
            activeforeground=PALETTE["button_fg"],
            bd=0,
            highlightthickness=0,
            cursor="hand2"
        )
        tutorial_btn.pack(pady=(0, 5))

        reset_btn = tk.Button(
            self,
            text="Resetează progresul",
            command=self.controller.reset_progress,
            font=("Segoe UI", 14, "bold"),
            width=btn_width,
            bg=PALETTE["button_bg"],
            fg=PALETTE["button_fg"],
            activebackground=PALETTE["accent"],
            activeforeground=PALETTE["button_fg"],
            bd=0,
            highlightthickness=0,
            cursor="hand2"
        )
        reset_btn.pack(pady=(0,10))

       
        img = Image.open("penguin.png").resize((300, 300))
        self.photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(self, image=self.photo, bg=PALETTE["background"])
        image_label.pack(pady=20)
