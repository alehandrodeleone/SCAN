from django.db import models

class info_user(models.Model):#для упрощения было принято решение использовать везде charfield так как другие операции не были предусмотрены
    name_pc=models.CharField(max_length=200,null=True)
    version_windows=models.CharField(max_length=200, null=True)
    build_number=models.CharField(max_length=200, null=True)
    mac=models.CharField(max_length=200,null=True)
    ip=models.CharField(max_length=200,null=True)
    work_system_non_stop=models.CharField(max_length=200,null=True)
    processor=models.CharField(max_length=200,null=True)
    processor_work=models.CharField(max_length=200,null=True)
    cores=models.CharField(max_length=20,null=True)
    name_videocard=models.CharField(max_length=200,null=True)
    memory_videocard=models.CharField(max_length=200,null=True)
    temperature_videocard=models.CharField(max_length=20,null=True)
    work_videocard=models.CharField(max_length=200,null=True)
    Mb_name=models.CharField(max_length=200,null=True)
    Mb_socket=models.CharField(max_length=200,null=True)
    Mb_Ram_memory=models.CharField(max_length=200,null=True)
    Mb_Ram_mhz=models.CharField(max_length=200,null=True)
    Hdd=models.TextField()
