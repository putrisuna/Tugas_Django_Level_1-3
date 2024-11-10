from django.shortcuts import render
from basicwishes import forms
# Create your views here.
def index(request):
    return render(request, 'basicwishes/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
        
    return render(request, 'basicwishes/form_page.html', {'form':form})