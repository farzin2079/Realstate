from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages

from account.models import Profile

from .forms import PropertyForm
from .models import Property, Category

@login_required(login_url='/login')
def index(request):
    prop = Property.objects.order_by("-updated").all()
    paginator = Paginator(prop , 12)
    page_num = request.GET.get('page')
    page_objs = paginator.get_page(page_num)

    categorys = Category.objects.all()
    
    return render(request, 'property/index.html', {
        "categorys":categorys,
        "propertis": page_objs,
    })

@login_required(login_url='/login')
def details(request, id):
    prop = Property.objects.get(pk=id)
    categorys = Category.objects.all()

    return render(request, "property/details.html",{
        "propertys":prop,
        "categorys":categorys
    })

@login_required(login_url='/login')
def category(request, id):

    category = Category.objects.get(pk=id)
    prop = category.property.all()

    paginator = Paginator(prop , 10)
    page_num = request.GET.get('page')
    page_objs = paginator.get_page(page_num)

    categorys = Category.objects.all()
    
    return render(request, 'property/index.html', {
        "categorys": categorys,
        "propertis": page_objs,
    })

@login_required(login_url="/login")
def addprop(request):
    categorys = Category.objects.all()
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.real_state = profile
            saved.save()
            category = Category.objects.get(pk=request.POST["category"])
            category.property.add(saved)
            profile.propertys.add(saved)

        return redirect("property")

    else:
        return render(request, 'property/addprop.html',{
            "categorys": categorys,
            "form": PropertyForm,
            "profile": profile
        })
    
@csrf_exempt
@login_required(login_url='/login')
def watchlist(request, id):
    prop = Property.objects.get(pk=id)
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":

        try:
            try:
                propwatch = prop.watchlist.get(id=profile.id)
                prowatch = profile.watchlist.get(id=prop.id)

                prop.watchlist.remove(profile)
                profile.watchlist.remove(prop)
                return JsonResponse({"message" : "success", "action": "remove"})
            except:
                prop.watchlist.add(profile)
                profile.watchlist.add(prop)
                return JsonResponse({"message" : "success", "action": "add"})

        
        except:
            return JsonResponse({"message" : "faild"})
    
    else:
        try: 
            propwatch = prop.watchlist.get(id=profile.id)
            prowatch = profile.watchlist.get(id=prop.id)
            return JsonResponse ({ "exist": "true"})
        except:
            return JsonResponse({ "exist": "false"})
        
@csrf_exempt
@login_required(login_url="/login")
def delete(request):
    if request.method == "POST":
        id = request.POST["id"]
        prop = Property.objects.get(pk=id)
        try:
            prop.delete()
            messages.success(request ,"success")
            return redirect("property")
        except:
            messages.error(request ,"faild")
            return redirect("details", args=id)
    else:
        messages.error(request ,"invalid request")
        return redirect("details", id=id)

