from django import forms
from backend.models.medico_model import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['first_name', 'last_name', 'email', 'cpf', 'rg', 'crm', 'especialidades', 'birth_date', 'address', 'estado_civil', 'genero', 'phone_number']
        widgets = {
            "especialidades": forms.SelectMultiple(attrs={"class": "select2"}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'crm': 'CRM',
            'especialidades': 'Especialidades',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'cpf': 'CPF',
            'rg': 'RG',
            'birth_date': 'Data de Nascimento',
            'address': 'Endereço',
            'estado_civil': 'Estado Civil',
            'genero': 'Gênero',
            'phone_number': 'Telefone',
        }
