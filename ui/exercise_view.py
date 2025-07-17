import tkinter as tk
from ui.theme import PALETTE, ThemedButton
from ui.punctaj import Punctaj 
from tkinter import messagebox
import os

# Stabileste calea de baza a fisierului curent
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Calea catre folderul "labs" care contine toate laboratoarele
DATA_PATH = os.path.join(BASE_DIR, "..", "labs")


class ExerciseView(tk.Frame):
    def __init__(self, master, controller, lab_name, ex_name):
        # Initializare cadru cu fundalul temei
        super().__init__(master, bg=PALETTE["background"])
        self.controller = controller  # Controlerul aplicatiei (pentru navigare)
        self.lab_name = lab_name  # Numele laboratorului selectat
        self.ex_name = ex_name  # Numele exercitiului selectat

        # Atribut pentru continutul enuntului, hint-ului si flag-ului
        self.flag = None
        self.hint = None
        self.exercise_text = None

        # Incarca fisierele necesare pentru exercitiu
        self.load_files()
        # Creeaza interfata grafica
        self.create_widgets()

    def load_files(self):
        # Incarca enuntul, hint-ul si flag-ul din fisierele respective
        base_path = os.path.join(DATA_PATH, self.lab_name, self.ex_name)

        # Incarca enuntul
        try:
            with open(os.path.join(base_path, "enunt.md"), "r", encoding="utf-8") as f:
                self.exercise_text = f.read()
        except Exception:
            self.exercise_text = "Nu am putut incarca enuntul exercitiului."

        # Incarca hint-ul
        try:
            with open(os.path.join(base_path, "hint.txt"), "r", encoding="utf-8") as f:
                self.hint = f.read()
        except Exception:
            self.hint = "Nu exista hint disponibil."

        # Incarca flag-ul
        try:
            with open(os.path.join(base_path, "flag.txt"), "r", encoding="utf-8") as f:
                self.flag = f.read().strip()
        except Exception:
            self.flag = None

    def create_widgets(self):
        # Creeaza antetul cu titlul si butonul de intoarcere
        header = tk.Frame(self, bg=PALETTE["background"])
        header.pack(fill="x")

        # Buton pentru a reveni la lista de exercitii
        back_btn = ThemedButton(header, text="⬅ Înapoi", command=self.on_back)
        back_btn.pack(side="left", padx=10, pady=10)

        # Eticheta cu titlul (numele exercitiului)
        title = tk.Label(
            header,
            text=self.ex_name,
            bg=PALETTE["background"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(pady=10)

        # Creeaza zona de text pentru afisarea enuntului, cu scrollbar
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
            insertbackground=PALETTE["foreground"],  # culoarea cursorului
        )
        self.text_widget.insert("1.0", self.exercise_text)
        self.text_widget.config(state="disabled")  # textul nu poate fi editat
        self.text_widget.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=self.text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_widget.config(yscrollcommand=scrollbar.set)

        # Creeaza zona pentru input-ul flag-ului si butoanele Check si Hint
        input_frame = tk.Frame(self, bg=PALETTE["background"])
        input_frame.pack(fill="x", pady=15, padx=30)

        # Eticheta pentru input
        flag_label = tk.Label(
            input_frame,
            text="Introdu flag-ul:",
            bg=PALETTE["background"],
            fg=PALETTE["foreground"],
            font=("Segoe UI", 12),
        )
        flag_label.pack(side="left")

        # Camp pentru introducerea flag-ului
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

        # Buton pentru verificarea flag-ului
        check_btn = ThemedButton(input_frame, text="Check", command=self.check_flag)
        check_btn.pack(side="left", padx=10)

        # Buton pentru afisarea hint-ului
        hint_btn = ThemedButton(input_frame, text="Hint", command=self.show_hint)
        hint_btn.pack(side="left")

    def on_back(self):
        # Navigheaza inapoi la lista de exercitii din laboratorul curent
        self.controller.show_exercise_list(self.lab_name)

    def check_flag(self):
        # Verifica daca flag-ul introdus este corect
        user_flag = self.flag_entry.get().strip()

        if not self.flag:
            # Daca nu exista flag in fisier
            messagebox.showwarning("Eroare", "Flag-ul nu este disponibil pentru acest exercitiu.")
            return

        if user_flag == self.flag:
            # Daca flag-ul este corect, finalizeaza exercitiul si arata mesaj de succes
            Punctaj().finalize_exercise(self.lab_name, self.ex_name)
            score = Punctaj().get_score(self.lab_name, self.ex_name)
            messagebox.showinfo("Felicitari!", "Flag corect!")
        else:
            # Daca flag-ul este gresit, afiseaza mesaj de eroare
            messagebox.showerror("Incorect", "Flag gresit. Incearca din nou.")

    def show_hint(self):
        # Marcheaza hint-ul ca folosit si afiseaza mesajul cu hint-ul
        Punctaj().use_hint(self.lab_name, self.ex_name)
        messagebox.showinfo("Hint", self.hint)
