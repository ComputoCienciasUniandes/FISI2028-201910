all: euler_001.dat euler_01.dat euler_1.dat implicit_001.dat implicit_01.dat implicit_1.dat 

%.dat: JaimeForero_Ejercicio25.x
	./JaimeForero_Ejercicio25.x

JaimeForero_Ejercicio25.x: JaimeForero_Ejercicio25.cpp
	c++ JaimeForero_Ejercicio25.cpp -o JaimeForero_Ejercicio25.x

clean:
	rm -rf *.x *.dat