from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Project
        fields = ('id' , 'Titulo' , 'Descripcion' , 'Tecnologia' , 'F_Creacion') 
        read_only_fields = ('F_Creacion',)