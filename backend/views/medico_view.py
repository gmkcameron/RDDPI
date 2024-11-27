from django.shortcuts import render
from backend.forms.medico_form import MedicoForm
from backend.forms.user_form import UserForm
from backend.models.medico_model import Medico
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render


@login_required
def medico_delete(request, id):
    try:
        medico = Medico.objects.get(pk=id)
        medico.delete()
        messages.success(request, "Médico excluído com sucesso!")
    except Medico.DoesNotExist:
        messages.error(request, "Médico não encontrado.")
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao excluir o médico: {str(e)}")
    return redirect('medico_list')

@login_required
def medico_list(request):
    medicos = Medico.objects.prefetch_related('especialidades').all()
    return render(request, 'medico/medico_list.html', {'medicos': medicos})

@login_required
def medico_create(request):

    if request.method == 'POST':
        user_form_instance = UserForm(request.POST)
        medico_form_instance = MedicoForm(request.POST)
        forms = [
            user_form_instance,
            medico_form_instance
        ]
        
        for form in forms:
            if not form.is_valid():
                messages.add_message(request, messages.ERROR, form.errors.as_text())     
                return redirect('medico_create', {'forms': forms})

        new_user = user_form_instance.save()
        new_medico = medico_form_instance.save(commit=False)
        new_medico.user = new_user
        new_medico.save()
        messages.add_message(request, messages.SUCCESS, "Medico salvo com sucesso!")
        return redirect("medico_list")
    
    context = {
        'forms' : [
            UserForm(),
            MedicoForm()
        ], 
    }
    return render(request, 'medico/medico_create.html', context)

@login_required
def medico_detail(request, id):
    try:
        medico = Medico.objects.get(pk=id)
    except Medico.DoesNotExist:
        messages.add_message(request, messages.ERROR, "Médico não encontrado.")
        return redirect('medico_list')
    except Exception as e:
        messages.add_message(request, messages.ERROR, f"Ocorreu um erro ao carregar o médico: {str(e)}")
        return redirect('medico_list')
    return render(request, 'medico/medico_detail.html', {'medico': medico})

@login_required
def medico_update(request, id):
    medico = Medico.objects.get(pk=id)
    
    if request.method == 'POST':
        medico_form_instance = MedicoForm(request.POST, instance=medico)
        
        if not medico_form_instance.is_valid():
            messages.add_message(request, messages.ERROR, medico_form_instance.errors.as_text())
            return render(request, 'medico/medico_update.html', {'form': medico_form_instance})
        
        medico_form_instance.save()
        messages.add_message(request, messages.SUCCESS, "Médico salvo com sucesso!")
        return redirect("medico_list")
    
    form = MedicoForm(instance=medico)
    
    return render(request, 'medico/medico_update.html', {'form': form, 'birth_date': medico.birth_date.isoformat()})
    