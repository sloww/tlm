from django.db import models
from datetime import datetime


class CheJian(models.Model):

    name = models.CharField(
        blank = False,
        max_length = 200,
        verbose_name = '车间名称',
        unique = True,
    )

    num = models.CharField(
        blank = False,
        max_length = 200,
        verbose_name = '编号',
        unique = True,
        )
    class Meta:
        verbose_name = '车间'
        verbose_name_plural = '1.车间'

    def __str__(self):
        return self.name



class GongQu(models.Model):

    che_jian = models.ForeignKey(
        'CheJian',
        on_delete = models.CASCADE,
        )

    name = models.CharField(
        blank = False,
        max_length = 200,
        verbose_name = '工区名称',
        unique = True,
    )

    num = models.CharField(
        blank = False,
        max_length = 200,
        verbose_name = '编号',
        unique = True,
        )

    class Meta:
        verbose_name = '工区'
        verbose_name_plural = '2.工区'

    def __str__(self):
        return self.name


class GongJuZhongLei(models.Model):

    name = models.CharField(
        blank = False,
        max_length = 200,
        verbose_name = '工具名称',
        unique = True,
    )

    num = models.CharField(
        blank = False,
        max_length = 200,
        verbose_name = '编号',
        unique = True,
        )

    class Meta:
        verbose_name = '工具种类'
        verbose_name_plural = '3.工具种类'

    def __str__(self):
        return self.name


class GongJuSet(models.Model):

    gong_qu = models.ForeignKey(
        'GongQu',
        on_delete = models.CASCADE,
        related_name = 'gongqu_gongju',
        verbose_name = '工区',
        )

    gjzl  = models.ForeignKey(
        'GongJuZhongLei',
        on_delete = models.CASCADE,
        related_name = 'gjzl_gongju',
        verbose_name = '工具类型',
        )

    count = models.IntegerField(
        default = 1,
        verbose_name = '数量',
        )
    
    has_print = models.BooleanField(
        default = True,
        verbose_name = '是否已打印',
        )

    class Meta:
        verbose_name = '工区工具'
        verbose_name_plural = '4.工区工具'

    def __str__(self):
        return  '%s %s %s %s%s%s * %s' % ( 
            self.gong_qu.che_jian.name,
            self.gong_qu.name,
            self.gjzl.name,
            self.gong_qu.che_jian.num,
            self.gong_qu.num, 
            self.gjzl.num.upper(),
            self.count,
            ) 


class GongJu(models.Model):

    gong_ju_set = models.ForeignKey(
        'GongJuSet',
        on_delete = models.CASCADE,
        related_name = 'gongjuset_gongju',
        verbose_name = '工区工具',
        )

    num = models.IntegerField(
        default = 1,
        verbose_name = '序号',
        )

    url = models.CharField(
        max_length = 200,
        default = '',
        verbose_name = '查询地址',
        )

    no = models.CharField(
        max_length = 200,
        default = '',
        verbose_name = '唯一编号',
        unique = True,
        )
    
    
    has_print = models.BooleanField(
        default = True,
        verbose_name = '是否已打印',
        )

    def CheJian(self):
        return self.gong_ju_set.gong_qu.che_jian.name

    def GongQu(self):
        return self.gong_ju_set.gong_qu.name

    def GongJu(self):
        return self.gong_ju_set.gjzl.name

    def NoSet(self):
        return '%s%s%s%s' % (
            self.gong_ju_set.gong_qu.che_jian.num,
            self.gong_ju_set.gong_qu.num, 
            self.gong_ju_set.gjzl.num.upper(),
            '%02d' % self.num,
            )

    class Meta:
        verbose_name = '工具'
        verbose_name_plural = '5.工具'

    def __str__(self):
        return  '%s No.%s' % ( 
            self.gong_ju_set,
            '%02d' % self.num,
            ) 

class Post(models.Model):
    
    gong_ju = models.ForeignKey(
        'GongJu',
        on_delete = models.CASCADE,
        related_name = 'gongju_post',
        )  

    feed_back = models.TextField(
        verbose_name = '反馈',
        blank = True,
        )

    contact = models.CharField(
        verbose_name = '反馈',
        max_length = 200,
        blank = True,
        )

    upload_img_url = models.URLField(
        verbose_name = '图片',
        )

    is_show = models.BooleanField(
        verbose_name = '是否显示',
        default = True,
        )

    date_time = models.DateTimeField(
        verbose_name = '时间',
        default=datetime.now(),
        blank=True
        )


    ip = models.GenericIPAddressField(
        verbose_name = 'IP',
        default = '0.0.0.0',
        )

    class Meta:
        verbose_name = '反馈'
        verbose_name_plural = '6.反馈'

    def __str__(self):
        return  '{} {}'.format( 
            self.ip,
            self.date_time,
            ) 


