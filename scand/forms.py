from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from taggit.forms import TagField

from scandoc import settings
from .models import ImageTag


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageTag
        exclude = ('created_at', 'changed_at', 'changed_by', 'status', 'is_reverted', 'is_forwarded')
        widgets = {
            'start_date': DatePickerInput(options={'format': 'DD/MM/YYYY', 'debug': True}).start_of('event active days'),
            'end_date': DatePickerInput(options={'format': 'DD/MM/YYYY', 'debug': True}).end_of('event active days'),
        }

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = visible.field.label
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
        self.fields['start_date'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['end_date'].input_formats = settings.DATE_INPUT_FORMATS

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        print(end_date)
        if start_date not in (None, '') and end_date not in (None, '') and start_date > end_date:
            msg = "From date can't be greater than till date"
            self.add_error('start_date', msg)


class SearchForm(forms.Form):
    company = forms.CharField(max_length=200, required=False, label='Company')
    accoff = forms.CharField(max_length=200, required=False, label='Office / Deptt')
    section = forms.CharField(max_length=200, required=False, label='Section')
    docref = forms.CharField(max_length=200, required=False, label= 'Document Ref')
    start_date = forms.DateField(label='Start Date', widget=DatePickerInput(format='%d/%m/%Y'), required=False)
    end_date = forms.DateField(label='End Date', widget=DatePickerInput(format='%d/%m/%Y'), required=False)
    pagenum = forms.CharField(max_length=200, required=False, label='Page No')
    refnum = forms.CharField(max_length=200, required=False, label='Reference No')
    pernum = forms.CharField(max_length=200, required=False, label='Personnel ID')
    attr1 = forms.CharField(max_length=200, required=False, label='Extra Attribute 1')
    attr2 = forms.CharField(max_length=200, required=False, label='Extra Attribute 2')
    attr3 = forms.CharField(max_length=200, required=False, label='Extra Attribute 3')
    attr4 = forms.CharField(max_length=200, required=False, label='Extra Attribute 4')
    attr5 = forms.CharField(max_length=200, required=False, label='Extra Attribute 5')
    tags = TagField(required=False)

    class Meta:
        widgets = {
            'start_date': DatePickerInput(options={'format': 'DD/MM/YYYY', 'debug': True}).start_of('event active days'),
            'end_date': DatePickerInput(options={'format': 'DD/MM/YYYY', 'debug': True}).end_of('event active days'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['end_date'].input_formats = settings.DATE_INPUT_FORMATS

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        print(end_date)
        if start_date not in (None, '') and end_date not in (None, '') and start_date > end_date:
            msg = "From date can't be greater than till date"
            self.add_error('start_date', msg)
