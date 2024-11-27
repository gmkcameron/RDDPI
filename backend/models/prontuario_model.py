from django.db import models
from backend.models.medico_model import Medico
from backend.models.paciente_model import Paciente

class Prontuario(models.Model):
    # Relacionamentos
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    
    # Dados do Registro
    data_consulta = models.DateField(auto_now_add=True)
    horario = models.TimeField()  # Campo para o horário do prontuário

    # Escolhas para Medicamentos
    medicamentos_aplicados = models.TextField(blank=True, null=True)

    # Escolhas para Pressão Arterial
    PRESSAO_OPCOES = [
        ("Selecione uma opção", "Selecione uma opção"),
        ("120/80", "120/80 mmHg (Normal)"),
        ("130/85", "130/85 mmHg (Normal Alta)"),
        ("140/90", "140/90 mmHg (Hipertensão Grau 1)"),
        ("160/100", "160/100 mmHg (Hipertensão Grau 2)"),
        ("180/110", "180/110 mmHg (Hipertensão Grau 3)"),
        ("<90/<60", "Menor que 90/60 mmHg (Hipotensão)"),
    ]
    pressao_arterial = models.CharField(max_length=20, choices=PRESSAO_OPCOES, default="Selecione uma opção")

    # Escolhas para Temperatura
    TEMPERATURA_OPCOES = [
        ("Selecione uma opção", "Selecione uma opção"),
        ("36.0", "36.0 °C (Normal)"),
        ("37.0", "37.0 °C (Febril Leve)"),
        ("38.0", "38.0 °C (Febre)"),
        ("39.0", "39.0 °C (Febre Alta)"),
        ("40.0", "40.0 °C (Hipertermia Grave)"),
        ("<35.0", "<35.0 °C (Hipotermia)"),
    ]
    temperatura = models.CharField(max_length=20, choices=TEMPERATURA_OPCOES, default="Selecione uma opção")

    # Sinais Vitais
    FREQUENCIA_CARDIACA_OPCOES = [
        ("Selecione uma opção", "Selecione uma opção"),
        ("60-100", "60-100 bpm (Normal)"),
        ("<60", "Menor que 60 bpm (Bradicardia)"),
        (">100", "Maior que 100 bpm (Taquicardia)"),
    ]
    frequencia_cardiaca = models.CharField(
        max_length=50,
        choices=FREQUENCIA_CARDIACA_OPCOES,
        default="Selecione uma opção",
    )

    FREQUENCIA_RESPIRATORIA_OPCOES = [
        ("Selecione uma opção", "Selecione uma opção"),
        ("12-20", "12-20 rpm (Normal)"),
        ("<12", "Menor que 12 rpm (Bradipneia)"),
        (">20", "Maior que 20 rpm (Taquipneia)"),
    ]
    frequencia_respiratoria = models.CharField(
        max_length=50,
        choices=FREQUENCIA_RESPIRATORIA_OPCOES,
        default="Selecione uma opção",
    )

    SATURACAO_OXIGENIO_OPCOES = [
        ("Selecione uma opção", "Selecione uma opção"),
        ("95-100", "95-100% (Normal)"),
        ("90-94", "90-94% (Leve Hipóxia)"),
        ("<90", "Menor que 90% (Hipóxia Grave)"),
    ]
    saturacao_oxigenio = models.CharField(
        max_length=50,
        choices=SATURACAO_OXIGENIO_OPCOES,
        default="Selecione uma opção",
    )

    GLICEMIA_OPCOES = [
        ("Selecione uma opção", "Selecione uma opção"),
        ("70-99", "70-99 mg/dL (Normal)"),
        ("100-125", "100-125 mg/dL (Pré-diabetes)"),
        (">126", "Maior que 126 mg/dL (Diabetes)"),
        ("<70", "Menor que 70 mg/dL (Hipoglicemia)"),
    ]
    glicemia = models.CharField(
        max_length=50,
        choices=GLICEMIA_OPCOES,
        default="Selecione uma opção",
    )


    # Observações
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Prontuário de {self.paciente} - {self.data_consulta} - {self.horario}"
