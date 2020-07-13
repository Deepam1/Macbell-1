# import form class from django 
from django import forms 
  
# import GeeksModel from models.py 
from .models import User_Register 
  
# create a ModelForm 
class About_form(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = User_Register 
        fields = "__all__"
    
