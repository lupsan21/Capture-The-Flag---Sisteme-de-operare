import os

class Punctaj:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Punctaj, cls).__new__(cls)
            cls._instance.scores = {}
            cls._instance.hint_used = set()
            cls._instance.load_scores_from_files()
        return cls._instance

    def _get_score_file_path(self, lab, exercitiu):
        base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, "..", "labs", lab, exercitiu, "score.txt")

    def load_scores_from_files(self):
        base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "labs")
        for lab in os.listdir(base):
            lab_path = os.path.join(base, lab)
            if not os.path.isdir(lab_path):
                continue
            for ex in os.listdir(lab_path):
                ex_path = os.path.join(lab_path, ex)
                if not os.path.isdir(ex_path):
                    continue
                score_file = os.path.join(ex_path, "score.txt")
                if os.path.exists(score_file):
                    try:
                        with open(score_file, "r") as f:
                            score = int(f.read().strip())
                            if score in (0, 50, 100):
                                self.scores[(lab, ex)] = score
                            else:
                                self.scores[(lab, ex)] = 0
                    except:
                        self.scores[(lab, ex)] = 0

    def use_hint(self, lab, exercitiu):
        self.hint_used.add((lab, exercitiu))

    def finalize_exercise(self, lab, exercitiu):
        key = (lab, exercitiu)
        current_score = self.scores.get(key, 0)

        if current_score != 0:
            return  # deja finalizat – scorul rămâne blocat

        score = 50 if key in self.hint_used else 100
        self.scores[key] = score
        self._save_score_to_file(lab, exercitiu, score)

    def _save_score_to_file(self, lab, exercitiu, score):
        path = self._get_score_file_path(lab, exercitiu)
        try:
            with open(path, "w") as f:
                f.write(str(score))
        except Exception as e:
            print(f"[Eroare la salvare punctaj]: {e}")

    def get_score(self, lab, exercitiu):
        return self.scores.get((lab, exercitiu), 0)

    def reset(self):
        self.scores.clear()
        self.hint_used.clear()
        base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "labs")
        for lab in os.listdir(base):
            lab_path = os.path.join(base, lab)
            if not os.path.isdir(lab_path):
                continue
            for ex in os.listdir(lab_path):
                ex_path = os.path.join(lab_path, ex)
                if not os.path.isdir(ex_path):
                    continue
                score_file = os.path.join(ex_path, "score.txt")
                try:
                    with open(score_file, "w") as f:
                        f.write("0")
                except:
                    pass
