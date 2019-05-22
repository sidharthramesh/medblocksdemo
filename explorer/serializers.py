from rest_framework import serializers
from .models import MedBlock
class MedBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedBlock
        fields = ('data','file','createdBy','insuranceHasPermission', 'type')
        read_only_fields = ('hash', 'signature')
        fields += read_only_fields