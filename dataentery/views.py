from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import MtoMSerializer, ProfitLossSerializer
from .models import MtoM, ProfitLoss
# Create your views here.

class MtoMView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request):

        datamodel = MtoM.objects.filter(user = request.user).order_by("-created_at")

        serializer = MtoMSerializer(instance=datamodel, many = True)
        if serializer.data:
            
            return Response(serializer.data)
        else:
            return Response({"error":"No data"})
    
    def post(self, request):
        data = request.data
        try:
            ebitactual1 = data["ebitactual1"]
            ebitactual2 = data["ebitactual2"]
            ebitactual3 = data["ebitactual3"]
            ebitactual4 = data["ebitactual4"]
            ebitactual5 = data["ebitactual5"]
            ebitactual6 = data["ebitactual6"]
            ebitactual7 = data["ebitactual7"]
            ebitactual8 = data["ebitactual8"]
            ebitactual9 = data["ebitactual9"]
            ebitactual10 = data["ebitactual10"]
            ebitactual11 = data["ebitactual11"]
            ebitactual12 = data["ebitactual12"]

            ebittarget1 = data["ebittarget1"]
            ebittarget2 = data["ebittarget2"]
            ebittarget3 = data["ebittarget3"]
            ebittarget4 = data["ebittarget4"]
            ebittarget5 = data["ebittarget5"]
            ebittarget6 = data["ebittarget6"]
            ebittarget7 = data["ebittarget7"]
            ebittarget8 = data["ebittarget8"]
            ebittarget9 = data["ebittarget9"]
            ebittarget10 = data["ebittarget10"]
            ebittarget11 = data["ebittarget11"]
            ebittarget12 = data["ebittarget12"]

            demo = data["demo"]

            

            mtm = MtoM(user = request.user, ebitactual1 = ebitactual1,
                                            ebitactual2 = ebitactual2,
                                            ebitactual3 = ebitactual3,
                                            ebitactual4 = ebitactual4,
                                            ebitactual5 = ebitactual5,
                                            ebitactual6 = ebitactual6,
                                            ebitactual7 = ebitactual7,
                                            ebitactual8 = ebitactual8,
                                            ebitactual9 = ebitactual9,
                                            ebitactual10 = ebitactual10,
                                            ebitactual11 = ebitactual11,
                                            ebitactual12 = ebitactual12,

                                            ebittarget1 = ebittarget1,
                                            ebittarget2 = ebittarget2,
                                            ebittarget3 = ebittarget3,
                                            ebittarget4 = ebittarget4,
                                            ebittarget5 = ebittarget5,
                                            ebittarget6 = ebittarget6,
                                            ebittarget7 = ebittarget7,
                                            ebittarget8 = ebittarget8,
                                            ebittarget9 = ebittarget9,
                                            ebittarget10 = ebittarget10,
                                            ebittarget11 = ebittarget11,
                                            ebittarget12 = ebittarget12,
                                            demo = demo)
            mtm.save()
            return Response({"message":"Data created"})
        except:
            demo = data["demo"]
            mtm = MtoM(user = request.user, demo = demo)
            mtm.save()
            return Response({"message":"Demo data created"})



class ProfitLossView(APIView):
    def get(self, request):
        profitLoss = ProfitLoss.objects.filter(user = request.user).order_by("-created_at")
        serializer = ProfitLossSerializer(instance=profitLoss, many = True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({"error":"No data"})
    
    def post(self, request):
        data = request.data
        print(data)
        try:
            revenue = data['revenue']
            const_of_goods_sold = data['const_of_goods_sold']
            sales = data['sales']
            marketing = data['marketing']
            general_and_admin = data['general_and_admin']
            other_income = data['other_income']
            other_expenses = data['other_expenses']
            interest_and_tax = data['interest_and_tax']
            demo = data["demo"]
            profitloss = ProfitLoss(user = request.user,revenue = revenue, cost_of_good_sold = const_of_goods_sold, sales = sales, 
                                    marketing = marketing, general_and_admin = general_and_admin, other_income = other_income, other_expenses = other_expenses, interest_and_tax = interest_and_tax, demo= demo )
            
            profitloss.save()
            return Response({"message":"Data created"})
        except:
            demo = data["demo"]
            profitloss = ProfitLoss(user = request.user, demo = demo)
            profitloss.save()
            return Response({"message":"Demo data created"})


