#Django

```bash
pip install Django
```

```bash
django-admin startproject hellodjango .
python manage.py runserver
```

# Creer une application djamgo
Structure projet
o Pnﬂethellodjango
o hellodjango
o manage.py
0 App 1
0 App 2
o m

__Contenu application__
- apps . py => configuration de l’app pour le projet
- views . py => réponses HTTP
- models . py => modele de données / table BDD
- admin . py => configuration interface de gestion des modéles

__creer une premier application__
```bash
python manage.py startapp appone
```

__mettre dans settings.py__
'appone.apps.ApponeConfig',

__creer dans appone.views__
hello

__rajouter dans url.py__
path('hello/', views.hello),

lancer python manage.py runserver

### Exercice: Creer une application Django
__Nommée apptwo:__ 
```bash
python manage.py startapp apptwo
```


- Avec une route /dj angorocks/
- apptwo/views.py => djangorocks()
Affiche en réponse "This is a Jazzy Response”

# Exercice afﬁcher les donnees d‘unutilisateur
Outils
- Une app peoplebook

- 2 URLS
    - users/ => liste de tous les utilisateurs
    - users/<name>/detail/ => détail d’un utilisateur

- Un utilisateur
    - { Name, Job, Picture}
    - 'han’ : { ‘name’: "han solo”, ’job’: "Pilot", 'picture’: ”img/han jpg" }
    - Fichier peoples . py en ressource de la vidéo
    
    
- Outils
    - Un template base . html
    - Bloc title
    - Bloc content
    - Un template enfant use rs_list . html
    - Untemplateenfantusers_detail.html
    - Images d’utilisateurs => peoplebook/static/img/v’v . j pg
    - Feuille de style CSS => peoplebook/statiC/style . css    
    
- Bonus
    - Chaque nom de la liste est un hyperlien vers Ie détail
    - urls.py+tagurl
    - 3émeURL/users/fu11/
    - Liste avec Ie détail de Chaque utilisateur
    - taginclude
    - FichierHTMLcentralisantledétailblock_users_detail.html    
