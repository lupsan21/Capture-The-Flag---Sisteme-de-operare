import tkinter as tk
from ui.lab_selector import LabSelector
from ui.exercise_list import ExerciseList
from ui.exercise_view import ExerciseView
from ui.theme import PALETTE, setup_styles  
from ui.start_menu import StartMenu      
from ui.punctaj import Punctaj
from tkinter import messagebox                                                                                       

class SOCheckerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw() 

        self.title("Capture The Flag - Sisteme de operare")
        self.configure(bg=PALETTE["background"])
        self.resizable(False, False)

        setup_styles()

        self.container = tk.Frame(self, bg=PALETTE["background"])
        self.container.pack(fill="both", expand=True)

        self.show_start_menu()
        self.after(0, lambda: self.finalize_window(900, 650))

    def finalize_window(self, width, height):
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.deiconify() 

    def show_tutorial(self):
        self.clear_container()
        from ui.tutorial_view import TutorialView
        tutorial_view = TutorialView(self.container, self)
        tutorial_view.pack(fill="both", expand=True)
        
    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_start_menu(self):
        self.clear_container()
        start_menu = StartMenu(self.container, self)
        start_menu.pack(fill="both", expand=True)

    
    def reset_progress(self):
        confirm = messagebox.askyesno("Confirmare", "Ești sigur că vrei să ștergi progresul?")
        if confirm:
            Punctaj().reset()
            messagebox.showinfo("Resetat", "Progresul a fost șters.")  

    def show_lab_selector(self):
        self.clear_container()
        selector = LabSelector(self.container, self)
        selector.pack(fill="both", expand=True)

    def show_exercise_list(self, lab_name):
        self.clear_container()
        ex_list = ExerciseList(self.container, self, lab_name)
        ex_list.pack(fill="both", expand=True)

    def show_exercise_view(self, lab_name, ex_name):
        self.clear_container()
        ex_view = ExerciseView(self.container, self, lab_name, ex_name)
        ex_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = SOCheckerApp()
    app.mainloop()