from django.db import models



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
        verbose_name_plural = '车间'

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
        verbose_name_plural = '工区'

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
        verbose_name_plural = '工具种类'

    def __str__(self):
        return self.name


class GongJu(models.Model):

    gong_qu = models.ForeignKey(
        'GongQu',
        on_delete = models.CASCADE,
        related_name = 'gongqu_gongju',
        )

    gjzl  = models.ForeignKey(
        'GongJuZhongLei',
        on_delete = models.CASCADE,
        related_name = 'gjzl_gongju',
        )

    num = models.IntegerField(
        default = 1,
        )

    def No(self):
        return  '%s%s%s' % ( self.gong_qu.num, 
            self.gjzl.num,
            str(self.num),
            )

    class Meta:
        verbose_name = '工具'
        verbose_name_plural = '工具'

    def __str__(self):
        return  '%s %s%s%s%s' % ( 
            self.gjzl.name,
            self.gong_qu.che_jian.num,
            self.gong_qu.num, 
            self.gjzl.num,
            str(self.num),
            ) 

