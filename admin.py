from django.contrib import admin
from .models import GongQu, CheJian, GongJuZhongLei,GongJu
from v1.admin import admin_site

admin_site.register(GongQu)
admin_site.register(CheJian)
admin_site.register(GongJuZhongLei)
admin_site.register(GongJu)
