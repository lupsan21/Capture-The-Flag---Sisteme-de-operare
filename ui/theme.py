import tkinter as tk
from tkinter import ttk


PALETTE = {
    "background": "#292D3E",    # fundal general
    "foreground": "#A6ACCD",    # text normal
    "button_bg": "#444267",     # buton normal
    "button_fg": "#FFFFFF",     # text pe buton
    "hover": "#5C598B",         # hover pe buton
    "primary": "#82AAFF",       # accent primar (albastru electric)
    "accent": "#C792EA"         # accent alternativ (mov pastel)
}

def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Custom.TButton",
                    background=PALETTE["button_bg"],
                    foreground=PALETTE["button_fg"],
                    borderwidth=0,
                    focusthickness=3,
                    focuscolor=PALETTE["primary"],
                    padding=8,
                    font=("Segoe UI", 11))

    style.map("Custom.TButton",
              background=[('active', PALETTE["hover"])],
              foreground=[('active', PALETTE["button_fg"])])

    style.configure("Hover.TButton",
                    background=PALETTE["hover"],
                    foreground=PALETTE["button_fg"])

    style.configure("TLabel",
                    background=PALETTE["background"],
                    foreground=PALETTE["foreground"],
                    font=("Segoe UI", 12))

    style.configure("TFrame",
                    background=PALETTE["background"])

# Buton cu efect de hover
class ThemedButton(ttk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(style="Custom.TButton")

    def on_enter(self, e):
        self.configure(style="Hover.TButton")

    def on_leave(self, e):
        self.configure(style="Custom.TButton")

class BackButton(ThemedButton):
    def __init__(self, parent, command):
        super().__init__(parent, text="← Înapoi", command=command)
        self.pack(pady=10, padx=10, anchor="w")
