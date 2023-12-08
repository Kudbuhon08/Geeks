from django.shortcuts import render
from apps.geeks.models import Settings, Contact, About, Values, Junior, Portfolio,Blog
# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    about = About.objects.latest("id")
    values = Values.objects.latest("id")
    junior = Junior.objects.latest("id")
    portfolio_id = Portfolio.objects.latest("id")
    portfolio_all = Portfolio.objects.all()
    blog = Blog.objects.all()
    return render(request, "index_2.html", locals())
 

def contact(request):
    contact = Contact.objects.latest("id")
    return render(request, "contact.html", locals()) 

def blog_detail(request,id):
    settings = Settings.objects.latest("id")
    about = About.objects.latest("id")
    values = Values.objects.latest("id")
    junior = Junior.objects.latest("id")
    portfolio_id = Portfolio.objects.latest("id")
    portfolio_all = Portfolio.objects.all()
    blog = Blog.objects.get()
    return render(request, 'blog_details.html', locals())