from django.contrib import admin
from .models import GongQu, CheJian, GongJuZhongLei,GongJu,GongJuSet,Post
from v1.admin import admin_site
from searchadmin.admin import SelectModelAdmin
  

class GongJuAdmin(SelectModelAdmin):
    search_fields = ('gong_ju_set__gjzl__name','gong_ju_set__gong_qu__name','gong_ju_set__gong_qu__che_jian__name',)
    list_display = ('GongJu','CheJian','GongQu','no',)

    
admin_site.register(GongQu)
admin_site.register(CheJian)
admin_site.register(GongJuZhongLei)
admin_site.register(GongJu, GongJuAdmin)
admin_site.register(GongJuSet)
admin_site.register(Post)
