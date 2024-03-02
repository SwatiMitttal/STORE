from .models import Category
from . import urls
def menu_links(req):
    
        links=Category.objects.all()
        urlls=urls
        return {'links':links}