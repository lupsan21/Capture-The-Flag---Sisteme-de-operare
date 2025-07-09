import tkinter as tk
from ui.theme import PALETTE, ThemedButton
from ui.punctaj import Punctaj 
import tkinter.messagebox as mb
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "labs")


class ExerciseList(tk.Frame):
    def __init__(self, master, controller, lab_name):
        super().__init__(master, bg=PALETTE["background"])
        self.controller = controller
        self.lab_name = lab_name
        self.exercises = self.load_exercises()
        self.ex_display_map = {}  # Mapare între index și nume real
        self.create_widgets()

    def load_exercises(self):
        lab_path = os.path.join(DATA_PATH, self.lab_name)
        if os.path.exists(lab_path):
            return sorted(
                [d for d in os.listdir(lab_path) if os.path.isdir(os.path.join(lab_path, d))],
                key=lambda x: int(x.split(" ")[1])  # ordonare Exercițiu 1, 2, 3...
            )
        else:
            return []

    def create_widgets(self):
        header = tk.Frame(self, bg=PALETTE["background"])
        header.pack(fill="x")

        back_btn = ThemedButton(header, text="⬅ Înapoi", command=self.on_back)
        back_btn.pack(side="left", padx=10, pady=10)

        title = tk.Label(
            header,
            text=f"Exerciții - {self.lab_name}",
            bg=PALETTE["background"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=10)

        list_frame = tk.Frame(self, bg=PALETTE["background"])
        list_frame.pack(fill="both", expand=True, padx=50, pady=10)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            list_frame,
            bg=PALETTE["button_bg"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 14),
            selectbackground=PALETTE["accent"],
            activestyle='none',
            bd=0,
            highlightthickness=0,
            yscrollcommand=scrollbar.set
        )

        for idx, ex in enumerate(self.exercises):
            score = Punctaj().get_score(self.lab_name, ex)
            display_name = f"{ex} - {score}p" if score > 0 else ex
            self.listbox.insert(tk.END, display_name)
            self.ex_display_map[idx] = ex  # mapăm indexul cu numele real

        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<Double-1>", self.on_double_click)
        scrollbar.config(command=self.listbox.yview)

        open_btn = ThemedButton(self, text="Deschide exercițiu", command=self.open_selected_exercise)
        open_btn.pack(pady=15)

    def on_back(self):
        self.controller.show_lab_selector()

    def on_double_click(self, event):
        self.open_selected_exercise()

    def open_selected_exercise(self):
        sel = self.listbox.curselection()
        if sel:
            index = sel[0]
            ex_name = self.ex_display_map.get(index)
            self.controller.show_exercise_view(self.lab_name, ex_name)
        else:
            mb.showwarning("Atenție", "Selectează un exercițiu mai întâi.")
