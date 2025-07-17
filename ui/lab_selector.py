import tkinter as tk
from ui.theme import PALETTE, ThemedButton
import tkinter.messagebox as mb

class LabSelector(tk.Frame):
    # Lista cu numele laboratoarelor disponibile
    LABS = [
        "Comenzi Linux",
        "Regex",
        "Scripturi"
    ]

    def __init__(self, master, controller):
        # Initializare cadru cu tema aplicatiei
        super().__init__(master, bg=PALETTE["background"])
        self.controller = controller  # Controlerul principal (gestioneaza navigarea)
        self.create_widgets()  # Creeaza elementele grafice

    def create_widgets(self):
        # Creeaza antetul cu butonul de intoarcere si titlul
        header = tk.Frame(self, bg=PALETTE["background"])
        header.pack(fill="x")

        # Butonul de intoarcere la meniul principal
        back_btn = ThemedButton(header, text="⬅ Înapoi", command=self.on_back)
        back_btn.pack(side="left", padx=10, pady=10)

        # Titlul sectiunii
        label = tk.Label(
            header,
            text="Selecteaza laboratorul",
            bg=PALETTE["background"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 18, "bold")
        )
        label.pack(pady=10)

        # Creeaza frame-ul pentru lista cu scrollbar
        list_frame = tk.Frame(self, bg=PALETTE["background"])
        list_frame.pack(fill="both", expand=True, padx=50, pady=10)

        # Scrollbar vertical pentru listbox
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        # Lista cu laboratoarele disponibile
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

        # Adauga fiecare laborator in listbox
        for lab in self.LABS:
            self.listbox.insert(tk.END, lab)

        self.listbox.pack(side="left", fill="both", expand=True)

        # Dublu-click pe un element din lista deschide laboratorul
        self.listbox.bind("<Double-1>", self.on_double_click)

        # Leaga scrollbar-ul la listbox
        scrollbar.config(command=self.listbox.yview)

        # Buton pentru deschiderea laboratorului selectat
        open_btn = ThemedButton(self, text="Deschide laborator", command=self.open_selected_lab)
        open_btn.pack(pady=15)

    def on_back(self):
        # Navigheaza inapoi la meniul de start
        self.controller.show_start_menu()

    def on_double_click(self, event):
        # Deschide laboratorul cand se face dublu-click pe un element
        self.open_selected_lab()

    def open_selected_lab(self):
        # Obtine laboratorul selectat si deschide lista de exercitii
        selection = self.listbox.curselection()
        if selection:
            lab_name = self.listbox.get(selection[0])
            self.controller.show_exercise_list(lab_name)
        else:
            # Afiseaza mesaj de avertizare daca nu a fost selectat nimic
            mb.showwarning("Atentie", "Selecteaza un laborator mai intai.")
