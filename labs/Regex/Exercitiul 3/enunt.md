Fișierul system_access.log conține jurnale de autentificare în formatul:

[user=NUME] [ip=ADRESA] [auth=success]

Dar un singur utilizator — aka — a strecurat un mesaj ascuns, adăugând un câmp suplimentar în log:

[user=aka] [ip=10.10.10.10] [auth=success] [note=CTF{...}]

Identifică linia care conține flagul valid și extrage doar flagul în format CTF{...} folosind comenzi Linux și expresii regulate.