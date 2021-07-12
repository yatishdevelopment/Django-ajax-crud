from django.http.response import JsonResponse
from django.shortcuts import render
from myapp.models import Mobile
from django.views.decorators.csrf import csrf_exempt

def all_mobiles(request):
    mobile_data = Mobile.objects.all()
    return render(request,"myapp/mobiles.html",{"mobiles":mobile_data})

@csrf_exempt
def save_mobile(request):
    try:
        id = request.POST.get("id")
        mobile_name = request.POST['mobileName']
        ram = request.POST['ram']
        color = request.POST['color']
        price = request.POST['price']

        if id is not None:
            mobile = Mobile.objects.get(id=int(id))
            mobile.name = mobile_name
            mobile.ram = ram
            mobile.color = color
            mobile.price = price
            mobile.save()
            return JsonResponse({"code":1,"data":mobile.id})
            
        mobile = Mobile.objects.create(name=mobile_name,ram=ram,color=color,price=price)
        return JsonResponse({"code":1,"id":mobile.id})
    except Exception as e:
        return JsonResponse({"code":0,"msg":"Error occured"})

@csrf_exempt
def delete_mobile(request):
    try:
        mobile = Mobile.objects.filter(id=int(request.POST["id"])).delete()
        return JsonResponse({"code":1,"data":"success"})
    except Exception as e:
        return JsonResponse({"code":0,"msg":"error ocured"})