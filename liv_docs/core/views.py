from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import re
import pdfplumber
from PyPDF2 import PdfReader

@login_required(login_url='/login/')
def home(request):
     return render(request, 'index.html')

@login_required(login_url='/login/')
def white(request):
     return render(request, 'white.html')

@login_required(login_url='/login/')
def sucafina(request):
     return render(request, 'sucafina.html')

@login_required(login_url='/login/')
def sucden_pd(request):
     return render(request, 'sucden_pd.html')

@login_required(login_url='/login/')
def sucden_rs(request):
     return render(request, 'sucden_rs.html')

@login_required(login_url='/login/')
def veloso(request):
     return render(request, 'veloso.html')

@login_required(login_url='/login/')
def mercon(request):
     return render(request, 'mercon.html')

def login_user(request):
    return render(request, 'login.html')

def index(request):
    return redirect('/home/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def upload_procafe_pdf(request, client_name):
    if request.method == 'POST' and request.FILES['procafe_pdf']:
        procafe_pdf = request.FILES['procafe_pdf']
        fs = FileSystemStorage()
        fs.save(procafe_pdf.name, procafe_pdf)

        # Adicione aqui a lógica específica do cliente, se necessário

        return HttpResponse('Procafé PDF enviado com sucesso.')

    return render(request, f'{client_name}.html')

# Função para processar PDFs
def processar_pdf(arquivo_pdf):
    texto = ""
    try:
        pdf_leitor = PdfReader(arquivo_pdf)
        for pagina_numero in range(len(pdf_leitor.pages)):
            pagina = pdf_leitor.pages[pagina_numero]
            texto += pagina.extract_text()
    except Exception as e:
        texto = f"Erro ao processar o PDF: {str(e)}"

    return texto

# Função para processar arquivos Procafe e Sucafina
@login_required(login_url='/login/')
def processar_sucafina(request):
    if request.method == 'POST':
        arq_procafe = request.FILES['arq_procafe']
        arq_sucafina = request.FILES['arq_sucafina']

        procafe_texto = processar_pdf(arq_procafe)
        sucafina_texto = processar_pdf(arq_sucafina)

        print(f"Texto do Procafé: {procafe_texto}")
        print(f"Texto do Sucafina: {sucafina_texto}")

        return render(request, 'sucafina.html', {'procafe_texto': procafe_texto, 'sucafina_texto': sucafina_texto})

    return render(request, 'sucafina.html')

# Função para processar arquivos Procafe e Sucden_RS
@login_required(login_url='/login/')
def processar_sucden_rs(request):
    if request.method == 'POST':
        arq_procafe = request.FILES['arq_procafe']
        arq_sucden_rs = request.FILES['arq_sucden_rs']

        procafe_texto = processar_pdf(arq_procafe)
        sucden_rs_texto = processar_pdf(arq_sucden_rs)

        print(f"Texto do Procafé: {procafe_texto}")
        print(f"Texto do Sucden_RS: {sucden_rs_texto}")

        return render(request, 'sucden_rs.html', {'procafe_texto': procafe_texto, 'sucden_rs_texto': sucden_rs_texto})

    return render(request, 'sucden_rs.html')

# Função para processar arquivos Procafe e Sucden_PD
@login_required(login_url='/login/')
def processar_sucden_pd(request):
    if request.method == 'POST':
        arq_procafe = request.FILES['arq_procafe']
        arq_sucden_pd = request.FILES['arq_sucden_pd']

        procafe_texto = processar_pdf(arq_procafe)
        sucden_pd_texto = processar_pdf(arq_sucden_pd)

        print(f"Texto do Procafé: {procafe_texto}")
        print(f"Texto do Sucden_PD: {sucden_pd_texto}")

        return render(request, 'sucden_pd.html', {'procafe_texto': procafe_texto, 'sucden_pd_texto': sucden_pd_texto})

    return render(request, 'sucden_pd.html')

# Função para processar arquivos Procafe e Veloso
@login_required(login_url='/login/')
def processar_veloso(request):
    if request.method == 'POST':
        arq_procafe = request.FILES['arq_procafe']
        arq_veloso = request.FILES['arq_veloso']

        procafe_texto = processar_pdf(arq_procafe)
        veloso_texto = processar_pdf(arq_veloso)

        print(f"Texto do Procafé: {procafe_texto}")
        print(f"Texto do Veloso: {veloso_texto}")

        return render(request, 'veloso.html', {'procafe_texto': procafe_texto, 'veloso_texto': veloso_texto})

    return render(request, 'veloso.html')

# Função para processar arquivos Procafe e White
@login_required(login_url='/login/')
def processar_white(request):
    if request.method == 'POST':
        arq_procafe = request.FILES['arq_procafe']
        arq_white = request.FILES['arq_white']

        procafe_texto = processar_pdf(arq_procafe)
        white_texto = processar_pdf(arq_white)

        print(f"Texto do Procafé: {procafe_texto}")
        print(f"Texto do White: {white_texto}")

        return render(request, 'white.html', {'procafe_texto': procafe_texto, 'white_texto': white_texto})

    return render(request, 'white.html')

# Função para processar arquivos Procafe e Mercon
@login_required(login_url='/login/')
def processar_mercon(request):
    if request.method == 'POST':
        arq_procafe = request.FILES['arq_procafe']
        arq_mercon = request.FILES['arq_mercon']

        procafe_texto = processar_pdf(arq_procafe)
        mercon_texto = processar_pdf(arq_mercon)

        print(f"Texto do Procafé: {procafe_texto}")
        print(f"Texto do Mercon: {mercon_texto}")

        return render(request, 'mercon.html', {'procafe_texto': procafe_texto, 'mercon_texto': mercon_texto})

    return render(request, 'mercon.html')