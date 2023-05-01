from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .serialiser import *

@api_view()
def hello_world(request):
    return Response({"message":"Hello, World"})

@api_view(['GET', 'POST'])
def hello(request):
    if request.method == "GET":
        return Response({"message":"Hello, World"})
    if request.method == "POST":
        return Response({"message":"Hello, {}".format(request.data["name"])})

# @api_view(['POST'])
# def calculator(request):
#     try:
#         num1 = request.data["num1"]
#         num2 = request.data["num2"]
#         opr = request.data["opr"]
#     except:
#         return Response({"error":"Bad Value"}, status=status.HTTP_400_BAD_REQUEST )
#     else:
#         if isinstance(num1, int) and isinstance(num2, int):
#             match opr:
#                 case "add":
#                     return Response({"result":num1+num2},
#                                 status=status.HTTP_200_OK)
#                 case "sub":
#                     return Response({"result":num1 - num2},
#                                     status=status.HTTP_200_OK)
#                 case _:
#                     return Response({"error":"Operator Not Supported"},
#                                     status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#         else:
#             return Response({"error" : "invalid integer input"},
#                             status =  status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def calculator(request):
    ser = CalcSerialiser(data=request.data)
    
    if ser.is_valid():
        num1 = ser.data["num1"]
        num2 = ser.data["num2"]
        opr = ser.data["opr"]
        match opr:
                case "add":
                    return Response({"result":num1+num2},
                                status=status.HTTP_200_OK)
                case "sub":
                    return Response({"result":num1 - num2},
                                    status=status.HTTP_200_OK)
                case _:
                    return Response({"error":"Operator Not Supported"},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
        return Response({"error" : "invalid integer input"},
                            status =  status.HTTP_400_BAD_REQUEST)