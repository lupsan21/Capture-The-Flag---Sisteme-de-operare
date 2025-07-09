import tkinter as tk
from ui.theme import PALETTE, ThemedButton
import tkinter.messagebox as mb

class LabSelector(tk.Frame):
    LABS = [
        "Comenzi Linux",
        "Regex",
        "Procese",
        "Sistemul de fișiere",
        "Managementul utilizatorilor",
        "Sistemul de permisiuni",
        "Configurări de rețea",
        "Scripturi"
    ]

    def __init__(self, master, controller):
        super().__init__(master, bg=PALETTE["background"])
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        header = tk.Frame(self, bg=PALETTE["background"])
        header.pack(fill="x")

        back_btn = ThemedButton(header, text="⬅ Înapoi", command=self.on_back)
        back_btn.pack(side="left", padx=10, pady=10)

        label = tk.Label(
            header,
            text="Selectează laboratorul",
            bg=PALETTE["background"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 18, "bold")
        )
        label.pack(pady=10)

        # Frame pentru listbox + scrollbar
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
        for lab in self.LABS:
            self.listbox.insert(tk.END, lab)
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<Double-1>", self.on_double_click)

        scrollbar.config(command=self.listbox.yview)

        open_btn = ThemedButton(self, text="Deschide laborator", command=self.open_selected_lab)
        open_btn.pack(pady=15)

    def on_back(self):
        self.controller.show_start_menu()  # te duce înapoi la meniul principal

    def on_double_click(self, event):
        self.open_selected_lab()

    def open_selected_lab(self):
        selection = self.listbox.curselection()
        if selection:
            lab_name = self.listbox.get(selection[0])
            self.controller.show_exercise_list(lab_name)
        else:
            mb.showwarning("Atenție", "Selectează un laborator mai întâi.")
