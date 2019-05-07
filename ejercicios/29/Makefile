plot.png: onda.dat plot.py
	python plot.py

%.dat : a.out
	./a.out 

a.out: JaimeForero_Ejercicio29.cpp
	g++ JaimeForero_Ejercicio29.cpp

clean:
	rm -rf a.out onda.dat plot.png *~