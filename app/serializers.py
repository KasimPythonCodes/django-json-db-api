from rest_framework import serializers 
from app.models import CustomUser
import re

class GetUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id' , 'name' ,'username' , 'mobile_no', 'email','address','password']
        
class CustomUserSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=250 ,style={'input_type':'password','placeholder':'password'},write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id' , 'name' ,'username' , 'mobile_no', 'email','address','password','confirm_password']
        
    def validate(self , attrs):
        username = attrs.get('username')   
        mobile_no = attrs.get('mobile_no') 
        email = attrs.get('email')
        password = attrs.get('password')   
        confirm_password = attrs.get('confirm_password') 
        Special_chr =['$', '@', '#', '%']
        regx=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(regx ,email)):
            pass
        else:
            raise serializers.ValidationError({"Email":"Enter a valid email address"})   
        if username.isalpha():
            pass
        else:
            raise serializers.ValidationError({"Username":"Only Alphabet Character Alloewd"})   
        if len(mobile_no)==10:
            pass 
        else:
            raise serializers.ValidationError({"Mobile Number ":"Only 10 digit number allowed"})
           
        if len(password) < 6 and len(confirm_password) <6:
            raise serializers.ValidationError({"Password & comfirm password":"length should be at least 6"})   
        if not any(char.isalnum() for char in password):
            raise serializers.ValidationError({"Password & comfirm password":"Password should have at least Alpha Numeric"})   
        if not any(char in Special_chr for char in password):
            raise serializers.ValidationError({"Password & comfirm password":"Password should have at least one of the symbols $@#"})   
           
        return attrs 
    
    
    
class LoginSerailizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        fields =['username' ,'password']