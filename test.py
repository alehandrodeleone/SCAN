# import socket

# def get_my_ip():
#     try:
#         # Создаем сокет
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#         # Устанавливаем подключение с публичным DNS-сервером (например, Google DNS)
#         s.connect(("8.8.8.8", 80))

#         # Получаем информацию об адресе сокета
#         ip_address = s.getsockname()[0]

#         # Закрываем сокет
#         s.close()

#         return ip_address

#     except socket.error:
#         return "Не удалось получить IP-адрес"

# my_ip = get_my_ip()
# print("Мой IP-адрес:", my_ip)

# import cpuinfo

# def get_motherboard_info():
#     info = cpuinfo.get_cpu_info()
#     motherboard_socket = info['hardware_raw']
#     motherboard_ram_slots = info['physical_processors']
#     motherboard_name = info['brand_raw']
    
#     return motherboard_socket, motherboard_ram_slots, motherboard_name

# socket, ram_slots, name = get_motherboard_info()
# print("Сокет материнской платы:", socket)
# print("Количество разъемов для оперативной памяти:", ram_slots)
# print("Название материнской платы:", name)


# import wmi

# # Создаем объект WMI
# c = wmi.WMI()

# # Получаем информацию о материнской плате
# motherboard = c.Win32_BaseBoard()[0]
# motherboard_name = motherboard.Product
# print("Название материнской платы:", motherboard_name)


# import wmi

# def get_memory_slots():
#     c = wmi.WMI()
#     memory_slots = 0
    
#     # Получение количества слотов памяти
#     for slot in c.Win32_PhysicalMemoryArray():
#         memory_slots = slot.MemoryDevices
    
#     # Получение информации о каждом слоте памяти
#     for slot in c.Win32_PhysicalMemory():
#         slot_number = slot.DeviceLocator
#         memory_type = slot.MemoryType
#         memory_speed = slot.ConfiguredClockSpeed
        
#         print(f"Слот {slot_number}: Тип памяти - {memory_type}, Частота - {memory_speed} МГц")
    
#     return memory_slots

# memory_slots = get_memory_slots()
# print(f"Количество слотов памяти: {memory_slots}")

# import psutil

# def get_hard_disks():
#     hard_disks = []
#     partitions = psutil.disk_partitions()

#     for partition in partitions:
#         if 'cdrom' in partition.opts or partition.fstype == '':
#             continue

#         disk_usage = psutil.disk_usage(partition.mountpoint)
#         disk_info = {
#             'brand': partition.device,
#             'volume': disk_usage.total / (1024**3)  # преобразуем в гигабайты
#         }
#         hard_disks.append(disk_info)

#     return hard_disks

# hard_disks = get_hard_disks()
# for disk in hard_disks:
#     print('Brand:', disk['brand'])
#     print('Volume:', round(disk['volume']), 'GB')
#     print('---')


# import uuid

# def get_mac_address():
#     mac = uuid.getnode()# получаем мак адрес
#     mac_address = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))# преобразуем в стандартный вид отображения мак адресов
#     return mac_address

# mac_address = get_mac_address()
# print("MAC-адрес компьютера:", mac_address)

import getpass

username = getpass.getuser()
print("Имя пользователя компьютера:", username)


import platform

# Версия Windows
version = platform.win32_ver()[0]
print("Версия Windows:", version)



# Сборка Windows
build_number = platform.win32_ver()[1]
print("Сборка Windows:", build_number)


