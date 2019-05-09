movie.gif: adveccion.dat plot.py
	python plot.py

%.dat : a.out
	./a.out 

a.out: JaimeForero_Ejercicio30.cpp
	g++ JaimeForero_Ejercicio30.cpp

clean:
	rm -rf a.out adveccion.dat *.png *~