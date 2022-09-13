from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O cpf não é valido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua numeros no nome"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve conter 9 numeros"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O celular deve ser do formato (11) 99999-9999"})
        return data
