from django.contrib import admin
from .models import Photocard, Collection

# On enregistre tes modèles pour qu'ils apparaissent dans l'interface /admin
admin.site.register(Photocard)
admin.site.register(Collection)