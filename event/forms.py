from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from crispy_forms import helper
from crispy_forms.layout import Submit, Layout, Field, Div, Row, HTML
from django import forms
from event.models import *


class EventForm(ModelForm):
    title = forms.CharField(max_length=265)
    location = forms.CharField(max_length=256)
    start_date = forms.DateField()
    start_time = forms.DateTimeField()
    end_date = forms.DateField()
    end_time = forms.DateTimeField()
    image = forms.ImageField()
    organiser = forms.ModelChoiceField(queryset=None)
    description = forms.CharField(widget=forms.Textarea)
    privacy = forms.BooleanField()
    show_remaining_tickets = forms.BooleanField()

    class Meta:
        model = Event
        fields = '__all__'

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
        self.fields['privacy'].label = 'Make this event private (Only people with the link can view it)'
        self.fields['show_remaining_tickets'].label = 'Show the number of remaining tickets on the event page'

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
                Div(Field('start_time', css_class='form-control'), css_class='form-group col-md-3'),
                Div(Field('end_date', css_class='form-control'), css_class='form-group col-md-3'),
                Div(Field('end_time', css_class='form-control'), css_class='form-group col-md-3'),
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
            Div(Field('privacy', css_class='form-check-input'), css_class='form-check mb-2 mr-sm-2'),
            Div(Field('show_remaining_tickets', css_class='form-check-input'), css_class='form-check mb-2 mr-sm-2'),
        )