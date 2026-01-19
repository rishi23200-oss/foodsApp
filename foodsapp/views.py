from django.shortcuts import render, get_object_or_404,redirect
from foodsapp.models import FoodItems


# def allfoods(request):
#     allfooditem = FoodItems.objects.all()
#     return render(request, 'foods/allfoods.html',{'allfooditem':allfooditem})

def allfoods(request):
    selected_category = request.GET.get('catogery')

    if selected_category:
        allfooditem = FoodItems.objects.filter(catogery=selected_category)
    else:
        allfooditem = FoodItems.objects.all()

    return render(request, 'foods/allfoods.html', {
        'allfooditem': allfooditem,
        'categories': FoodItems.Catageries,
        'selected_category': selected_category
    })

def Food_details(request, id):
    fooditems = get_object_or_404(FoodItems, id=id)
    return render(request, 'foods/foodDetails.html', {'fooditems': fooditems})

def addFood(request):
    if request.method == 'POST':
        FoodItems.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            rating=request.POST.get('rating'),
            catogery =request.POST.get('Categories'),
            description=request.POST.get('description'),
            foodimg = request.FILES.get('food_image')
        )
        return redirect('allfoods')

    return render(request, 'foods/addnewfood.html')









