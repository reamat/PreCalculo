# Folha de estilo

Este documento contém informações sobre os padrões de estilo de escrita e organização dos livros colaborativos do projeto REAMAT. Antes de submeter uma colaboração, verifique que seu trabalho está de acordo com os pontos observados nesta folha de estilo.

Estamos muito mais interessados em melhorar o conteúdo dos livros (tando em qualidade como em quantidade) e menos interessados em melhorar a sua estética. Portanto, busque manter o código LaTeX o mais simples possível buscando potencializar a colaboração de outras pessoas e de forma a se obter um resultado que permita uma leitura objetiva e agradável do livro.

Qualquer dúvida, poste no nosso fórum https://www.ufrgs.br/reamat/forum.html, crie um _issue_ no repositório do livro ou escreva para reamat@ufrgs.br.

## Regionalização e estilo de escrita

Os livros estão escritos em língua portuguesa, seguindo os costumes linguísticos brasileiros. Dá-se prioridade à ortografia prevista no Acordo Ortográfico de 1990.

### Capitalização

Deve-se usar maiúscula apenas em nomes próprios, ex: método de Newton, métodos dos mínimos quadrados, teorema de Liouville, método de Euler implícito.

O uso de maiúsculas e minúsculas nos títulos (de capítulos, seções etc) segue a mesma regra do corpo do texto.

Em referências internas, como a teoremas, lemas e exercícios, usa-se maiúscula inicial, seguido de (~) tilde e o comando de referencia:

	Seguindo o Teorema~\ref{teo:rótulo_do_teorema}.

## Código fonte LaTeX

