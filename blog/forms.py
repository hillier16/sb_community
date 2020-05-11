from django import forms
from .models import MyUser


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['nickname','username', 'email', 'password']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control',  'placeholder': '로그인을 할 id 입니다.'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '15자 이내로 입력 가능합니다.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nickname': '닉네임',
            'username': '이름',
            'email': '이메일',
            'password': '패스워드'
        }

    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15