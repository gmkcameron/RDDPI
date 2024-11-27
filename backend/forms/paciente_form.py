from django import forms
from backend.models.paciente_model import Paciente
from django.forms.widgets import DateInput as DjangoDateInput
from datetime import datetime

class PacienteForm(forms.ModelForm):
    title = "Informações Pessoais"
    
    field_order = [
        "phone_number",
        "first_name",
        "last_name",
        "email",
        "birth_date_field",
        "cpf",
        "rg",
        "address",
        "estado_civil",
        "genero",
        "nome_responsavel",
        "telefone_responsavel",
        "grau_parentesco",
        "doencas_cronicas",
        "alergias",
        "medicamentos",
        "cirurgias",
        "historico_internacoes",
        "condicoes_cognitivas",
        "alteracoes_humor",
        "comportamento_social",
    ]
    
    birth_date_field = forms.DateField(
        widget=DjangoDateInput(
            attrs={"type": "date", 'class': 'form-control', 'required': False}),
        label='Data de Aniversário',
    )
    
    # Configuração para o campo Medicamentos usando SelectMultiple
    medicamentos = forms.MultipleChoiceField(
        choices=[
            ("Paracetamol", "Paracetamol"),
            ("Ibuprofeno", "Ibuprofeno"),
            ("Dipirona", "Dipirona"),
            ("AAS", "AAS"),
            ("Amoxicilina", "Amoxicilina"),
            ("Omeprazol", "Omeprazol"),
            ("Metformina", "Metformina"),
            ("Insulina", "Insulina"),
            ("Losartana", "Losartana"),
            ("Clonazepam", "Clonazepam"),
            ("Diazepam", "Diazepam"),
            ("Captopril", "Captopril"),
            ("Enalapril", "Enalapril"),
            ("Simeticona", "Simeticona"),
            ("Diclofenaco", "Diclofenaco"),
        ],
        widget=forms.SelectMultiple(attrs={"class": "form-control select2", "id":  'id_medicamentos'}),
        label="Medicamentos",
        required=False,
    )
    
    doencas_cronicas = forms.MultipleChoiceField(
        choices=[
            ("Diabetes", "Diabetes"),
            ("Hipertensão Arterial", "Hipertensão Arterial"),
            ("Asma", "Asma"),
            ("DPOC", "Doença Pulmonar Obstrutiva Crônica"),
            ("Depressão", "Depressão"),
            ("Ansiedade", "Ansiedade"),
            ("Artrite Reumatóide", "Artrite Reumatóide"),
            ("Insuficiência Cardíaca", "Insuficiência Cardíaca"),
            ("Doença Renal Crônica", "Doença Renal Crônica"),
            ("Hepatite", "Hepatite"),
            ("Doença de Alzheimer", "Doença de Alzheimer"),
            ("Parkinson", "Parkinson"),
            ("Osteoporose", "Osteoporose"),
            ("Epilepsia", "Epilepsia"),
            ("Doenças da Tireoide", "Doenças da Tireoide"),
            ("Doença Inflamatória Intestinal", "Doença Inflamatória Intestinal"),
            ("Esclerose Múltipla", "Esclerose Múltipla"),
            ("Psoríase", "Psoríase"),
            ("Hiperlipidemia", "Hiperlipidemia"),
            ("Obesidade", "Obesidade"),
        ],
        widget=forms.SelectMultiple(attrs={"class": "form-control select2", "id": "id_doencas_cronicas"}),
        label="Doenças Crônicas",
        required=False,
    )

    def clean_birth_date_field(self):
        birth_date = self.cleaned_data["birth_date_field"]
        age = datetime.now().year - birth_date.year
        if age < 18:
            raise forms.ValidationError('O paciente deve ter mais de 18 anos de idade.')
        return birth_date
    
    def save(self, commit=True):
        self.instance.birth_date = self.cleaned_data["birth_date_field"]
        self.instance.doencas_cronicas = ", ".join(self.cleaned_data["doencas_cronicas"])
        self.instance.medicamentos = ", ".join(self.cleaned_data["medicamentos"])  # Salva como string separada por vírgulas
        return super().save(commit)
        
    class Meta:
        model = Paciente
        exclude = ("user", "birth_date")
        fields = (
            "phone_number",
            "first_name",
            "last_name",
            "email",
            "cpf",
            "rg",
            "address",
            "estado_civil",
            "genero",
            "nome_responsavel",
            "telefone_responsavel",
            "grau_parentesco",
            "doencas_cronicas",
            "alergias",
            "medicamentos",
            "cirurgias",
            "historico_internacoes",
            "condicoes_cognitivas",
            "alteracoes_humor",
            "comportamento_social",
        )
        labels = {
            "nome_responsavel": "Nome do Responsável",
            "telefone_responsavel": "Telefone do Responsável",
            "grau_parentesco": "Grau de Parentesco",
            "phone_number": "Telefone",
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "email": "Email",
            "cpf": "CPF",
            "rg": "RG",
            "address": "Endereço",
            "estado_civil": "Estado Civil",
            "genero": "Gênero",
            "doencas_cronicas": "Doenças Crônicas",
            "alergias": "Alergias",
            "medicamentos": "Medicamentos",
            "cirurgias": "Cirurgias",
            "historico_internacoes": "Histórico de Internações",
            "condicoes_cognitivas": "Condições Cognitivas",
            "alteracoes_humor": "Alterações no Humor",
            "comportamento_social": "Comportamento Social",
        }
        
        widget = {  # Adiciona os widgets no Meta
        "birth_date": forms.SelectDateWidget(attrs={"class": "form-control", "type": "date"}),
        "phone_number": forms.TextInput(attrs={"class": "form-control", "type": "tel"}),
        "first_name": forms.TextInput(attrs={"class": "form-control"}),
        "last_name": forms.TextInput(attrs={"class": "form-control"}),
        "email": forms.EmailInput(attrs={"class": "form-control"}),
        "cpf": forms.TextInput(attrs={"class": "form-control"}),
        "rg": forms.TextInput(attrs={"class": "form-control"}),
        "address": forms.TextInput(attrs={"class": "form-control"}),
        "estado_civil": forms.Select(attrs={"class": "form-control"}),
        "genero": forms.Select(attrs={"class": "form-control"}),
        "nome_responsavel": forms.TextInput(attrs={"class": "form-control"}),
        "telefone_responsavel": forms.TextInput(attrs={"class": "form-control", "type": "tel"}),
        "grau_parentesco": forms.Select(attrs={"class": "form-control"}),
        "doencas_cronicas": forms.SelectMultiple(attrs={"class": "select2"}),  # Select2 aplicado
        "medicamentos": forms.SelectMultiple(attrs={"class": "select2"}),  # Select2 aplicado
        "alergias": forms.TextInput(attrs={"class": "form-control"}),
        "cirurgias": forms.TextInput(attrs={"class": "form-control"}),
        "historico_internacoes": forms.TextInput(attrs={"class": "form-control"}),
        "condicoes_cognitivas": forms.TextInput(attrs={"class": "form-control"}),
        "alteracoes_humor": forms.TextInput(attrs={"class": "form-control"}),
        "comportamento_social": forms.TextInput(attrs={"class": "form-control"}),
        }