Os livros estão escritos em [LaTex](https://latex-project.org/) e os arquivos estão em `charset=utf-8`.

O arquivo principal `main.tex` encontra-se no diretório principal do livro no repositório do mesmo. O código LaTeX de cada capítulo encontra-se em um subdiretório específico com nome `cap_abrev`, onde `abrev` é uma abreviação que lembre o conteúdo do capítulo. Por sua vez, o arquivo `cap_abrev.tex` contém o código LaTeX referente a este capítulo.

Para informações sobre como compilar o código fonte, leia o arquivo `README.md`.

### Compatibilidade

O código LaTeX do livro deve permitir sua compilação tanto com `latex` como com `pdflatex`, além de permitir a compilação no formato HTML. Ao adicionar suas colaborações, certifique-se que elas são compatíveis testando a compilação definida no `Makefile`. Para mais informações sobre a compilação dos materiais disponíveis, consulte o README.md no repositório GitHub do recurso de seu interesse.

#### Instruções LaTeX não compatíveis

Fazemos a conversão do livro de código LaTeX para HTML usando o pacote [TeX4ht](https://www.tug.org/tex4ht/). Os ambientes matemáticos são convertidos para [MathMl](https://www.w3.org/Math/) e então renderizados usando [MathJax](https://www.mathjax.org/). Para que a conversão funcione de forma apropriada deve-se observar as seguintes questões:

* Não usar o ambiente `align`: no lugar use o ambiente `eqnarray` ou o `split` dentro de um ambiente `equation`.

* Não usar as sintaxes `\[ \]` e `$$ $$`, no lugar use o ambiente `equation`.

* Não usar `array` para composição de tabelas. A alternativa é usar o ambiente `tabular`, por exemplo:

		\begin{center}
			\begin{tabular}{r|c|c}
				$h$ & $Df(1)$ & $|f'(1) - D_{+,h}F(1)|$ \\ \hline
				$10^{-1}$ & $-8,67062\E-01$ & $2,55909\E-02$\\
				$10^{-2}$ & $-8,44158\E-01$ & $2,68746\E-03$\\
				$10^{-14}$ & $-8,43769\E-01$ & $2,29851\E-03$ \\\hline
			\end{tabular}
		\end{center}

* Não colocar `label` dentro de colchetes ou chaves.

### Capítulos

Dentro de cada subdiretório de um capítulo, por exemplo  `cap_foo`, devem estar presentes todos os arquivos referentes ao texto deste. As imagens devem ser colocadas no subdiretório `cap_foo/figs`. De preferência, deve-se criar um subdiretório para cada figura. Quando possível, as figuras devem ser acompanhadas de seu código fonte.

### Figuras

Os arquivos das figuras devem ser fornecidos em formato `EPS` e `PNG` sendo armazenados no subdiretório `cap_foo/figs`, onde `cap_foo` é o diretório do capítulo que a figura pertence. As figuras devem ser fornecidas no tamanho desejado para o livro, i.e. evite definir o tamanho da figura no código LaTeX. Para uma vizualização conformável em celulares, recomendamos que a figura tenha largura inferior a 320px.

A inclusão de uma figura no código LaTex deve ser feita da seguinte forma:

    \begin{figure}
        \centering
	    \includegraphics{cap_foo/figs/picfoo}
		\caption{Descrição da figura figfoo.}
		\label{fig:figfoo}
	\end{figure}

Não insira figuras dentro de outros ambientes como, por exemplo, `ex`, `teo`, `sol` e outros.

Sempre que possível, forneça o código fonte da figura armazenando-o na pasta `cap_foo/figs/figfoo`. Nesta mesma pasta, crie um arquivo README.md com uma descrição da figura e a linceça da mesma, a qual deve ser compatível com a CC-BY-SA 3.0.

### Equações e símbolos matemáticos

As equações e símbolos matemáticos estão escritos usando a coleção de pacotes [AMS-LaTeX](http://www.ams.org/publications/authors/tex/amslatex).

A fim de facilitar a discussão sobre o material do livro, **todas as equações devem ser numeradas**.

#### Uso da vírgula

Os livros usam o pacote LaTeX [`icomma`](https://www.ctan.org/pkg/icomma). Desta forma, para que um espaço apareça após uma vírgula é necessário por o espaço no código LaTeX. Por exemplo, o código LaTeX `$1,24$` produz o número 1,24, enquanto o código `$1, 24$` produz os números 1 e 24 separados por uma vírgula e um espaço.

#### Números em notação científica

Números em notação científica podem ser representados, tando usando `$\times 10^$` como usando o macro `\E`, por exemplo:

    $1,25673\times 10^{-13} = 1,25673\E-13.$

#### Subíndices e superíndices

Entradas de vetores e matrizes devem ser indicadas com subíndices:

    $v = (v_1, v_2, v_3).$

O uso dos parênteses denota um vetor coluna, i.e.

    $v = (v_1, v_2, v_3) = [v_1 v_2 v_3]^T.$

Processos iterativos devem ser indicados com superíndices:

    $x^{(n+1)} = x^{(n)} + \frac{1}{n}.$

### Exercícios

Os livros podem contar com três tipos de exercícios, os intitulados "Exercícios resolvidos", "Exercícios" e "Exercícios finais". Recomenda-se que cada seção do livro conte com uma subseção de exercícios resolvidos seguida de outra com exercícios.

#### Exercícios resolvidos

Exercícios resolvidos são exercícios com resolução completa. Eles devem ser colocados em subseção da seção a que se referem. A subseção deve ser não numerada e intitulada "Exercícios Resolvidos" , i.e.:

    \subsection*{Exercícios resolvidos}

O enunciado de um exercício resolvido  deve ser colocado dentro de um ambiente `exeresol` como, por exemplo:

    \begin{exeresol}
	    Escreva aqui o enunciado do exercício resolvido.
    \end{exersol}

A resolução do exercício deve ser colocada dentro de um ambiente `resol`, colocado logo abaixo do `\end{exeresol}`, por exemplo:

    \begin{resol}
	    Escreva aqui a resolução completa (detalhada) do exercício.
	\end{resol}
		
No caso de livros com apenas exercícios no final de capítulo, em vez de subseção não numerada usar seção numerada, i.e.:

	\section{Exercícios resolvidos}
		
#### Exercícios

Exercícios com resposta ou sem devem ser colocados em subseção da seção a que se referem. A subseção deve ser não numerada e intitulada "Exercícios", i.e.:

    \subsection*{Exercícios}

O enunciado de um exercício com resposta ou sem deve ser colocado dentro de um ambiente `exer` como, por exemplo:

    \begin{exer}
	   Escreva aqui o enunciado do exercício com resposta ou sem.
    \end{exer}

Caso o exercício tenha resposta (para resolução completa, veja a subsecção Exercícios resolvidos) ela deve ser colocada em um ambiente `resp` logo abaixo do ambiente ao qual o exercício se refere como, por exemplo:

    \begin{resp}
	   Escreva aqui a resposta do exercício.
    \end{resp}

No caso de livros com apenas exercícios no final de capítulo, em vez de subseção não numerada usar seção numerada, i.e.:

	\section{Exercícios}

#### Exercícios finais

Exercícios finais constituem uma seção contendo a lista de exercícios (com resposta ou sem) de final de capítulo. A seção dever numerada e intitulada "Exercícios finais", i.e.:

    \section{Exercícios finais}

O enunciado de cada exercícios deve ser colocado dentro de um ambiente `exer` como, por exemplo:

    \begin{exer}
	   Escreva aqui o enunciado do exercício com resposta ou sem.
    \end{exer}

No caso do exercícios ter resposta indicada, esta deve ser colocada dentro de um ambiente `resp` como, por exemplo:

    \begin{resp}
	   Escreva aqui a resposta do exercício.
    \end{resp}

Esta estrutura de exercícios não é recomendada para livros com apenas exercícios no final de capítulo.

### Inserção de códigos computacionais

Salvo livros com objetivo específico em alguma linguagem computacional, eles devem ser versáteis o suficiente para não depender de qualquer linguagem e/ou pacote computacional em específico. Para tanto, textos envolvendo algum pacote (ou alguma linguagem) computacional devem ser encapsulados dentro de uma declaração `se ... então`. Os códigos (_scripts_) computacionais devem ser encapsulados em ambiente `verbatim`, por exemplo

	\ifispython
	  \begin{verbatim}
		  print("Olá, mundo!")
	  \end{verbatim}
	\fi

## Convenções anteriores à migração para o REAMAT

Comandos que estou usando:

	\vskip0.3cm
	\colorbox{azul}{
	\begin{minipage}{0.9\linewidth}
	\begin{center}
	texto
	\end{center}
	\end{minipage}}
	\vskip0.3cm


	\begin{table}[H]
	\centering
	\begin{tabular}{|c|c|c|c|} \hline
	\rowcolor{cinza}
	$P$ & $\neg P$ & $\neg (\neg P)$ & $ P \leftrightarrow \neg (\neg P)$\\ \hline
	V & F & V & V \\ \hline
	F & V & F & V \\ \hline
	\end{tabular}
	\end{table}

 Para fazer hiperlink dentro do texto
	
	\label{...}
	\autoref{...}

	\begin{exer}
	\end{exer}

