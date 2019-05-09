#include <iostream>
#include <fstream>
#include <cmath>

/*Solucion de la ecuacion de adveccion no-lineal (Burgers) con el esquema explicito de Lax-Wendroff*/

using namespace std;

int main(){
  double L=1.0;
  double delta_x = 0.01;
  double delta_t = 0.01;
  double t_max = 2.0, t=0.0;
  double epsilon = 1.0;
  double beta = epsilon/(delta_x/delta_t);
  int n_side = L/(delta_x) + 1;
  double y_past[n_side];
  double y_present[n_side];
  double pi = asin(1.0)*2.0;
  int iteracion=0;
  double x;
  ofstream outfile;
  int i;

  /*inicializa T_old*/
  for(i=0;i<n_side;i++){
    x = i * delta_x;
    y_past[i] = 0.05*sin(4.0*pi * x/L);
    y_present[i] = y_past[i];
  }

  outfile.open("adveccion.dat");
  
  while(t < t_max){
    /*Escribe en el archivo*/
    for(i=0;i<n_side;i++){
      outfile << y_present[i] << " ";
    }
    outfile << "\n";
    
    /*actualiza future*/
    for(i=1;i<n_side-1;i++){
      y_present[i] = y_past[i] - 0.25*beta*(y_past[i+1]*y_past[i+1] - y_past[i-1]*y_past[i-1]);
      y_present[i] += (1.0/8.0)*beta*beta*((y_past[i+1] + y_past[i])*
					   (y_past[i+1]*y_past[i+1] - y_past[i]*y_past[i])-
					   (y_past[i]+y_past[i-1])*(y_past[i]*y_past[i] 
								    - y_past[i-1]*y_past[i-1]));
    }
    
    /*copia los arrays*/
    for(i=1;i<n_side-1;i++){
      y_past[i] = y_present[i];
    }
    t = t + delta_t;
  }
  outfile.close();

  return 0;
}
