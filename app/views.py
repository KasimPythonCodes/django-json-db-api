from django.shortcuts import render
from app.models import CustomUser
from app.serializers import CustomUserSerializers ,LoginSerailizer,GetUserSerializers
from django.contrib.auth.hashers import make_password ,check_password
from rest_framework import serializers , status , response ,generics
from django.http import JsonResponse
# Create your views here.

class  CustomUserRegisterAPI(generics.GenericAPIView):
    serializer_class = CustomUserSerializers
    queryset = CustomUser.objects.all()
    def post(self,request):
        serializer = self.serializer_class(data =request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.data.get('name')
        username = serializer.data.get('username')
        mobile_no = serializer.data.get('mobile_no')
        email = serializer.data.get('email')
        address = serializer.data.get('address')
        password = serializer.data.get('password')
        obj_create=CustomUser.objects.create(username=username ,name=name,mobile_no=mobile_no,email=email,password=make_password(password),address=address)
        res=response.Response(serializer.data)
        for k,v in res.items():
            setattr(obj_create,k,v)
            obj_create.save()
        return response.Response({'msg':'user register successfully'},status=status.HTTP_200_OK)    
        
    
    
class CustomUserLoginSerializer(generics.GenericAPIView):
    serializer_class =LoginSerailizer
    queryset = CustomUser.objects.all()
    def post(self ,request):
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user =CustomUser.objects.filter(username=username).first()
            if user== None:
                raise serializers.ValidationError("This username not regiter in database!")
            flag = check_password(password , user.password)
            if flag:
                if user is not None:
                    context ={
                        'username':user.username ,
                        'Name':user.name ,
                        'Mobile Number':user.mobile_no,
                        'Email':user.email ,
                        'Address':user.address
                    }
                    return response.Response({'User Details':context},status=status.HTTP_200_OK)
                else:
                    return response.Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
            else:
                return response.Response({"msg":"username and password doen't match"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JsonViewAllUserSerializerAPI(generics.GenericAPIView):
    serializer_class =GetUserSerializers
    queryset = CustomUser.objects.all()
    def get(self , request):
        userdata = list(CustomUser.objects.values())
        serializer = self.serializer_class(userdata ,many=True)
        
        return JsonResponse(serializer.data ,safe=False)
    