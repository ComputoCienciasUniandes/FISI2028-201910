#include <iostream>
#include <fstream>
#include <cmath>

/*Solucion de la ecuacion de onda por diferencias finitas*/
using namespace std;

int main(){
  double L=1.0;
  double delta_x = 0.01;
  double delta_t = 0.01;
  double t_max = 6.0, t=0.0;
  double c=0.5;
  double c_prime=delta_x/delta_t;
  int n_side = L/(delta_x) + 1;
  double y_past[n_side];
  double y_present[n_side];
  double y_future[n_side];
  double pi = asin(1.0)*2.0;
  int iteracion=0;
  double x;
  ofstream outfile;
  int i;

  /*inicializa T_old*/
  for(i=0;i<n_side;i++){
    x = i * delta_x;
    y_past[i] = sin(pi * x/L);
    y_present[i] = y_past[i];
    y_future[i] = y_past[i];
  }

  outfile.open("onda.dat");
  /*primer paso de tiempo es diferente por la condicion 
   de derivada parcial con respecto al tiempo igual a cero*/
  for(i=1;i<n_side-1;i++){
    y_present[i] = y_past[i] + 0.5*pow(c/c_prime,2.0) * (y_past[i+1] + y_past[i-1] -2.0*y_past[i]);
  }
  t = t+delta_t;

  /*esquema valido para las iteraciones siguientes*/
  while(t < t_max){
    /*Escribe en el archivo*/
    for(i=0;i<n_side;i++){
      outfile << y_present[i] << " ";
    }
    outfile << "\n";
    
    /*actualiza future*/
    for(i=1;i<n_side-1;i++){
      y_future[i] = 2.0*y_present[i] - y_past[i];
      y_future[i] += pow(c/c_prime, 2.0) * (y_present[i+1] + y_present[i-1] -2.0 * y_present[i]);
    }
    
    /*copia los arrays*/
    for(i=1;i<n_side-1;i++){
      y_past[i] = y_present[i];
      y_present[i] = y_future[i];
    }
    t = t + delta_t;
  }
  outfile.close();

  return 0;
}
