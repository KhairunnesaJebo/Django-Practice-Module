from django import forms
from django.forms.widgets import NumberInput
import datetime
# from django.core import validators

BIRTH_YEAR_CHOICES = ['1996', '1997', '1998']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
GEEKS_CHOICES = ( 
    (1, "A"), 
    (2, "B"), 
    (3, "C"),
    (4, "D"), 
    (5, "E"), 
    ) 

DEMO_CHOICES =( 
    ("1", "Naveen"), 
    ("2", "Pranav"), 
    ("3", "Isha"), 
    ("4", "Saloni"), 
) 

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(
	max_length = 10,
    )
    email_address = forms.EmailField( 
    label="Please enter your email address",
    )
    first_name = forms.CharField(initial='Your name')
    agree2 = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors2 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

    first_name2 = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput())
  
    geeks_field = forms.TypedChoiceField( 
                   choices = GEEKS_CHOICES, 
                   coerce = str
                  ) 
    geeks_field2 = forms.DateTimeField( ) 
    geeks_field3 = forms.DurationField( ) 
    geeks_field4 = forms.FileField() 
    geeks_field5 = forms.FilePathField(path = "practice_project1/")
    geeks_field6 = forms.FloatField( )
    geeks_field7 = forms.ImageField()
    # geeks_field8 = forms.IntegerField(max_length = 200) 
    geeks_field8 = forms.GenericIPAddressField( )
    geeks_field9 = forms.TypedMultipleChoiceField( 
                             choices = DEMO_CHOICES, 
                             coerce = int
                             )     
    geeks_field10 = forms.NullBooleanField( )
    geeks_field11 = forms.RegexField(regex = "K.*a")
    geeks_field12 = forms.TimeField( ) 
    geeks_field13 = forms.URLField( ) 
    