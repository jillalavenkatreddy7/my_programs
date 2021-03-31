from django.shortcuts import render,redirect
from .models import AddFood,AddNewCustomer,CustomerOrder
from django.contrib import messages
from .forms import OderForm
# Create your views here.
def showIndex(request):
    return render(request,"OnlineFoodOrder.html",{"data":"Welcome To Reddy's Food Court"})
def entry(request):
    who=request.GET.get("who")
    if(who=="Admin"):
        return render(request,"AdminLogin.html",{"data":"Welcome To Admin Login Panel"})
    if(who=="Customer"):
        return render(request, "CustomerLogin.html", {"data": "Welcome To Customer Login Panel"})

def validate(request):
    uname=request.POST.get("u")
    pword=request.POST.get("p")
    if(uname=="admin" and pword=="admin"):
        return render(request,"AdminPanel.html",{"data1":"Welcome To Admin Panel"})
    else:
        return render(request, "AdminLogin.html", {"data1": "invalid details"})
def addFodd(request):
    return render(request,"AddFood.html",{"data2":"Enter the details to add the food "})

def logout(request):
    del request.session["username"]
    return redirect("index")


def logout1(request):
    return redirect("index")


def previous(request):
    return render(request,"AdminPanel.html")

def saveFood(request):
    Food_type=request.POST.get("type")
    Food_name=request.POST.get("fn")
    Food_price=request.POST.get("fp")
    Food_image=request.FILES["fi"]
    AddFood(Food_Type=Food_type,Food_Name=Food_name,Food_price=Food_price,Food_image=Food_image).save()
    messages.success(request,"Saved Sucessfully")
    return redirect("addfood")

def viewFoods(request):
    food_data=AddFood.objects.all()
    return render(request,"viewFoods.html",{"food_data":food_data,"data":"Food details panel"})

def deleteFood(request):
    id=request.GET.get("id")
    AddFood.objects.filter(Food_id=id).delete()
    return redirect("viewfoods")


def updateFood(request):
    ud=request.GET.get("update")
    data=AddFood.objects.filter(Food_id=ud)
    return render(request,"update.html",{"data":data,"data2":"Enter the details to update the food "})
def updatedataFood(request):
    id=request.POST.get("fid")
    Food_type=request.POST.get("type")
    Food_name=request.POST.get("fn")
    Food_price=request.POST.get("fp")
    Food_image=request.FILES["fi"]
    addupdate=AddFood.objects.get(Food_id=id)
    addupdate.Food_Type=Food_type
    addupdate.Food_Name=Food_name
    addupdate.Food_price=Food_price
    addupdate.Food_image=Food_image
    addupdate.save()
    return viewFoods(request)
def back(request):
    return redirect("viewfoods")
def newcustomer(request):
    return render(request,"newcustomer.html",{"data":"Welcome to customer registration panel"})
def backcustomer(request):
    return render(request,"CustomerLogin.html")
def newcustomersave(request):
    customer_name=request.POST.get("cn")
    customer_contact=request.POST.get("ccn")
    customer_password=request.POST.get("cp")
    customer_confirm =request.POST.get("cp1")
    username=request.POST.get("un")
    if(customer_password==customer_confirm):
        AddNewCustomer(customer_name=customer_name,customer_contact_number=customer_contact,password=customer_password,username=username).save()
        return render(request,"newcustomer.html",{"data1":"Customer data saved sucessfully"})
    else:
        return render(request,"newcustomer.html",{"data1":"Customer password not yet confirmed"})

def customerlogin(request):
    username=request.POST.get("uc")
    password=request.POST.get("pc")
    try:
        data=AddNewCustomer.objects.get(username=username,password=password)
        if data:
            request.session["username"]=username
            return render(request,"CustomerHome.html",{"data4":data})
    except:
        messages.success(request,"invalid details")
        return render(request,"CustomerLogin.html")

def customerViewFoods(request):
    food_data=AddFood.objects.all()
    return render(request,"customerViewFoods.html",{"food_data":food_data})

def backcustomer1(request):
    return render(request,"CustomerHome.html")
def order(request):
    data=AddFood.objects.all()
    form=OderForm()
    return render(request,"order.html",{"data":data,"form":form})
def ordersave(request):
    food_type=request.POST.get("Food_type")
    food_name=request.POST.get("type")
    price=request.POST.get("price")
    qty=request.POST.get("qty")
    p1=float(price)
    qty2=int(qty)
    total_price=p1*qty2
    CustomerOrder(Food_type_id=food_type,Food_Name=food_name,Price=price,Food_qty=qty,Total_Amount_paid=total_price).save()
    messages.success(request,"your order placed sucessfully")
    return customerViewFoods(request)