pdf:
	pdflatex main
	bibtex main
	makeindex main
	pdflatex main
	pdflatex main

.PHONY: clean

clean:
	rm -f *.aux *.bbl *.blg *.lof *.log *.out *.toc
	rm -f Capitulos/*.aux Capitulos/*.bbl Capitulos/*.blg Capitulos/*.lof\
		Capitulos/*.log Capitulos/*.out Capitulos/*.toc
