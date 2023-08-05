from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from projects.models import Employee

class CustomUserCreateSerializer(UserCreateSerializer):
    # Add your custom fields here

    class Meta:
        model = Employee
        fields = ['id','legal_name','gid','english_name','email']



    # Meta is not needed when directly specifying fields in the serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        fields = ['legal_name', 'english_name',
                  'email', 'gid','grade','title','hire_date'] 