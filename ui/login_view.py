import tkinter as tk
from ui.theme import PALETTE, ThemedButton

class LoginView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg=PALETTE["background"])
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="Autentificare", font=("Segoe UI", 20, "bold"),
                         bg=PALETTE["background"], fg=PALETTE["primary"])
        title.pack(pady=40)

        self.username_entry = tk.Entry(self, font=("Segoe UI", 12))
        self.username_entry.pack(pady=10)
        self.username_entry.insert(0, "Nume")

        self.group_entry = tk.Entry(self, font=("Segoe UI", 12))
        self.group_entry.pack(pady=10)
        self.group_entry.insert(0, "Grupă")

        login_btn = ThemedButton(self, text="Login", command=self.handle_login)
        login_btn.pack(pady=20)

        back_btn = ThemedButton(self, text="⬅ Înapoi", command=self.controller.show_start_menu)
        back_btn.pack(pady=10)

    def handle_login(self):
        nume = self.username_entry.get().strip()
        grupa = self.group_entry.get().strip()
        print(f"[LOGIN] Utilizator: {nume}, Grupă: {grupa}")
        # Poți salva utilizatorul în controller sau într-un fișier aici
        self.controller.show_lab_selector()
