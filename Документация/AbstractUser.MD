#### все это в папке `credo`

### models.py

```python
from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    fio = models.CharField('ФИО', max_length=255, default='')
```

### __init__.py

```python
default_app_config = 'credo.apps.CredoConfig'
```

### apps.py

```python
from django.apps import AppConfig


class CredoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'credo'
```

### settings.py

```python
INSTALLED_APPS = [
    'credo', # -Вот это
    'django_redis',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

AUTH_USER_MODEL = 'credo.CustomUser'
```

### forms.py

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
```

# После этого всего

- `sudo docker-compose exec web python manage.py makemigrations credo`
- `sudo docker-compose exec web python manage.py migrate credo`
- `sudo docker-compose exec web python manage.py migrate`

