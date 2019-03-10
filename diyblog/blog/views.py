from django.shortcuts import render
from blog.models import Blogger, Blog
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_bloggers = Blogger.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
        # sets the value of the 'num_visits' session key to 0 if it has not previously been set
    request.session['num_visits'] = num_visits + 1
        # each time a request is received, the value is incremented and store it back in the session

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5

class BloggerDetailView(generic.DetailView):
    model = Blogger
