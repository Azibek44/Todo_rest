from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email","phone_number","created_at","age")
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255,
        write_only = True
    )
    password2 = serializers.CharField(
        max_length = 255,
        write_only = True
    )
     
    class Meta:
         model = User
         fields = ("id","email","phone_number","created_at","age","password","password2")              
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError ({'password2': 'Пароли отличаются'})
        if '+996' not in attrs['phone_number']:      
            raise serializers.ValidationError('Номер телефона должен быть в формате +996XXXXXXXXX')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            age=validated_data['age'], 
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
                
    
    # def validate(self, attrs):
    #     if '+996' not in attrs['phone_number']:
    #         raise serializers.ValidationError('Номер телефона должен быть в формате +996XXXXXXXXX')   