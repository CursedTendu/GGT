from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Favorite, Profile, Rating
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import ProductForm, ReviewForm
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from authentication.models import User


def product_list(request):
    products = Product.objects.all

    return render(request, 'market/product_list.html', {'products': products})

def product_detail(request, product_id):
       product = get_object_or_404(Product, id = product_id)
       is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()

       if request.method == 'POST':
           form = ReviewForm(request.POST)

           if form.is_valid():
               review = form.save(commit = False)
               review.product = product
               review.author = request.user.username
               review.save()
               return redirect('market:product_detail', product_id = product_id)
       else:
           form = ReviewForm()
       reviews = product.reviews.all()

       return render(request, 'market/product_detail.html', {'product': product, 'form': form, 'reviews': reviews, 'is_favorite': is_favorite})

@login_required  
def favorite_products(request):
    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'market/favorite_products.html', {'favorites': favorites})

@login_required  
def toggle_favorite(request, product_id):
    product = Product.objects.get(id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if not created:
        favorite.delete()

    return redirect('market:product_detail', product_id=product_id)

class user_profile(LoginRequiredMixin, TemplateView):
       template_name = 'market/user_profile.html'

def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    products = Product.objects.filter(user=user)
    average_rating = profile.average_rating
        
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        rating = Rating(user=user, rating=rating_value)
        rating.save()

    return render(request, 'market/profile.html', {'profile': profile,  'products': products, 'average_rating': average_rating})

class ProductCreateEditDelete:
    @login_required
    def create_product(request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return redirect('market:product_list')
        else:
            form = ProductForm()
        return render(request, 'market/create_product.html', {'form': form})

    @login_required
    def delete_product(request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if product.user == request.user:
            product.delete()
        return redirect('market:product_list')

    @login_required
    def edit_product(request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('market:product_list')
        else:
            form = ProductForm(instance=product, initial={'service_name': product.service_name, 'game_version': product.game_version, 'service_type': product.service_type, 'price': product.price, 'description': product.description})
        return render(request, 'market/edit_product.html', {'form': form})

'''
class ProductCreateEditDelete(LoginRequiredMixin, View):
    form_class = ProductForm
    template_create = 'market/create_product.html'
    template_edit = 'market/edit_product.html'
    template_delete = 'market/delete_product.html'
    success_url = 'market:product_list'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_create, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect(self.success_url)
        return render(request, self.template_create, {'form': form})

    def delete(self, request, product_id):
        product = get_object_or_404(Product, id = product_id)
        if product.user == request.user:
            product.delete()
        return redirect(self.success_url)

    def put(self, request, product_id):
        product = get_object_or_404(Product, id = product_id)
        form = self.form_class(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_edit, {'form': form})
'''

'''       
@login_required
def create_product(request):
       if request.method == 'POST':
           form = ProductForm(request.POST)
           if form.is_valid():
               product = form.save(commit=False)
               product.user = request.user
               product.save()
               return redirect('market:product_list')
       else:
           form = ProductForm()
       return render(request, 'market/create_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
       product = get_object_or_404(Product, id = product_id)
       if product.user == request.user:
           product.delete()
       return redirect('market:product_list')

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('market:product_list')
    else:
        form = ProductForm(instance = product, initial = {'service_name': product.service_name, 'game_version': product.game_version, 'service_type': product.service_type, 'price': product.price, 'discription': product.discription})
    return render(request, 'market/edit_product.html', {'form': form})
'''

'''
class ProductCreateEditDelete(LoginRequiredMixin, View):
    template_create = 'market/create_product.html'
    template_edit = 'market/edit_product.html'
    success_url = 'market:product_list'

    def post(self, request, product_id = None):
        if product_id is None:
            form = ProductForm(request.POST)
        else:
            product = get_object_or_404(Product, id = product_id)
            form = ProductForm(request.POST, instance = product)

        if form.is_valid():
            if product_id is None:
                product = form.save(commit=False)
                product.user = request.user
                product.save()
            else:
                form.save()
            return redirect(self.success_url)
        return render(request, self.template_create, {'form': form})

    def get(self, request, product_id = None):
        if product_id is None:
            form = ProductForm(instance = product)
        else:
            product = get_object_or_404(Product, id = product_id)
            form = ProductForm(instance=product)
        return render(request, self.template_edit, {'form': form})

    def delete(self, request, product_id):
        product = get_object_or_404(Product, id = product_id)
        if product.user == request.user:
            product.delete()
        return redirect(self.success_url)
'''
