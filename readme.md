# Django

## Instalace
```python
python -m pip install django==4.1.1
```

## Vytvoreni Django projektu
```python
django-admin startproject hollymovies .
```

## Spusteni serveru (defaultne na portu 8000)
```python
python manage.py runserver
```

## port muzeme zmenit parametrem:
```python
python manage.py runserver 8001
```


## Vytvoreni aplikace

viewer = nazev aplikace
```python
python manage.py startapp viewer
```
Vznikla nova slozka "Viewer", ktera obsahuje:
    - slozka migrations (obsahuje migracni skripty, lepsi neupravovat)
    - slozka admin.py - zde budeme registrovat modely, ktere chceme zobrazit
                       v administracni casti projektu
    - apps.py - nastaveni aplikace (neni treba menit)
    - tests.py - zde uvadime testy
    - views.py - zde bude naprogramovana funkcionalita aplikace


## Registrace aplikace do Djanga

V souboru /hollymovies/settings.py pridame aplikaci "viewer" do listu "INSTALLED_APPS"



## Zobrazovani obsahu
do views.py pridam funkci --> do urls.py pridam cestu --> spustim server


## Vytvoreni migracniho skriptu
```python
python manage.py makemigrations
```

## Provedeme zmeny v databazi
```python
python manage.py migrate
```

## Shell
```python
python manage.py shell
```
Nejdriv import modelu:
from viewer.models import Genre
zde mohu zobrazovat a pridavat veci do databaze.
    Zobrazeni:
        Vse:        
            Query.objects.all()
        Neco:
            horror = Genre.objects.get(name='Horror')   ##horror je akorat promenna, do ktere ukladam vysledek
            print(horror)  

    Pridani:
        Option 1: 
        Genre.objects.create(name="Horrors")
        Option 2:
        genre = Genre(name="Thriller")
        genre.save()
 

## Vytvoreni administratora
```python
python manage.py createsuperuser
```
Pak prejdu do souboru "admin.py" a zaregistuju classy


## Export databaze
```python
python manage.py dumpdata viewer --output fixtures.json
```

## Import databaze
```python
python manage.py loaddata fixtures.json
```
Nefunguje s diakritikou. Pokud chceme diakritiku, nainstalujeme rozsireni:
```bash
pip install django-dump-load_utf8
```
+ je potreba pridat radek do settings.py, sekce INSTALLED_APPS: 'django_dump_load_utf8'
Pak muzu exportovat pomoci rozsireni:
    python manage.py dumpdatautf8 viewer --output fixtures.json

## Filtrovani v shellu (nesmim zapomenout naimportovat classy)
Movie.objects.filter(released__year=1994)
Movie.objects.filter(rating__lt=90)
## Count
Movie.objects.filter(title="Harry Potter").count()
## Order by
Movie.objects.filter(title_contains="Harry Potter).order_by('released')   #od nejstarsiho
Movie.objects.filter(title_contains="Harry Potter).order_by('-released')  #od nejnovejsiho
## Data manipulation - Update
Movie.objects.filter(released__year=2000).update(rating=5)   #sets movie ratings from year 2000 to 5
    To save data
pulp_fiction = Movie.objects.get(title='Pulp Fiction')
pulp_fiction.rating = 7
pulp.fiction.save()
## Delete
Movie.objects.filter(title_contains="Harry Potter).delete()


##Add another
https://django-addanother.readthedocs.io/en/latest/

pip install django_addanother

Do settings.py vložit do INSTALLED_APPS: 'django_addanother',

Do views.pyv do formuláře do podtřídy Meta` přidáme widget:

widgets = {
            'directors': AddAnotherWidgetWrapper(
                SelectMultiple,
                reverse_lazy('creator_create')
            )
        }
Do template form_movie.html přidáme: {% load static %}

a do formuláře:

<script src="{% static 'admin/js/vendor/jquery/jquery.js' %}"></script>
{{ form.media }}
Do view PeopleCreateView(CreatePopupMixin, CreateView): přidáme CreatePopupMixin

Do šablony base.html přidáme:

{% if not view.is_popup %}
...
{% endif %}


## Zakladni struktura projektu (hollymovies)
    -settings.py - zde je veskere nastaveni projektu
    -urls.py - zde jsou uvedeny url adresy, na ktere 
               budou navazane funkce

## Rady a tipy pro finalni projekt

-vytvorit readme.md soubor s popisem projektu, muze obsahovat
i obrazky (ER diagram), screenshoty,...)
-vytvorit git repozitar a sdilet v tymu (settings -> collaborators)
