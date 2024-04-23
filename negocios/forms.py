from django import forms


class FormularioDeCadastro(forms.Form):
    usuario = forms.CharField(label='usuario', max_length=150)
    email = forms.EmailField(label='Email', error_messages={
                             'invalid': 'Por favor, insira um email válido.'})
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
