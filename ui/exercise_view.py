import tkinter as tk
from ui.theme import PALETTE, ThemedButton
from ui.punctaj import Punctaj 
from tkinter import messagebox
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "labs")


class ExerciseView(tk.Frame):
    def __init__(self, master, controller, lab_name, ex_name):
        super().__init__(master, bg=PALETTE["background"])
        self.controller = controller
        self.lab_name = lab_name
        self.ex_name = ex_name

        self.flag = None
        self.hint = None
        self.exercise_text = None

        self.load_files()
        self.create_widgets()

    def load_files(self):
        base_path = os.path.join(DATA_PATH, self.lab_name, self.ex_name)
        try:
            with open(os.path.join(base_path, "enunt.md"), "r", encoding="utf-8") as f:
                self.exercise_text = f.read()
        except Exception:
            self.exercise_text = "Nu am putut încărca enunțul exercițiului."

        try:
            with open(os.path.join(base_path, "hint.txt"), "r", encoding="utf-8") as f:
                self.hint = f.read()
        except Exception:
            self.hint = "Nu exista hint disponibil."

        try:
            with open(os.path.join(base_path, "flag.txt"), "r", encoding="utf-8") as f:
                self.flag = f.read().strip()
        except Exception:
            self.flag = None

    def create_widgets(self):
        header = tk.Frame(self, bg=PALETTE["background"])
        header.pack(fill="x")

        back_btn = ThemedButton(header, text="⬅ Înapoi", command=self.on_back)
        back_btn.pack(side="left", padx=10, pady=10)

        title = tk.Label(
            header,
            text=self.ex_name,
            bg=PALETTE["background"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(pady=10)

        # Frame pentru text cu scrollbar
        text_frame = tk.Frame(self, bg=PALETTE["background"])
        text_frame.pack(fill="both", expand=True, padx=30, pady=10)

        self.text_widget = tk.Text(
            text_frame,
            wrap="word",
            bg=PALETTE["button_bg"],
            fg=PALETTE["foreground"],
            font=("Consolas", 12),
            bd=0,
            relief="flat",
            insertbackground=PALETTE["foreground"],  # cursor color
        )
        self.text_widget.insert("1.0", self.exercise_text)
        self.text_widget.config(state="disabled")
        self.text_widget.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=self.text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_widget.config(yscrollcommand=scrollbar.set)

        input_frame = tk.Frame(self, bg=PALETTE["background"])
        input_frame.pack(fill="x", pady=15, padx=30)

        flag_label = tk.Label(
            input_frame,
            text="Introdu flag-ul:",
            bg=PALETTE["background"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 12),
        )
        flag_label.pack(side="left")

        self.flag_entry = tk.Entry(
            input_frame,
            font=("Consolas", 12),
            bg=PALETTE["button_bg"],
            fg=PALETTE["foreground"],
            insertbackground=PALETTE["foreground"],
            relief="flat",
            bd=2,
            highlightthickness=1,
            highlightbackground=PALETTE["accent"],
            highlightcolor=PALETTE["accent"],
        )
        self.flag_entry.pack(side="left", fill="x", expand=True, padx=10)

        check_btn = ThemedButton(input_frame, text="Check", command=self.check_flag)
        check_btn.pack(side="left", padx=10)

        hint_btn = ThemedButton(input_frame, text="Hint", command=self.show_hint)
        hint_btn.pack(side="left")

    def on_back(self):
        self.controller.show_exercise_list(self.lab_name)

    def check_flag(self):
        user_flag = self.flag_entry.get().strip()
        if not self.flag:
            messagebox.showwarning("Eroare", "Flag-ul nu este disponibil pentru acest exercițiu.")
            return
        if user_flag == self.flag:
            Punctaj().finalize_exercise(self.lab_name, self.ex_name)

            score = Punctaj().get_score(self.lab_name, self.ex_name)
            messagebox.showinfo("Felicitări!", "Flag corect!")
        else:
            messagebox.showerror("Incorect", "Flag greșit. Încearcă din nou.")

    def show_hint(self):
        Punctaj().use_hint(self.lab_name, self.ex_name)
        messagebox.showinfo("Hint", self.hint)
