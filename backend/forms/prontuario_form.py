from django import forms
from backend.models.prontuario_model import Prontuario

class ProntuarioForm(forms.ModelForm):
    MEDICAMENTOS_OPCOES = [
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
    ]

    medicamentos_aplicados = forms.MultipleChoiceField(
        choices=MEDICAMENTOS_OPCOES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),  # Caixa de seleção múltipla
        required=False,
    )

    class Meta:
        model = Prontuario
        fields = ['paciente', 'medico', 'horario', 'medicamentos_aplicados', 
                  'pressao_arterial', 'temperatura', "frequencia_cardiaca",
            "frequencia_respiratoria",
            "saturacao_oxigenio",
            "glicemia", 'observacoes']
        widgets = {
            'horario': forms.TimeInput(attrs={'type': 'time'}),  # Input de horário
            "medicamentos_aplicados": forms.SelectMultiple(attrs={"class": "select2"}),
            "pressao_arterial": forms.Select(attrs={"class": "select2"}),
            "temperatura": forms.Select(attrs={"class": "select2"}),
            "frequencia_cardiaca": forms.Select(attrs={"class": "select2"}),
            "frequencia_respiratoria": forms.Select(attrs={"class": "select2"}),
            "saturacao_oxigenio": forms.Select(attrs={"class": "select2"}),
            "glicemia": forms.Select(attrs={"class": "select2"}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
        'paciente': 'Paciente',
        'medico': 'Médico',
        'horario': 'Horário',
        'medicamentos_aplicados': 'Medicamentos Aplicados',
        'pressao_arterial': 'Pressão Arterial',
        'temperatura': 'Temperatura',
        'frequencia_cardiaca': 'Frequência Cardíaca',
        'frequencia_respiratoria': 'Frequência Respiratória',
        'saturacao_oxigenio': 'Saturação Oxigênio',
        'glicemia': 'Glicemia',
        'observacoes': 'Observações',
        }

    def clean_medicamentos_aplicados(self):
        # Combina os medicamentos selecionados em uma string separada por vírgulas
        medicamentos = self.cleaned_data.get('medicamentos_aplicados', [])
        return ", ".join(medicamentos)
