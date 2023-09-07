
from django.shortcuts import render
import datetime
import psutil
import GPUtil
import  platform
import cpuinfo
import socket
import wmi
import pythoncom
import uuid
import getpass
from .models import info_user



def start_page(request):
    return render (request,"start_page.html")


def scan_page(request):
    pythoncom.CoInitialize()# инициализация потока wmi для работы в джанго

    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute

    time_sys = datetime.datetime.fromtimestamp(psutil.boot_time())
    runtime = time - time_sys
    #processor = platform.processor()#получаем название процессора
    cpu_percent = psutil.cpu_percent()# получить загруженность
    cpu_count = psutil.cpu_count()#получить кол-во ядер
    cpu_name=cpuinfo.get_cpu_info()['brand_raw']#получаем название процессора
    gpus = GPUtil.getGPUs()
    c = wmi.WMI()

    for i in gpus:#проходимся по всем полученным данным и передаем их в переменную для сохранения
        name=i.name
        memory_card=i.memoryTotal
        temperature=i.temperature
        load_gpu=i.load 
        
    # Получаем информацию о материнской плате
    motherboard = c.Win32_BaseBoard()[0]
    motherboard_name = motherboard.Product#название мат платы
    processor = c.Win32_Processor()[0]
    socket_name = processor.SocketDesignation# получаем название сокета
    
    memory_slots = []
    for slot in c.Win32_PhysicalMemory():
        slot_number = slot.DeviceLocator
        memory_type = slot.MemoryType
        memory_speed = slot.ConfiguredClockSpeed

        memory_slots.append({
            'slot_number': slot_number,
            'memory_type': memory_type,
            'memory_speed': memory_speed
        })
    for memory in c.Win32_PhysicalMemory():
        memory= memory.Capacity
        
    for mhz in memory_slots:# проходимся по списку что бы получить mhz оперативной памяти
        mhz=memory_speed

# получаем обьем оперативки
    mem_info = psutil.virtual_memory()
    total_ram = mem_info.total
    total_ram_gb=total_ram/(1024**3)# преобразовываем в гигабайты

    # функция получения инфы о жд
    def get_hard_disks():
        hard_disks = []
        partitions = psutil.disk_partitions()
    
        for partition in partitions:
            if 'cdrom' in partition.opts or partition.fstype == '':
                continue
    
            disk_usage = psutil.disk_usage(partition.mountpoint)
            disk_info = {
                'disk': partition.device,
                'memory': round(disk_usage.total / (1024**3))  # преобразуем в гигабайты
            }
            hard_disks.append(disk_info)
    
        return hard_disks    
    hard_disks = get_hard_disks()

# получение ip адреса пользователя
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

# получаем информацию о windows
    username = getpass.getuser()#имя компьютера
    version = platform.win32_ver()[0]#Версия
    build_number = platform.win32_ver()[1]# сборка

    save_info_user=info_user(name_pc=username,processor=cpu_name,processor_work=cpu_percent,
                             cores=cpu_count, name_videocard=name,work_videocard=load_gpu,
                             temperature_videocard=temperature,memory_videocard=memory_card,Mb_name=motherboard_name,
                             Mb_socket=socket_name,Mb_Ram_memory=total_ram_gb,Mb_Ram_mhz=mhz,
                             version_windows=version,build_number=build_number,mac=mac_address,
                             ip=ip_address,work_system_non_stop=runtime,Hdd=hard_disks)
    save_info_user.save()

    context = {
        "hour": hour,
        "minute": minute,
        "runtime":runtime,
        "cpu_info":cpu_percent,
        "cpu_info2":cpu_count,
        "gpus":gpus,
        "cpu_info3":cpu_name,
        "cpu_info4":processor,
        "ip":ip_address,
        "name_mb":motherboard_name,
        "socket_mb":socket_name,
        'memory_slots': memory_slots,
        'slots_count': len(memory_slots),
        "memory":round(total_ram_gb),#roundокругляем до целых чисел
        "hard_disk":hard_disks,
        "mac_address":mac_address
    }
    return render(request,"home.html",context)

from  rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import info_user_serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 4  # Количество элементов на страницу
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества элементов на страницу
    max_page_size = 100

class info_users(ListAPIView):
    queryset = info_user.objects.all()
    serializer_class =info_user_serializers
    filterset_fields = ['id', "mac", "ip"]
    pagination_class = CustomPagination

class info_users_id(RetrieveAPIView):
    queryset = info_user.objects.all()
    serializer_class = info_user_serializers
    
class info_users_viewset(ModelViewSet):
    queryset = info_user.objects.all()
    serializer_class = info_user_serializers
    pagination_class = CustomPagination
