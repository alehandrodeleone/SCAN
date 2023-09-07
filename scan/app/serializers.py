from rest_framework import serializers
from .models import *

class info_user_serializers(serializers.ModelSerializer):
    class Meta:
        model=info_user
        fields=["id","name_pc","version_windows","build_number","mac","ip","work_system_non_stop","processor","processor_work",
                "cores","name_videocard","memory_videocard","temperature_videocard","work_videocard","Mb_name","Mb_socket","Mb_Ram_memory",
                "Mb_Ram_mhz","Hdd"]
