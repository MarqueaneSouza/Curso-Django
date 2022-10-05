from django.shortcuts import render


# from pypro.modulos import facade #noqa


def home(request):
    # return render(request, 'base/login.html', {'MODULOS': facade.listar_modulos_ordenados()}) comentado porque #noqa
    # estava dando erro na página principal da aplicação: TemplateDoesNotExist #noqa
    return render(request, 'base/home.html', {})
