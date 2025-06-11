from django.shortcuts import render
from django.http import Http404

def index(request):
  return render(request, 'glossario/pages/index.html')

def corpo_humano(request):
  return render (request,'glossario/pages/corpo_humano.html')

def apresentacao(request):
  return render(request, 'glossario/pages/apresentacao.html')

def como_usar(request):
    
    palavras_context = [
        {"id": 1, "palavra": "ORDEM ALFABÉTICA", "significado": "ORGANIZAÇÃO DAS PALAVRAS SEGUINDO AS LETRAS DO ALFABETO (A-Z)", "cor": "azul"},
        {"id": 2, "palavra": "VERBETE", "significado": "PALAVRA OU TERMO DEFINIDO OU EXPLICADO EM UM GLOSSÁRIO OU DICIONÁRIO", "cor": "amarelo"},
        {"id": 3, "palavra": "GÊNERO", "significado": "CATEGORIA GRAMATICAL QUE INDICA SE UMA PALAVRA É MASCULINA, FEMININA OU NEUTRA", "cor": "verde"},
        {"id": 4, "palavra": "DEFINIÇÃO", "significado": "EXPLICAÇÃO CLARA E PRECISA SOBRE O SIGNIFICADO DE UMA PALAVRA OU EXPRESSÃO", "cor": "vermelho"},
        {"id": 5, "palavra": "IMAGEM", "significado": "REPRESENTAÇÃO VISUAL QUE AJUDA A ILUSTRAR OU EXPLICAR O SIGNIFICADO DE UM TERMO", "cor": "azul"},
        {"id": 6, "palavra": "CONTEXTO", "significado": "SITUAÇÃO OU FRASE ONDE A PALAVRA É USADA, AJUDANDO A ENTENDER SEU SIGNIFICADO", "cor": "amarelo"},
        {"id": 7, "palavra": "ÁUDIO", "significado": "ARQUIVO OU GRAVAÇÃO SONORA QUE MOSTRA COMO A PALAVRA É PRONUNCIADA", "cor": "verde"},
        {"id": 8, "palavra": "REMISSÃO", "significado": "INDICAÇÃO QUE DIRECIONA PARA OUTRO TERMO OU PARTE DO GLOSSÁRIO RELACIONADO", "cor": "vermelho"}
    ]

    
    return render(
        request,'glossario/pages/como_usar.html',
        {"palavras_context" : palavras_context}
    )

def palavra(request, id):
    palavra_context = [
        {
            "id": 1,
            "letra": "B",
            "palavra": "BRAÇO",
            "genero": "NOME MASCULINO",
            "imagem": "glossario/img/palavra/braco.jpg",
            "descricao": "MEMBRO DO CORPO QUE LIGA O OMBRO À MÃO.",
            "frase": "EU ESTIQUEI O BRAÇO",
            "remissa": "MEMBRO SUPERIOR"
        },

        {
            "id": 2,
            "letra": "B",
            "palavra": "BOCA",
            "genero": "NOME FEMININO",
            "imagem": "glossario/img/palavra/boca.jpg",
            "descricao": "PARTE DO CORPO QUE USAMOS PARA COMER, FALAR E SORRIR.",
            "frase": "EU TENHO UMA BOCA",
            "remissa": "CAVIDADE BUCAL"
        },
        {
            "id": 3,
            "letra": "C",
            "palavra": "CABEÇA",
            "genero": "NOME FEMININO",
            "imagem": "glossario/img/palavra/cabeca.png",
            "descricao": "PARTE DO CORPO HUMANO QUE CONTÉM OLHOS, ORELHAS, BOCA E NARIZ.",
            "frase": "EU TENHO UMA CABEÇA",
            "remissa": "CRÂNIO"
        },
        
        {
            "id": 4,
            "letra": "M",
            "palavra": "MÃO",
            "genero": " NOME FEMININO",
            "imagem": "glossario/img/palavra/mao.jpg",
            "descricao": "PARTE DO CORPO QUE USAMOS PARA PEGAR E SEGURAR AS COISAS.",
            "frase": "EU LEVANTEI A MÃO",
            "remissa": "MEMBRO SUPERIOR"
        }

        
    ]

    # Localiza a palavra pelo ID
    palavra_atual = next((p for p in palavra_context if p["id"] == id), None)

    if not palavra_atual:
        raise Http404("Palavra não encontrada.")

    # Navegação: anterior e próxima
    ids = [p["id"] for p in palavra_context]
    pos = ids.index(id)
    anterior = ids[pos - 1] if pos > 0 else ids[-1]
    proxima = ids[pos + 1] if pos < len(ids) - 1 else ids[0]

    return render(request, 'glossario/pages/palavra.html', {
        "palavra": palavra_atual,
        "anterior": anterior,
        "proxima": proxima
    })


def autores(request):
    autores_context = [
        {
            "id" : 1,
            "nome" : "TATIANE MENDES FERREIRA",
            "foto": "glossario/img/autores/autor_1.png",
            "funcao": "FUNÇÃO"
        },
        {
            "id" : 2,
            "nome" : "REBEKA DA SILVA AGUIAR",
            "foto": "glossario/img/autores/autor_1.png",
            "funcao": "FUNÇÃO"
        },
        {
            "id" : 3,
            "nome" : "NATHALIA MARIANO LOPES",
            "foto": "glossario/img/autores/autor_1.png",
            "funcao": "DESENVOLVEDORA WEB"
        },
    ]
    
    return render(request, 'glossario/pages/autores.html',{
        "autores" : autores_context
    })

def ficha_tecnica(request):
    
    ficha_tecnica =[
        {
            "universidade" : "UNIVERSIDADE",
            "autor": "TATIANE MENDES FERREIRA",
            "site": "NATHALIA MARIANO LOPES",
            "diagramacao": "NOME PESSOA",
            "info": "PRODUZIDO"
        },
    ]
    
    referencias =[
        {
            "id" : 1,
            "autor": "TATIANE MENDES FERREIRA",
            "site": "NATHALIA MARIANO LOPES",
            "diagramacao": "NOME PESSOA",
            "info": "PRODUZIDO"
        }
    ]
    
    return render(request,'glossario/pages/ficha_tecnica.html',{
        "ficha": ficha_tecnica,
        
    } )
