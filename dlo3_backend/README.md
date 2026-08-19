# Back-end Django — DLO3

Ce projet fait tourner dynamiquement les pages du site (Accueil, À propos,
Paroisses, Activités, Galerie, Contact) à partir d'une vraie base de données,
avec une interface d'administration pour tout gérer sans toucher au code.

## Installation (première fois)

```bash
python -m venv venv
venv\Scripts\activate          # sous Windows
# source venv/bin/activate     # sous Mac/Linux

pip install -r requirements.txt

python manage.py migrate
python manage.py charger_donnees_initiales   # recharge tes 23 communautés + 4 activités
python manage.py createsuperuser             # crée TON compte admin (recommandé plutôt que celui de test)
```

Un compte de test existe déjà dans `db.sqlite3` fourni :
**identifiant `admin` / mot de passe `dlo3admin2026`** — change-le ou crée le tien avec
`createsuperuser` avant de mettre le site en ligne.

## Lancer le site en local

```bash
python manage.py runserver
```

Puis ouvre :
- **http://127.0.0.1:8000/** — le site
- **http://127.0.0.1:8000/admin/** — l'interface de gestion (paroisses, activités,
  photos, messages de contact, candidatures)

## Fichiers à copier toi-même

Le dossier `static/` contient déjà `navbar.css`, `navbar.js`, `Accueil.css`,
`Apropos.css`, `paroisses.css`, `Activites.css`, `Galerie.css`, `formulaires.css`.

**Il te manque encore** dans ce dossier `static/` :
- `logo.jpeg` (le logo du DLO3)
- `join.jpg` (l'icône du bouton "Faire un don")

Copie-les depuis ton projet front-end existant.

## Ce qui est géré depuis l'admin (sans toucher au code)

- **Communautés** (paroisses, quasi-paroisses, stations, sanctuaire) : nom, curé/recteur,
  responsable de base, localisation, coordonnées GPS.
- **Activités** : icône, titre, accroche, description, fichier PDF/Word.
- **Photos** : upload direct depuis l'admin, avec catégorie et légende.
- **Messages de contact** : chaque message envoyé depuis le formulaire /contact/
  apparaît dans l'admin, avec une case "traité" à cocher une fois répondu.
- **Candidatures** ("Rejoindre les servants") : le modèle et la vue existent
  (`/rejoindre/`) mais ne sont plus liés depuis la navbar, remplacés par le bouton
  "Faire un don" — dis-moi si tu veux qu'on la relie à une page, ou qu'on la retire.

## Pages qui restent à construire côté back-end

- **Faire un don** : le bouton pointe vers `#` pour l'instant, comme sur le site
  statique — pas encore de page ni de logique derrière.
- **Actualités** : pas encore de modèle ni de vue Django (existe seulement en
  statique pour l'instant).

## Ce qu'il reste à faire avant une mise en ligne réelle

- Changer `SECRET_KEY` dans `dlo3_backend/settings.py` (actuellement la valeur
  générée par défaut, à ne jamais garder en production).
- Mettre `DEBUG = False` et renseigner `ALLOWED_HOSTS` avec ton vrai nom de domaine.
- Remplacer SQLite par une vraie base (MySQL, que tu connais déjà) si tu veux plus
  de robustesse — Django rend ce changement simple, juste `DATABASES` à modifier.
- Configurer un vrai serveur d'envoi d'e-mails si tu veux recevoir une notification
  à chaque nouveau message de contact (actuellement juste enregistré en base).
