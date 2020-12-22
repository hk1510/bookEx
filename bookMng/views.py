from django.shortcuts import render
from django.http import HttpResponse
from .models import MainMenu
from django.db.models import Q
from .forms import ReviewForm
from .forms import BookForm
from django.http import HttpResponseRedirect

from .models import Book
from .models import Review

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model


# Create your views here.


def index(request):
    # return HttpResponse("<h1 align='center'>Hello World</h1>")
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
                  'bookMng/home.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  }
                  )


##@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():

            review = form.save(commit=False)
            try:
                review.username = request.user
                review.book_id = book_id
            except Exception:
                pass
            review.save()
            return HttpResponseRedirect('/book_detail/'+str(book_id))
    else:
        form = ReviewForm()
        book = Book.objects.get(id=book_id)
        reviews = Review.objects.filter(book_id=book_id)
        book.pic_path = book.picture.url[14:]
        return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'form': form,
                      'book': book,
                      'reviews': reviews,
                  })


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


@login_required(login_url=reverse_lazy('login'))
def displayusers(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request,
                  'bookMng/displayusers.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'users': users
                  })


@login_required(login_url=reverse_lazy('login'))
def user_detail(request, user_id):
    User = get_user_model()
    user = User.objects.get(id=user_id)
    return render(request,
                  'bookMng/user_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'user': user
                  })


@login_required(login_url=reverse_lazy('login'))
def myprofile(request):
    User = get_user_model()
    user = request.user
    return render(request,
                  'bookMng/myprofile.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'user': user
                  })


def about_page(request):

    return render(request,
                  "bookMng/about_page.html",
                  {
                      "item_list": MainMenu.objects.all()
                  }
                  )


def about_us(request):

    return render(request,
                  "bookMng/about_us.html",
                  {
                      "item_list": MainMenu.objects.all()
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def requestbook(request):
    # return HttpResponse("<h1 align='center'>Hello World</h1>")
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
                  'bookMng/requestbook.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def searchbar(request):
    query = request.GET.get('q')

    queryset = Book.objects.all()

    if query is not None:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(username__username__icontains=query)
        )
        for b in queryset:
            b.pic_path = b.picture.url[14:]

    context = {
        "books": queryset,
        "item_list": MainMenu.objects.all(),
    }
    template = "bookMng/searchbar.html"
    return render(request, template, context)


##@login_required(login_url=reverse_lazy('login'))
def sorting(request):
    choice = request.GET.get('choice')
    if choice == '-price':
        books = Book.objects.all().order_by('-price')
    elif choice == 'price':
        books = Book.objects.all().order_by('price')
    elif choice == 'name':
        books = Book.objects.all().order_by('name')
    elif choice == '-name':
        books = Book.objects.all().order_by('-name')
    elif choice == 'publishdate':
        books = Book.objects.all().order_by('publishdate')
    elif choice == '-publishdate':
        books = Book.objects.all().order_by('-publishdate')
    elif choice == None:
        books = Book.objects.filter(name='None')

    if books is not None:
        for b in books:
            b.pic_path = b.picture.url[14:]
        return render(request,
                      'bookMng/sorting.html',
                      {
                          'item_list': MainMenu.objects.all(),
                          'books': books,
                      })


@login_required(login_url=reverse_lazy('login'))
def add_to_shopping_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.username != request.user:
        book.shopping_cart_user.add(request.user)
        book.save()
    return HttpResponseRedirect('/book_detail/' + str(book_id))


@login_required(login_url=reverse_lazy('login'))
def remove_shopping_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    book.shopping_cart_user.remove(request.user)
    book.save()
    return HttpResponseRedirect('/book_detail/' + str(book_id))


@login_required(login_url=reverse_lazy('login'))
def remove_in_shopping_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    book.shopping_cart_user.remove(request.user)
    book.save()
    books = Book.objects.filter(shopping_cart_user=request.user)
    return HttpResponseRedirect('/shopping_cart')


@login_required(login_url=reverse_lazy('login'))
def shopping_cart(request):
    books = Book.objects.filter(shopping_cart_user=request.user)
    totalprice = 0
    for book in books:
        totalprice += book.price
    return render(request,
                  'bookMng/shopping_cart.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'totalprice': totalprice
                  })


@login_required(login_url=reverse_lazy('login'))
def buybooks(request):
    books = Book.objects.filter(shopping_cart_user=request.user)
    for book in books:
        book.pic_path = book.picture.url[14:]
        book.purchased = True
        book.shopping_cart_user.clear()
        book.save()
    return render(request,
                  'bookMng/buybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })
