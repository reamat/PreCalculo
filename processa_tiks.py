import sys
import os
import datetime
import subprocess


template_tiks = rb"""
% Arquivo de origem: ___ORIGEM___
% Arquivo de destino: ___DESTINO___
% Processamento: ___PROCESSAMENTO___
\documentclass[crop,tikz,convert=pdf2svg]{standalone}
\usetikzlibrary{fit,shapes.geometric,arrows} 
\begin{document}
___CODIGO_TIKS___
\end{document}
"""

def processa_arquivo(nome_tex, nome_saida, N_inicial):
    """nome_tex: arquivo tex a ser lido
       nome_saida: arquivo tex a ser criado"""
    caminho_base = os.path.dirname(nome_tex)
    caminho_destino = os.path.join(caminho_base, "figs/tikz/")
    nome_base = "figura_" + os.path.basename(nome_tex) #.replace(r'.', '_')
    nome_base = nome_base[ : nome_base.find(r'.')]
    os.makedirs(caminho_destino, exist_ok=True) # cria o diretório caso não exista.

    with open(nome_tex, "rb") as f:
        conteudo = f.read()
    
    tag_i = rb"\begin{tikzpicture}"
    tag_f = rb"\end{tikzpicture}"
    while (tag_i in conteudo):
        pos_i = conteudo.find(tag_i)
        pos_f = conteudo.find(tag_f) + len(tag_f)
        codigo_imagem = conteudo[pos_i : pos_f]
        nome_tikz = escolhe_nome(caminho_destino, nome_base, N_inicial)
        nome_tikz_sem_extensao = nome_tikz.replace(r".tex", '')
        include = f"\includegraphics{{{nome_tikz_sem_extensao}}}".encode()
        conteudo = conteudo.replace(codigo_imagem, include)
        processa_tikz(codigo_imagem, nome_tex, nome_tikz)

    with open(nome_saida, "wb") as f:
        f.write(conteudo)
   

def escolhe_nome(caminho_destino, nome_base, N):
    """Escolhe um nome livre para salvar"""
    prefixo_nome = os.path.join(caminho_destino, nome_base) 
    
    while True:
        nome = prefixo_nome + f"_{N}.tex" 
        if not os.path.exists(nome):
            break
        else:
            N += 1
    return nome


def processa_tikz(codigo, nome_tex, nome_tikz):
    conteudo = template_tiks.replace(rb"___CODIGO_TIKS___", codigo)\
                            .replace(rb"___ORIGEM___", nome_tex.encode())\
                            .replace(rb"___DESTINO___", nome_tikz.encode())\
                            .replace(rb"___PROCESSAMENTO___", 
                                  datetime.datetime.now().strftime("%x - %X")\
                                                         .encode())
    print("Criando arquivo", nome_tikz)
    with open(nome_tikz, 'wb') as f:
        f.write(conteudo)
    
    
    nome_completo = os.path.abspath(nome_tikz)
    # print(nome_completo)
    cwd = os.path.dirname(nome_completo)
    subprocess.run(["latex", nome_completo], cwd=cwd)
    subprocess.run(["dvisvgm", nome_completo.replace(".tex", ".dvi")]
                             , cwd=cwd)



if len(sys.argv)<2:
    print("Indique o nome do arquivo tex")
    quit()

nome_tex = sys.argv[1]

processa_arquivo(nome_tex, "saida.tex", 1)
