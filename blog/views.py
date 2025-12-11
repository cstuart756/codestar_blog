from django.http import HttpResponse

# Create your view for the blog home
def blog_home(request):
    return HttpResponse("Hello, blog!")
