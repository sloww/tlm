from django.shortcuts import render
from .models import CheJian, GongQu,GongJuZhongLei, GongJu,GongJuSet
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.conf import settings


@staff_member_required
def get_gongju_list(request, che_jian_num, gong_qu_num):
    try:
        gong_ju_list = GongJu.objects.filter(gong_ju_set__gong_qu__che_jian__num = che_jian_num).filter(gong_ju_set__gong_qu__num = gong_qu_num)
        context = {'gong_ju_list':gong_ju_list,}
        return render(request, 'tl/get-gongju-list.html', context)
    except:
        return HttpResponse("not exist")

def get_gongju(request, no):
    try:
        gong_ju = GongJu.objects.get(no=no)
        context = {'gong_ju':gong_ju,}
        return render(request, 'tl/get-gongju.html', context)
    except:
        return HttpResponse("not exist")
        
        

@staff_member_required
def rebuild(request, che_jian_num):
    try:
        gjs =  GongJu.objects.filter(gong_ju_set__gong_qu__che_jian__num = che_jian_num)
        if gjs:
            gjs.delete()
        gong_ju_set_list = GongJuSet.objects.filter(gong_qu__che_jian__num = che_jian_num)
        if gong_ju_set_list:
            for gong_ju_set in gong_ju_set_list:
                for i in range(1,gong_ju_set.count+1):
                    gj = GongJu(gong_ju_set = gong_ju_set,num=i)
                    gj.no = gj.NoSet()
                    gj.url = settings.GONGJUURLPRE+ gj.no + '/'
                    gj.save()

        return HttpResponse("finished")
    except:
        return HttpResponse("not exist")
        

