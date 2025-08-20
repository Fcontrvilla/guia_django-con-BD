from .models import Tarea
from django import forms

class TareaForm(forms.ModelForm):
    
    class meta:
        model = Tarea
        fields = ['titulo', 'descripcion']