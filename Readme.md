Idee aplicatie:

Sa zicem ca suntem intr-un office unde angajatii lucreaza pe niste statii ale firmei. Sa zicem ca angajatii lucreaza in ture de cate 5 oameni, deci sunt 5 statii.
Sa zicem ca in firma sunt 15 programatori, fiecare programator lucreaza la 1 din cele 5 statii, deci ar fi cam 3 programatori pe statie. Fiecare programator
are fisierele, mail-urile si programele lui. Statiile nu se inchid niciodata, ci doar intra in stand by daca nu sunt folosite un anumit timp.
Fiecare statie are integrata o camera video. Camera video recunoaste fata programatorului si afiseaza workspace-ul acestuia, adica acel programator vede doar fisierele si tool-urile pe care el le-a creat, sau care i-au fost daruite.

Explicatie fisiere:

/app fisierul pentru aplicatie
/app/static/ # Fisiere statice pentru frontend (de ex. imagini, CSS)
/app/templates/ # Template-uri HTML pentru frontend
/app/face_recognition/ # Codul pentru recunoasterea faciala
/app/file_explorer/ # Codul pentru gestionarea fisierelor
/app/api/ # Codul Codul API-ului pentru gestionarea fisierelor si autentificare
/app/models/ # Modele (de ex fisiere pentru utilizatori)
/app/app.py # Fisierul principal pentru a lansa aplicatia FastAPI

pentru a instala dependintele ruleaza urmatoarea comanda:

pip3 install -r requirements.txt
CA SA FUNCTIONEZE TREBUIE SA AVETI INSTALAT python3 si cmake si probabil si altele, dar daca e cazul imi trimiteti mesaj.

Daca nu va place ceva sau vreti sa schimba,
schimbati si vedem la final ce facem.
