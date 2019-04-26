plot.png: euler.dat rk4.dat leapfrog.dat plots.py
	python plots.py

%.dat : a.out
	./a.out

a.out: JaimeForero_Ejercicio26.cpp
	g++ JaimeForero_Ejercicio26.cpp