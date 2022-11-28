from django import forms
from django.core.exceptions import ValidationError
from blog.models import Associado
from datetime import date

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('f', 'Feminino'),
    ('n', 'Não Informar')
)

class AssociadoForm(forms.ModelForm):
    class Meta:
        model = Associado
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'id-nome'})
        self.fields['numero_associado'].widget.attrs.update({'class': 'id-nassoc'})
        self.fields['sexo'].widget.attrs.update({'class': 'id-sexo'})
        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-data'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-fone'})
        self.fields['celular'].widget.attrs.update({'class': 'mask-cel'})
        self.fields['email'].widget.attrs.update({'class': 'id-email'})

# esse bloco faz as validações
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 9:
            raise ValidationError("Digite seu nome completo")
        else:
            return nome

    def clean_dt_nasc(self):
        dt_nasc = self.cleaned_data.get['data_nascimento']
        if dt_nasc >= date.today():
            raise ValidationError('A data de nascimento não pode ser maior ou igual a data atual')
        else:
            return dt_nasc
