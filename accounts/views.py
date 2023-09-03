from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UserPaymentInfoSerailizer
from .models import UserPaymentInfo
from django.shortcuts import get_object_or_404
from rest_framework import status

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)

                    user.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})
        

class UserPaymentInfoView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request):
        userpaymentinfo = get_object_or_404(UserPaymentInfo, user = self.request.user)
        serializer = UserPaymentInfoSerailizer(instance=userpaymentinfo, many = False)
        return Response(serializer.data)

    def post(self, request):
        try:
            data = request.data
            payed_ceo = data["payed_ceo"]
            payed_cto = data["payed_cto"]
            userpaymentinfo = UserPaymentInfo.objects.get(user = self.request.user)

            if payed_ceo is not None:
                userpaymentinfo.payed_ceo = payed_ceo
            if payed_cto is not None:
                userpaymentinfo.payed_cto = payed_cto
            userpaymentinfo.save()
            return Response({"message":"updated"})
            
            
            
        except UserPaymentInfo.DoesNotExist:
            data = request.data
            payed_ceo = data["payed_ceo"]
            payed_cto = data["payed_cto"]
            userpaymentinfo = UserPaymentInfo(user = self.request.user, payed_ceo = payed_ceo,  payed_cto = payed_cto )
            userpaymentinfo.save()
            return Response({"message":"created"})
        

        


            
            
        

