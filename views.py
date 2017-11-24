from django.shortcuts import render
from .models import CheJian, GongQu,GongJuZhongLei, GongJu,GongJuSet,Post
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@staff_member_required
def get_gongju_list(request, che_jian_num, gong_qu_num):
    try:
        gong_ju_list = GongJu.objects.filter(gong_ju_set__gong_qu__che_jian__num = che_jian_num).filter(gong_ju_set__gong_qu__num = gong_qu_num)
        context = {'gong_ju_list':gong_ju_list,}
        return render(request, 'tl/get-gongju-list.html', context)
    except:
        return HttpResponse("not exist")


def post(request, id):
    try:
        print('1231')
        lfb = Post.objects.get(id=id)
        print(lfb.feed_back)
        context = {'lfb':lfb,}
        print(context)
        return render(request, 'tl/post.html', context)
    except:
        return HttpResponse("not exist")
        
        


def get_gongju(request, no):
    try:
        
        gong_ju = GongJu.objects.get(no=no)
        lfb = Post() 
        if request.POST:
                lfb.gong_ju = gong_ju
                lfb.feed_back = request.POST['feed_back']
                lfb.contact = request.POST['contact']
                lfb.ip = get_client_ip(request) 
                lfb.date_time = datetime.now()
                lfb.is_show = True
                try:
                    if request.FILES['img']:
                        bucket = oss2.Bucket(oss2.Auth(settings.ACCESS_KEY_ID,
                            settings.ACCESS_KEY_SECRET), settings.ENDPOINT, settings.BUCKET_NAME)
                        myfile = request.FILES['img']
                        t0 = datetime(1, 1, 1)
                        now = datetime.now()
                        seconds = (now - t0).total_seconds()
                        new_name = qr_label.qrcode + str(seconds) + os.path.splitext(myfile.name)[1]
                        bucket.put_object(new_name, myfile)
                        lfb.upload_img_url = settings.IMGPREURL + new_name
                except:
                    pass
                lfb.save()
        print('ok')
        lfbs = Post.objects.filter(gong_ju = gong_ju).filter(is_show = True)
        print(lfbs) 
        context = {'gong_ju':gong_ju,'lfbs':lfbs,}
        return render(request, 'tl/get-gongju.html', context)
    except:
        return HttpResponse("not exist")
        
        

@staff_member_required
def rebuild(request, che_jian_num):
    try:
        #gjs =  GongJu.objects.filter(gong_ju_set__gong_qu__che_jian__num = che_jian_num)
        #if gjs:
        #    gjs.delete()
        gong_ju_set_list = GongJuSet.objects.filter(gong_qu__che_jian__num = che_jian_num)
        if gong_ju_set_list:
            for gong_ju_set in gong_ju_set_list:
                for i in range(1,gong_ju_set.count+1):
                    gj = GongJu(gong_ju_set = gong_ju_set,num=i)
                    gj.no = gj.NoSet()
                    tmpno = gj.NoSet()
                    gj.url = settings.GONGJUURLPRE+ gj.no + '/'
                    if GongJu.objects.filter(no = tmpno).exists():
                        print(gj.no)   
                    else:
                        gj.save()

        return HttpResponse("finished")
    except:
        return HttpResponse("not exist")
        

