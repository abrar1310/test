from rest_framework.decorators import( 
    api_view,
    # renderer_classes,
    # parser_classes
    )
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.renderers import( 
#     JSONRenderer,
#     BrowsableAPIRenderer
#     )
# from rest_framework.parsers import JSONParser
# from rest_framework_xml.renderers import XMLRenderer # لازم نروح ع موقع ال rest framework  ونفوت ع قسم renderers  ونشوف صيغة xml  لأنو إلها مستلزمات للتنزيل 
# from rest_framework.parsers import XMLParser ما مشي حالها لأنو ما بتدعم البارسر لهيك استخدمنا اللي تحتا 
# from rest_framework_xml.parsers import XMLParser
from ..models import Car
from ..models import Brand
from ..serializers import CarModelSerializer, CarSerializer
from ..serializers import BrandModelSerializer


@api_view(['GET'])
# @renderer_classes([BrowsableAPIRenderer,JSONRenderer,XMLRenderer])
def index(request):
    # print(request.data)
    # data = {
    #     "name" : "abrar",
    #     "age"  : 24,
    #     "method": request.method,
    #     "data" : request.data,
    #     "headers": request.headers
    # }

    cars= Car.objects.all()
    # print(cars.query)
    # serializer= CarModelSerializer(cars, many=True)
    serializer= CarSerializer(cars, many=True)

    # data = []
    # for car in cars:
    #     data.append({
    #         "id" : car.id,
    #         "status": car.status,
    #         "price" :car.price,
    #         "quantity": car.quantity,
    #         # "brand": car.brand
    #     })
    return Response(serializer.data,
                    status= status.HTTP_201_CREATED,
                    )


@api_view(['GET'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer, XMLRenderer])
def getById(request, id):
    # print("abrar I am here")
    try:
        cars = Car.objects.get(pk= id)
        serializer= CarModelSerializer(cars)
        # data= {
        # "id" : cars.id,
        #     "status": cars.status,
        #     "price" :cars.price,
        #     "quantity": cars.quantity
        # }

        return Response(
        serializer.data, status = status.HTTP_202_ACCEPTED
        )
    except Car.DoesNotExist:
        return Response({"error": "Car not found"},status=status.HTTP_404_NOT_FOUND)


# @api_view(['POST'])
# def create(request):
        
#         # data= request.data
#         # print(type(data))
#         # cars= Car.objects.create(
#         #     price= data['price'],
#         #     quantity= data['quantity']
#         # )

#         serializer= CarModelSerializer(
#             data= request.data
#         )

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 data = serializer.data,
#                 status= status.HTTP_201_CREATED
#             )

#         return Response(
#             data= serializer.errors,
#             status= status.HTTP_400_BAD_REQUEST
#         )

@api_view(['POST'])
# @parser_classes([JSONParser, XMLParser])    # الصيغ المسموح من طرف العميل توصل
# @renderer_classes([JSONRenderer, XMLRenderer, BrowsableAPIRenderer])  # صيغ العرض الممكنة من طرف الباك 
def create(request):
        print("Received data:", request.data) 
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        print("Validation errors:", serializer.errors) 
        return Response(
            data= serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
def delete(request, id):
        try:
            cars= Car.objects.get(pk=id)
            cars.delete()
            return Response(
                data={ "status": "deleted successfully"},
                status = status.HTTP_200_OK
            )
        except:
            return Response(
                status= status.HTTP_400_BAD_REQUEST
            )
''

@api_view(['PUT'])
# @parser_classes([JSONParser, XMLParser])
# @renderer_classes([JSONRenderer, XMLRenderer, BrowsableAPIRenderer])
def update(request, id):
    try: 
        cars = Car.objects.get(pk= id)
        serializer= CarModelSerializer(
            instance= cars, # لأنو عنا اوبجيكت بالاساس موجود بس بدنا نعدل عليه فلازم ننبهو ما تأنشئ اوبجيكت بل عدل على الموجود وانستانس يعني مثيل من الاوبجيكت
            data= request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )
    except Car.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)