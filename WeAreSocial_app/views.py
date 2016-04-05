from django.shortcuts import render
from WeAreSocial_app.models import Contact
# Create your views here.

# Create your views here.
def get_contacts(request):
    return render(request, "WeAreSocial/home.html",
                  {'contact_list': Contact.objects.all()})