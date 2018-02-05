from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from crispy_forms import helper
from crispy_forms.layout import Submit, Layout, Field, Div, Row, HTML
from django import forms
from event.models import *


class EventForm(ModelForm):

    PRIVACY = (
        ('P', 'List your event publicly for anybody to see.'),
        ('N', 'Only people with the events link can see the event. It will be unlisted')
    )
    ALLOW_RESELL_CHOICES = (
        ('Y', 'Yes! - I want event goers to be able to resell their tickets.'),
        ('N', 'No! - I do not want people to be able to resell their tickets')
    )

    RESELL_WHEN_CHOICES = (
        # W: Whenever
        # S: Sold Out
        # A: Amount
        ('W', 'Allow event goers to resell their tickets at anytime.'),
        ('S', 'Allow event goers to resell their tickets after the event has sold out.'),
        ('A', 'Allow event goers to resell their tickets after a certain amount of tickets have been sold.')
    )

    title = forms.CharField(max_length=265)
    location = forms.CharField(max_length=256)
    start_date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}
    ))
    start_time = forms.TimeField()
    end_date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}
    ))
    end_time = forms.TimeField()
    image = forms.ImageField()
    organiser = forms.ModelChoiceField(queryset=None)
    description = forms.CharField(widget=forms.Textarea)
    privacy = forms.ChoiceField(choices=PRIVACY)
    show_remaining_tickets = forms.BooleanField(required=False)
    allow_resell = forms.ChoiceField(choices=ALLOW_RESELL_CHOICES)
    when_resell = forms.ChoiceField(choices=RESELL_WHEN_CHOICES, required=False)
    amount_resell = forms.IntegerField(required=False)

    class Meta:
        model = Event
        fields = '__all__'


    # Overriding save allows us to process the value of the servers, variables and required packages.
    def save(self, commit):
        # Get the unsave Package instance
        instance = forms.ModelForm.save(self, False)

        print("Hello World")


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        forms.ModelForm.__init__(self, *args, **kwargs)

        self.fields['title'].label = 'Event Title'
        self.fields['start_time'].label = 'Time'
        self.fields['start_date'].label = 'Date'
        self.fields['end_time'].label = 'Time'
        self.fields['end_date'].label = 'Date'
        self.fields['privacy'].label = 'Privacy'
        self.fields['show_remaining_tickets'].label = 'Show the number of remaining tickets on the event page'
        self.fields['allow_resell'].label = 'Would you like event goers to be able to resell their tickets on Ticketr?'
        self.fields['when_resell'].label = 'When would you like event goers to be able to resell their tickets?'
        self.fields['amount_resell'].label = 'How many tickets should be sold before reselling can occur?'

        # Fill in the persons organiser accounts
        self.fields['organiser'].queryset = Organiser.objects.all().filter(user=self.request.user)

        # Crispy forms layout
        self.helper.layout = Layout(
            HTML("""<h2><span class="badge badge-dark">1</span> Let's get some basic information</span></h2><hr/>"""),
            Div(Field('title', css_class='form-control', placeholder='Give your event a name'), css_class='form-group'),
            Div(Field('location', css_class='form-control', placeholder='Your location will help users find your event'), css_class='form-group'),
            Row(
                Div(HTML("""<h5><i class="fa fa-hourglass-start" aria-hidden="true"></i> Start</h5><hr/>"""), css_class='col-md-6'),
                Div(HTML("""<h5><i class="fa fa-hourglass-end" aria-hidden="true"></i> End</h5><hr/>"""), css_class='col-md-6')
            ),
            Row(
                Div(Field('start_date', css_class='form-control'), css_class='form-group col-md-3'),
                Div(Field('start_time', css_class='form-control', placeholder="23:00"), css_class='form-group col-md-3'),
                Div(Field('end_date', css_class='form-control'), css_class='form-group col-md-3'),
                Div(Field('end_time', css_class='form-control', placeholder="23:00"), css_class='form-group col-md-3'),
            ),
            HTML("""<br/><h2><span class="badge badge-dark">2</span> Make it pretty & get some more information</span></h2><hr/>"""),
            Row(
                Div(Field('image', css_class='form-control'), css_class='form-group col-md-4'),
                Div(Field('description', css_class='form-control'), css_class='form-group col-md-8'),
            ),
            HTML("""<div class="float-right" style="padding-bottom: 1%"><a href="" class="btn btn-success btn-sm">Create Organiser</a></div>"""),
            Div(Field('organiser', css_class='form-control'), css_class='form-group'),
            HTML("""<br/><h2><span class="badge badge-dark">3</span> Let's create some tickets</span></h2><hr/>"""),
            Div(HTML('''
            <button type="button" class="btn btn-success btn-block" onClick="addInput('dynamicInput');"><i class="fa fa-plus" aria-hidden="true"></i> Add a Ticket</button>
            <br/>
                <div id="dynamicInput">
                 </div>
            '''), css_class='form-group', css_id='dropdownoption'),
            HTML("""<br/><h2><span class="badge badge-dark">4</span> Finally, some additional settings.</span></h2><hr/>"""),
            Div(Field('privacy', css_class='form-control'), css_class='form-group'),
            Div(Field('show_remaining_tickets', css_class='form-check-input'), css_class='form-check mb-2 mr-sm-2'),
            HTML("""<br/><strong>Resell Settings:</strong><hr/>"""),
            Div(Field('allow_resell', css_class='form-control'), css_class='form-group'),
            Div(Field('when_resell', css_class='form-control'), css_class='form-group'),
            Div(Field('amount_resell', css_class='form-control'), css_class='form-group'),
            HTML("""<br/><div class="card text-center"><div class="card-body"><h1>Awesome! Let's make it official.</h1>"""),
            Div(Submit('submit', 'Make Event Live', css_class='btn btn-success btn-block btn-lg')),
            HTML("""</div></div>""")
        )