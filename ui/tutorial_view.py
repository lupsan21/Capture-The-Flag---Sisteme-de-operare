import tkinter as tk
from ui.theme import PALETTE, ThemedButton
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TUTORIAL_PATH = os.path.join(BASE_DIR, "..", "tutorial.md")

class TutorialView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg=PALETTE["background"])
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        header = tk.Frame(self, bg=PALETTE["background"])
        header.pack(fill="x")

        back_btn = ThemedButton(header, text="⬅ Înapoi", command=self.controller.show_start_menu)
        back_btn.pack(side="left", padx=10, pady=10)

        title = tk.Label(
            header,
            text="Tutorial de joc",
            font=("Segoe UI", 20, "bold"),
            bg=PALETTE["background"],
            fg=PALETTE["foreground"]
        )
        title.pack(pady=10)

        content_frame = tk.Frame(self, bg=PALETTE["background"])
        content_frame.pack(fill="both", expand=True, padx=40, pady=10)

        scrollbar = tk.Scrollbar(content_frame)
        scrollbar.pack(side="right", fill="y")

        text_widget = tk.Text(
            content_frame,
            wrap="word",
            bg=PALETTE["button_bg"],
            fg=PALETTE["foreground"],
            font=("Consolas", 12),
            yscrollcommand=scrollbar.set,
            bd=0,
            relief="flat",
            state="normal"
        )
        try:
            with open(TUTORIAL_PATH, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            content = "Fișierul tutorial.md nu a fost găsit."

        text_widget.insert("1.0", content)
        text_widget.config(state="disabled")
        text_widget.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_widget.yview)
