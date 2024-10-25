from rest_framework.decorators import( 
    api_view,
    renderer_classes,
    parser_classes
    )
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import( 
    JSONRenderer,
    BrowsableAPIRenderer
    )
from rest_framework.parsers import JSONParser
from rest_framework_xml.renderers import XMLRenderer # لازم نروح ع موقع ال rest framework  ونفوت ع قسم renderers  ونشوف صيغة xml  لأنو إلها مستلزمات للتنزيل 
# from rest_framework.parsers import XMLParser ما مشي حالها لأنو ما بتدعم البارسر لهيك استخدمنا اللي تحتا 
from rest_framework_xml.parsers import XMLParser
from ..models import Car
from ..models import Brand
from ..serializers import CarModelSerializer
from ..serializers import BrandModelSerializer


@api_view(['GET','POST'])
@renderer_classes([BrowsableAPIRenderer,JSONRenderer,XMLRenderer])
def index(request):
    brands= Brand.objects.all()
    serializer= BrandModelSerializer(brands, many=True)

    return Response(serializer.data,
                    status= status.HTTP_201_CREATED,
                    )

@api_view(['DELETE'])
def delete(request, id):
    try:
        brands = Brand.objects.get(pk=id)
        brands.delete()
        return Response (
            data = {
                'status': "Deleted Successfully "
                    }
        )
    except Brand.DoesNotExist:
        return Response(
            status= status.HTTP_404_NOT_FOUND
        )