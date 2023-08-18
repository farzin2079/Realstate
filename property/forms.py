from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = (
            "title",
            "area",
            "vpm",
            "value",
            "image1",
            "image2",
            "image3",
            "image4",
            "category",
            "discription",
        )

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({ 'class': "form-control"})