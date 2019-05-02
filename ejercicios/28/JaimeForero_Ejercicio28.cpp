#include <iostream>
#include <fstream>
#include <cmath>

/*Solucion de la ecuacion de poisson por el metodo de relajacion*/
/*Problema de dos placas encerradas en una caja conductora a potencial cero*/
using namespace std;

int main(){
  double kappa=200.0;
  double C=900.0;
  double rho=2700;  
  double t_max = 100.0;
  double delta_t = 0.5;
  double eta;
  double t;
  double delta_x = 0.01;
  int n_side = 2.0/(delta_x) + 1;
  double T_old[n_side];
  double T_new[n_side];
  int i, j;
  int iteracion=0;
  ofstream outfile;

  /*inicializa T_old*/
  for(i=0;i<n_side;i++){
    T_old[i] = 300.0;
    if(i>80 && i < 120){
      T_old[i] = 500.0;      
    }
  }
  T_new[0] = 300.0;
  T_new[n_side-1] = 300.0;

  /*calculo de eta*/
  eta = kappa * delta_t / (C * rho * delta_x * delta_x);
  cout << eta << endl;


  outfile.open("temperatura.dat");
  /*evolucion temporal*/
  while(t < t_max){
    /*Calcula nuevo valor de la temperatura*/
    for(i=1;i<n_side-1;i++){
      T_new[i] = T_old[i] + eta * (T_old[i+1]+T_old[i-1]-2.0*T_old[i]);
    }
    /*Escribe en el archivo*/
    for(i=0;i<n_side;i++){
      outfile << T_new[i] << " ";
    }
    outfile << "\n";

    /*Reescribe old*/
    for(i=1;i<n_side-1;i++){
      T_old[i] = T_new[i];
    }
    t = t + delta_t;
  }
  outfile.close();
  return 0;
}
