import tkinter as tk
from ui.theme import PALETTE, ThemedButton
from ui.punctaj import Punctaj 
import tkinter.messagebox as mb
import os

# Stabileste calea de baza a fisierului curent
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Stabileste calea catre folderul "labs", aflat cu un nivel mai sus
DATA_PATH = os.path.join(BASE_DIR, "..", "labs")


class ExerciseList(tk.Frame):
    def __init__(self, master, controller, lab_name):
        # Initializeaza cadrul principal
        super().__init__(master, bg=PALETTE["background"])
        self.controller = controller  # Controlerul aplicatiei (pentru navigare)
        self.lab_name = lab_name  # Numele laboratorului curent
        self.exercises = self.load_exercises()  # Incarca lista de exercitii
        self.ex_display_map = {}  # Mapare intre indexul din listbox si numele real al exercitiului
        self.create_widgets()  # Creeaza elementele grafice

    def load_exercises(self):
        # Incarca exercitiile din directorul laboratorului
        lab_path = os.path.join(DATA_PATH, self.lab_name)
        if os.path.exists(lab_path):
            # Returneaza o lista sortata a folderelor care reprezinta exercitii (Exercitiu 1, 2 etc.)
            return sorted(
                [d for d in os.listdir(lab_path) if os.path.isdir(os.path.join(lab_path, d))],
                key=lambda x: int(x.split(" ")[1])  # Sorteaza numeric dupa numarul exercitiului
            )
        else:
            return []  # Daca nu exista folderul, returneaza lista goala

    def create_widgets(self):
        # Creeaza antetul cu butonul de intoarcere si titlul
        header = tk.Frame(self, bg=PALETTE["background"])
        header.pack(fill="x")

        # Butonul de intoarcere
        back_btn = ThemedButton(header, text="⬅ Înapoi", command=self.on_back)
        back_btn.pack(side="left", padx=10, pady=10)

        # Titlul cu numele laboratorului
        title = tk.Label(
            header,
            text=f"Exerciții - {self.lab_name}",
            bg=PALETTE["background"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=10)

        # Creeaza zona pentru lista de exercitii
        list_frame = tk.Frame(self, bg=PALETTE["background"])
        list_frame.pack(fill="both", expand=True, padx=50, pady=10)

        # Scrollbar pentru lista
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        # Creeaza listbox-ul pentru afisarea exercitiilor
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

        # Adauga exercitiile in listbox, cu punctajul daca este cazul
        for idx, ex in enumerate(self.exercises):
            score = Punctaj().get_score(self.lab_name, ex)  # Obtine punctajul pentru exercitiu
            display_name = f"{ex} - {score}p" if score > 0 else ex  # Adauga punctajul daca e > 0
            self.listbox.insert(tk.END, display_name)
            self.ex_display_map[idx] = ex  # Mapam indexul din listbox la numele real al exercitiului

        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<Double-1>", self.on_double_click)  # Dublu-click deschide exercitiul
        scrollbar.config(command=self.listbox.yview)  # Scrollbar legat de listbox

        # Buton pentru deschiderea exercitiului selectat
        open_btn = ThemedButton(self, text="Deschide exercițiu", command=self.open_selected_exercise)
        open_btn.pack(pady=15)

    def on_back(self):
        # Se intoarce la ecranul de selectie al laboratorului
        self.controller.show_lab_selector()

    def on_double_click(self, event):
        # Deschide exercitiul la dublu-click
        self.open_selected_exercise()

    def open_selected_exercise(self):
        # Deschide exercitiul selectat din lista
        sel = self.listbox.curselection()
        if sel:
            index = sel[0]
            ex_name = self.ex_display_map.get(index)
            self.controller.show_exercise_view(self.lab_name, ex_name)  # Navigheaza catre exercitiul selectat
        else:
            mb.showwarning("Atenție", "Selectează un exercițiu mai întâi.")  # Avertizeaza daca nu a fost selectat nimic
