from typing import __all__
from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
from .models import Car
from .models import Brand


## هدول هنن ال model serializer 
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Car
        fields= '__all__'
        # fields= ['id', 'status']      هون عبر رابط الايبي ما بيوصل من الجدول غير الحقلين هدول علما إنو لازم نعالج هالمشكلة في إنو ما نبعت كل معلومات الجدول مبطنة مشان التحميل هي حكى عنها بظن سومر كيسين بس للارفيل

class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Brand
        fields= '__all__'         # علما إنو فينا نحدد الحقول اللازم إرسالها عبر ال Api





##################################################  هون ال custom serializer 

class CarSerializer(serializers.Serializer):

    
    # id= serializers.UUIDField(
    #     read_only= True      # هي لأنو الآيدي تولد بشكل تلقائي وما نحنا اللي مندخلها (نحن ما منكتبها)
    # )

    # name= serializers.CharField(
    #     required= True,
    #     max_length= 20,
    #     min_length= 2,
    #     validators= [
    #         UniqueValidator(
    #             queryset= Car.objects.all()
    #         )
    #     ]

    
    id= serializers.IntegerField(read_only= True)

    status= serializers.ChoiceField(choices= Car.STATUS_CHOICES,
                                    # source='get_status_display',  # مشان يعرض القيم المخصصة للعرض مو التانية # Display user-friendly status
                                    )

    price= serializers.DecimalField(
        max_digits=20,
        decimal_places=4,
        allow_null= True,
        required= False,
        error_messages={
            'invalid': 'Please enter a valid price.'
            }
    )

    quantity= serializers.IntegerField(
        required= False,
        allow_null= True,
        error_messages={
            'invalid': 'Quantity must be a valid integer.'
        }
    )

    brand= serializers.PrimaryKeyRelatedField(queryset= Brand.objects.all(), required= False, allow_null= True)  # هون مشان لأنو هالحقل بعلاقة فلازم يكون نوعو برايمري ريلايتيد فيلد

    # status_display = serializers.CharField(source='get_status_display', read_only=True)  # هيدي مشان نعرض القيم المرئية للمستخدم ورح تلاحظي بالخرج إنو قيمة الحقل ستاتيوس العادية هية القيم اللي مو مخصصة للعرض والقيمة هون هية المخصصة للعرض 


######### بعض عمليات الفاليديشن عالحقول مثل السعر برايس وال الكمية عملنا تحقق من إنو ما يكونو أعداد سالبة بس تحقق التميز يونيك يفضل يكون الحقل اساسا بالمودل هيك يونيك وهون نعملو يونيك متل المثال المعلق فوق للحق نيم
    
    def validate_quantity(self, value):

        if value is not None and value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value
    

    def validate_price(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value
    
    def create(self, validated_data):
        # Create and return a new Car instance given the validated data
        return Car.objects.create(**validated_data)
