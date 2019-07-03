from django import forms
from django.core.exceptions import ValidationError
from example.models import UserProfileInfo, Object
from django.contrib.auth.models import User

def ForbiddenUsernamesValidator(value):
    forbidden_usernames = ['admin', 'settings', 'news', 'about', 'help', 'signin', 'signup',
        'signout', 'terms', 'privacy', 'cookie', 'new', 'login', 'logout', 'administrator',
        'join', 'account', 'username', 'root', 'blog', 'user', 'users', 'billing', 'subscribe',
        'reviews', 'review', 'blog', 'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs',
        'contribute', 'newsletter', 'shop', 'profile', 'register', 'auth', 'authentication',
        'campaign', 'config', 'delete', 'remove', 'forum', 'forums', 'download', 'downloads',
        'contact', 'blogs', 'feed', 'feeds', 'faq', 'intranet', 'log', 'registration', 'search',
        'explore', 'rss', 'support', 'status', 'static', 'media', 'setting', 'css', 'js',
        'follow', 'activity', 'questions', 'network',]
    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')


def InvalidUsernameValidator(value):
    if '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')


def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


def UniqueUsernameIgnoreCaseValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


class UserForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True,
        label='User Name')

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True,
        label='Email')

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        self.fields['username'].validators.append(InvalidUsernameValidator)
        self.fields['username'].validators.append(UniqueUsernameIgnoreCaseValidator)

    def clean(self):
        super(UserForm, self).clean()
        password = self.cleaned_data.get('password')
        return self.cleaned_data


class UserProfileInfoForm(forms.ModelForm):
     portfolio_site = forms.URLField(initial="http://",widget=forms.TextInput(attrs={'class':'form-control'}),
     max_length=250,
     required=True,
     label='Portfolio Site')

     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')


class ObjectForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True,
        label='Name')

    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=300,
        required=True,
        label='Description')

    activated = forms.BooleanField(required=False,initial=False,label='Activated')

    class Meta():
         model = Object
         fields = ('name','description', 'activated', 'slug')
