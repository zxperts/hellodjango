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


## Découvrir Django
### Découvrir les templates

fichier template dans lequel on ecrit le code html et du dtl
- Injection fait coté view

- Config par defaut setting.py
TEMPLATES
modeut de templaples Jinja2
Dirs : listes deds dossier pour fichier templates
Apps_dire : les dossiers templates à l'interirus des apps si true

template.apptwo > fichier i   
index.html

```html
<!DOCTYPE htm1>
<htm1 lang="en">
<head>
<meta charset="UTF-8">
<tit1e>Index AppTwo</tit1e>
</head>
<body>
<h1>This is AppTwo</h1>
<div sty1e="background: #ff0000;">Lorem ipsum texﬂ</div>
</body>
</html>
```

views.py
```python
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def djangorocks(request):
  return HttpResponse("This is a Jazzy Response")

def picture_detail(request, category, year=0, month=0, dayze):
  template = loader.get_template('apptwo/index.html')
  return HttpResponse(template.render({}, request))
```

utiliser en l'associantion à une vue
views.py

### Assigner des variables à un template

views.py
```python
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def djangorocks(request):
return HttpResponse("This is a Jazzy Response")
def picture_detail(request, category, year=0, month=0, day=0):
template = loader.get_template('apptwo/index.html')
picture = {
'filename': 'mountain.jpg',
'categories': ['color', 'landscape', ],
}
context = {
'title‘: 'This is the picture detail',
'category': category,
'year': year,
'month': month,
'day': day,
2 'picture': picture,
}
return HttpResponse(template.render(context, request))
```

index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Index AppTwo</title>
</head>
<body>
{# Title block here #}
<!-- HTML comment -->
<h1>{{ title }}</h1>
{% comment "This is a commented block. Not visible in the generated HTML" %}
<h2>Test title</h2>
{% endcomment %}
<div>
Category: {{ category }} <br/>
Year: {{ year }} <br/>
Month: {{ month }} <br/>
Day: {{ day }} <br/>
</div>
<h2>Access variable detail</h2>
<div>
filename : {{ picture.filename }} <br/>
first category : {{ picture.categories.q }} <br/>
</div>
</body>
</html>
```


### Tags et filtres dans template


Tags

Controler la logique du template
- {% comment "bla" %} m {% endcomment %}
- {% if condition %} m {% endif %}
- {% for . .. °/o} {% endfor %}

Pourquoi cette syntaxe plutét que du XML ?
- <my-tag>...</my—tag>
- Langage plus généraliste : template d’emails, JavaScript,


Filters
- Modifier une variable avant son affichage
- {{ namellength %}
- {{ nameldefault:"Empty" %}
- {{ name|lower|truncatewords 5 %}

Tag if
```html
{{ descriptionlsafelstriptags }}
<div>
Category: {{ category }} <br/>
Year: {{ year }} <br/>
Month: {{ month }} <br/>
Day: {{ day }} <br/>
</div>
<h2>Access variable detail</h2>
<div>
filename : {{ picture.filename }} <br/>
All categories :
‘g {% for category in picture.categories %}
{{ category }}
{% endfor %}
</div>
{% if day == 1-%}
<h3>Special day!</h3>
{% elif day == 3-%}
<h3>Publish at the end of the month<lh3>
{% else %}
<h4>Nothinq fancv</h4>
```

Tag for
```html
<div>
  filename : {{ picture.filename }} <br/>
  All categories :
  {% for category in picture.categories %}
  {{ category }}
  {% endfor %}
  All categories with filter : {{ picture.categoriesljoin:', ' }}
</div>
```

Tag Cycle
```html
<table>
<tr style="background-color: {% cycle '#80e27e' '#087f23' as rowcolors %}">
<td>Resolution</td>
<td>1920x1080</td>
</tr>
<tr style="background-color: {% cycle rowcolors %}">
<td>Location</td>
<td>Tokyo</td>
</tr>
<tr style="background-color: {% Eycle rowcolors %}">
<td>Location</td>
<td>Tokyo</td>
</tr>
</table>
```

###  Templates et héritage


v unencujango ~/pr0Jec15/nenoc1jango
> m appone
v :1 apptwo
b [:3 mlgratlons
v Eatemplates
v L:- apptwo
basehtml
lndexhtml

base.HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{% block title %}My Django site{% endblock %}</title>
</head>
<body>
<div id="content">
{% block content %H
</div>
</body>
</html>
```


index.html
```HTML
{% extends “apptwo/base.html" %}
{% block title %}Pictures{% endblock %}
{% block content %}
This is the pictures page!
{{ block.super }}
{% endblock content %}
```


### Ressources statiques dans un template

Fichiers “statiques” stockés sur le serveur
- JavaScript
- CSS
- Images
Fournis au client sans modification
Accessibles depuis Ies templates

Inline-style: ![alt text](static.JPG)


style.CSS

```CSS
.picture h2 {
font-size: 24px

}

.picture img {
width: 300px;

}
```

views.py
```python
from django shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def djangorocks(request):
return HttpResponse("This is a Jazzy Response")
def picture_detail(request, category, year=0, month=0, day=0)
template = loader.get_template('apptwo/index.html')
context = {
'pictures': [
      {
      'name': 'Duck',
      'filename': 'duck.jpg',
      }.
      {
      'name': 'Hountain',
      'filename': 'mountain.jpg',
      }.
      {
      , 'name': 'Building',
      ‘2 'filename': 'bmilding.jpg',
      }.
      1.
      }
return HttpResponse(template.render(context, request))
```

index.html
```HTML
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index AppTwo</title>
    <link rel="stylesheet" href="{% static 'apptwo/css/style.css' %}" type="text/css" media="screen">
</head>
<body>
{% for picture in pictures %}
    {% with 'apptwol'|add:picture.filename as filepath %}
    <h2>{{ picture.name }}</h2>
    <img src="{% static filepath %}" />
    {% endwith %}
{% endfor %}
</body>
</html>
```

setting.py
```python
import os
#gBuild paths inside the project like this: os.path.join(BASElDIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATIC_URL = ’/static/'
STATICFILES_DIRS = [s.path.join(BASElDIR, 'static'),]

```

setting.py
```python
```


### Exercice : afficher les données d'un utilisateur

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
    
    
#### Exercice : créer un modèle, ajouter en db et l'affichage  

```cmd
python manage.py makemigration
python manage.py migrate
````
