# Create your views here.
from google.appengine.ext import db

import django
from django import shortcuts

from blog.models import BlogPost

def index(request):
    """Displays the index page."""
    # Fetch all of the BlogPosts
    posts = BlogPost.all().order('-date')

    # Setup the data to pass on to the template
    template_values = {
        'posts': posts,
    }

    # Load and render the template
    return shortcuts.render_to_response('index.html', template_values)
