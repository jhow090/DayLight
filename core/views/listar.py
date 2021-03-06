from django.shortcuts import render
from core.forms import *
from core.models import *


def list_usuario(request):
    template = "gerencial/gerenciarusuario.html"
    if request.method == 'POST':
        search = request.POST.get('nome_usuario')
        lista_usuario = Usuario.objects.filter(nome__contains=search)
        if search == "":
            search = request.POST.get('email_usuario')
            lista_usuario = Usuario.objects.filter(email__contains=search)
            if search == "":
                search = request.POST.get('cpf_usuario')
                lista_usuario = Usuario.objects.filter(cpf=search)
                if search == "":
                    return render(request, template)
        return render(request, template, {'lista_usuario':lista_usuario})
    else:
        return render(request, template)


def list_cliente(request):
    template = "comercial/gerenciarcliente.html"
    if request.method == 'POST':
        search = request.POST.get('nome_cliente')
        lista_cliente = Cliente.objects.filter(clientename__contains=search)
        if search == "":
            search = request.POST.get('email_cliente')
            lista_cliente = Cliente.objects.filter(email__contains=search)
            if search == "":
                search = request.POST.get('cpf/cnpj_cliente')
                lista_cliente = Cliente.objects.filter(numero_fiscal=search)
                if search == "":
                    return render(request, template)
        return render(request, template, {'lista_cliente':lista_cliente})
    else:
        return render(request, template)
   

def list_fornecedor(request):
    template = "comercial/gerenciarfornecedor.html"
    if request.method == 'POST':
        search = request.POST.get('nome_fornecedor')
        lista_fornecedor = Fornecedor.objects.filter(fornecedorname__contains=search)
        if search == "":
            search = request.POST.get('email_fornecedor')
            lista_fornecedor = Fornecedor.objects.filter(email__contains=search)
            if search == "":
                search = request.POST.get('cpf/cnpj_fornecedor')
                lista_fornecedor = Fornecedor.objects.filter(numero_fiscal=search)
                if search == "":
                    return render(request, template)
        return render(request, template, {'lista_fornecedor':lista_fornecedor})
    else:
        return render(request, template)


def list_prestador(request):
    template = "producao/gerenciarprestador.html"
    if request.method == 'POST':
        search = request.POST.get('nome_prestador')
        lista_prestador = PrestadorServico.objects.filter(prestadorname__contains=search)
        if search == "":
            search = request.POST.get('email_prestador')
            lista_prestador = PrestadorServico.objects.filter(email__contains=search)
            if search == "":
                search = request.POST.get('cpf/cnpj_prestador')
                lista_prestador = PrestadorServico.objects.filter(numero_fiscal=search)
                if search == "":
                    return render(request, template)
        return render(request, template, {'lista_prestador':lista_prestador})
    else:
        return render(request, template)


def list_material(request):
    template = "comercial/gerenciarmaterial.html"
    if request.method == 'POST':
        search = request.POST.get('cod_material')
        lista_material = Material.objects.filter(cod_mprima=search)
        if search == "":
            search = request.POST.get('tipo_material')
            lista_material = Material.objects.filter(tipo_mprima__contains=search)
            if search == "":
                search = request.POST.get('fabricante')
                lista_material = Material.objects.filter(nome_fabricante__contains=search)
                if search == "":
                    search = request.POST.get('desc_material')
                    lista_material = Material.objects.filter(material__contains=search)
                    if search == "":
                        return render(request, template)
        return render(request, template, {'lista_material':lista_material})
    else:
        return render(request, template)


def list_produto(request):
    template = "comercial/gerenciarproduto.html"
    if request.method == 'POST':
        search = request.POST.get('tipo_produto')
        lista_produto = Produto.objects.filter(tipo_produto__contains=search)
        if search == "":
            search = request.POST.get('classificacao_produto')
            lista_produto = Produto.objects.filter(classificacao__contains=search)
            if search == "":
                search = request.POST.get('desc_produto')
                lista_produto = Produto.objects.filter(produto__contains=search)
                if search == "":
                    return render(request, template)
        return render(request, template, {'lista_produto':lista_produto})
    else:
        return render(request, template)


def list_servico(request):
    template = "producao/gerenciarservico.html"
    if request.method == 'POST':
        search = request.POST.get('tipo_servico')
        lista_servico = Servico.objects.filter(tipo_servico=search)
        if search == "--Selecione--":
            search = request.POST.get('servico')
            lista_servico = Servico.objects.filter(servico=search)
            if search == "--Selecione--":
                return render(request, template)
        return render(request, template, {'lista_servico':lista_servico})
    else:
        return render(request, template)