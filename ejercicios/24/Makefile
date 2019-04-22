fit_mcmc.png: fit_mcmc.dat
	python plot_mcmc.py 

fit_mcmc.dat: fit_mcmc.x
	./fit_mcmc.x > fit_mcmc.dat

fit_mcmc.x: fit_mcmc.cpp
	c++ fit_mcmc.cpp -o fit_mcmc.x