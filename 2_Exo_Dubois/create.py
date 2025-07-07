import os

# Create a folder structure for the forensic exercise
base_path = "forensic_exercise"
subfolders = [
    "01_Logs",
    "02_Capture reseau",
    "03_Mails",
    "04_Entretien",
    "05_Capture_ecran",
    "06_Consignes"
]

# Create the folders
for folder in subfolders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

base_path


# Contenu fictif pour chaque dossier

# 01_Logs - Journal système fictif
log_content = """\
[2025-06-20 18:32:11] User login: mdubois
[2025-06-20 18:35:47] External USB device connected: /dev/sdb1
[2025-06-20 18:36:10] File copied: /home/mdubois/Documents/clients_confidentiels.xlsx
[2025-06-20 18:36:11] File copied: /home/mdubois/Documents/archive.zip
[2025-06-20 18:37:20] External USB device removed: /dev/sdb1
[2025-06-20 18:38:45] User logout: mdubois
"""

with open(os.path.join(base_path, "01_Logs", "journal_systeme.txt"), "w") as f:
    f.write(log_content)

# 02_Capture reseau - Trafic réseau suspect
network_capture = """\
[2025-06-20 18:34:10] Connection to IP 104.26.14.45:443 (encrypted)
[2025-06-20 18:34:12] 560 KB data sent
[2025-06-20 18:34:13] Connection closed
"""

with open(os.path.join(base_path, "02_Capture reseau", "capture_reseau.txt"), "w") as f:
    f.write(network_capture)

# 03_Mails - Extrait d'email
email_content = """\
De : mdubois@entreprise.com
À : contact@exfildata.io
Objet : Dernier jour

Salut, comme convenu, je t’ai laissé un petit paquet. Tu sauras quoi en faire.

- M.
"""

with open(os.path.join(base_path, "03_Mails", "mail_suspect.txt"), "w") as f:
    f.write(email_content)

# 04_Entretien - Interview fictive
interview_content = """\
Entretien avec M. Dubois – 21 juin 2025

Q : Que faisiez-vous le soir du 20 juin sur votre poste ?
R : Je terminais quelques sauvegardes personnelles, c’était mon dernier jour.

Q : Avez-vous utilisé une clé USB ?
R : Oui, pour transférer mes CV et quelques photos.

Q : Que contient le fichier archive.zip ?
R : Je ne me souviens plus, sûrement des documents perso.

Q : Avez-vous envoyé des fichiers à l’extérieur ?
R : Non, je ne vois pas pourquoi je ferais ça.
"""

with open(os.path.join(base_path, "04_Entretien", "entretien_dubois.txt"), "w") as f:
    f.write(interview_content)

# 05_Capture_ecran - Capture d’écran fictive (texte remplacé par description)
screenshot_description = """\
[Image Description]
Une fenêtre d’explorateur de fichiers est ouverte sur le bureau de M. Dubois.
Un fichier nommé 'archive.zip' est visible. Taille : 1.2 Mo
Date de modification : 2025-06-20 18:36
"""

with open(os.path.join(base_path, "05_Capture_ecran", "capture_ecran.txt"), "w") as f:
    f.write(screenshot_description)

# 06_Consignes - Énoncé pédagogique
instructions = """\
Exercice de Forensic : L’affaire du fichier mystérieux

Objectifs :
- Travailler à partir de faits
- Garder un esprit critique (sources humaines et techniques)
- Être méthodique et rigoureux
- Bien documenter ses démarches
- Savoir présenter ses conclusions

Consignes :
1. Analysez tous les documents fournis (logs, mails, capture réseau, etc.)
2. Listez uniquement les faits observables
3. Discutez de la fiabilité des sources
4. Relevez les incohérences ou informations manquantes
5. Rédigez un rapport structuré (faits, hypothèses, incertitudes, conclusion provisoire)
6. Présentez oralement votre analyse comme une équipe d’experts

Rappel : ne tirez pas de conclusions hâtives. Travaillez comme des analystes.
"""

with open(os.path.join(base_path, "06_Consignes", "consignes_exercice.txt"), "w") as f:
    f.write(instructions)

# Créons des fichiers supplémentaires pour enrichir l'exercice et le rendre plus long et plus complexe

# 07_Metas - Métadonnées de fichiers
metadata_content = """\
Fichier : clients_confidentiels.xlsx
Créé : 2025-06-19 22:41
Dernière modification : 2025-06-20 18:36
Auteur : mdubois
Chemin original : C:\\Users\\mdubois\\Documents\\clients_confidentiels.xlsx

Fichier : archive.zip
Créé : 2025-06-20 18:36
Dernière modification : 2025-06-20 18:36
Auteur : inconnu
Contient : fichiers.txt, note.txt
"""

# 08_Analyse_hash - Analyse de hachage (signature)
hashes_content = """\
Fichier : archive.zip
SHA256 : 3d4f2a3b5f1ce1ac0d6b982abf5f1271a6890abacd3e4df4a345f712a973dd8a
Correspondance dans base VirusTotal : OUI (flagged: 2/70 - possible steganographie)

Fichier : fichiers.txt (dans archive.zip)
SHA256 : 71f1d8b4b9a2c22e93050a44fda273a4a4dbdde5f8c640e37deba45a1b832aad
Aucune correspondance

Fichier : note.txt (dans archive.zip)
SHA256 : 9ae8ff58abf5beae9f0d7123467f620cb377f519cd44f20d5fd0d671a2aefc5e
Contenu : "Rendez-vous dans 2 semaines. Supprime tout."
"""

# 09_Tickets_IT - Historique des tickets IT
tickets_it = """\
[2025-06-18] Ticket #3249 – mdubois : demande d'accès temporaire au dossier partagé "Projets_Finaux"
[2025-06-19] Ticket #3251 – mdubois : signalement d’un problème d’envoi de mail chiffré
[2025-06-20] Ticket #3253 – IT : Suppression du compte utilisateur mdubois planifiée pour le 21/06 à 09:00
"""

# Création des dossiers supplémentaires
extra_folders = [
    "07_Metadonnees",
    "08_Analyse_hash",
    "09_Tickets_IT"
]

for folder in extra_folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Sauvegarde des fichiers supplémentaires
with open(os.path.join(base_path, "07_Metadonnees", "metadata_fichiers.txt"), "w") as f:
    f.write(metadata_content)

with open(os.path.join(base_path, "08_Analyse_hash", "analyse_hash.txt"), "w") as f:
    f.write(hashes_content)

with open(os.path.join(base_path, "09_Tickets_IT", "historique_tickets.txt"), "w") as f:
    f.write(tickets_it)

base_path
