from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now

from backend.forms.prontuario_form import ProntuarioForm
from backend.models.prontuario_model import Prontuario


@login_required
def prontuario_list(request):
    prontuarios = Prontuario.objects.all()
    return render(request, 'prontuario/prontuario_list.html', {'prontuarios': prontuarios})


@login_required
def prontuario_create(request):
    if request.method == 'POST':
        form = ProntuarioForm(request.POST)
        if form.is_valid():
            prontuario = form.save(commit=False)
            prontuario.data_consulta = now().date()  
            prontuario.save()
            messages.success(request, "Prontuário criado com sucesso!")
            return redirect('prontuario_list')
        else:
            messages.error(request, "Erro ao criar prontuário. Verifique os campos.")
    else:
        form = ProntuarioForm()
    return render(request, 'prontuario/prontuario_create.html', {'form': form})


@login_required
def prontuario_detail(request, id):
    prontuario = get_object_or_404(Prontuario, id=id)
    return render(request, 'prontuario/prontuario_detail.html', {'prontuario': prontuario})


@login_required
def prontuario_update(request, id):
    prontuario = get_object_or_404(Prontuario, id=id)
    
    if request.method == 'POST':
        prontuario_form_instance = ProntuarioForm(request.POST, instance=prontuario)
        
        if prontuario_form_instance.is_valid():
            prontuario_form_instance.save()
            messages.add_message(request, messages.SUCCESS, "Prontuário atualizado com sucesso!")
            return redirect("prontuario_list")  # Redireciona para a lista após salvar
        else:
            messages.add_message(request, messages.ERROR, "Erros encontrados no formulário.")
    
    # Renderiza o formulário com erros ou para a edição inicial
    context = {
        'form': ProntuarioForm(instance=prontuario),
        'prontuario': prontuario,
    }
    return render(request, 'prontuario/prontuario_update.html', context)


@login_required
def prontuario_delete(request, id):
    prontuario = get_object_or_404(Prontuario, id=id)
    
    if request.method == 'POST':
        prontuario.delete()
        messages.add_message(request, messages.SUCCESS, "Prontuário excluído com sucesso!")
        return redirect("prontuario_list")
    
    return render(request, 'prontuario/prontuario_confirm_delete.html', {'prontuario': prontuario})
