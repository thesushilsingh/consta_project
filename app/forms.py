from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name','document','user_id')
    name = forms.CharField(label='Name', max_length=250)
    document = forms.FileField()