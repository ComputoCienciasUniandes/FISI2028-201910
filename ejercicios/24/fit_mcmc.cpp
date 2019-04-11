#include <fstream>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <cmath>

using namespace std; 

float *read_file(string filename, int *n_points);
void model(float *y, float*x, int n_points, float *c, int poly_degree);
float loglikelihood(float *x_obs, float *y_obs, int n_points, float *c, int poly_degree);
float logprior(float *c, int poly_degree);
void MCMC_polynomial(float *x_obs, float *y_obs, int n_points, int n_steps, int poly_degree);

int main(){
  float *x=NULL;
  float *y=NULL;
  int n_x=0;
  int n_y=0;

  x = read_file("valores_x.txt", &n_x);
  y = read_file("valores_y.txt", &n_y);
  
  MCMC_polynomial(x, y, n_x, 1000000, 3);
  
  return 0;
}

void MCMC_polynomial(float *x_obs, float *y_obs, int n_points, int n_steps, int poly_degree){
  int i, j, k;
  float sigma_step = 0.1;
  float like_now, like_next;
  float u;
  float r;
  float *c;
  float *c_next;

  c = new float[poly_degree+1];
  c_next = new float[poly_degree+1];

  for(k=0;k<=poly_degree;k++){
    c[k] = 0.0;
  }

  for(i=0;i<n_steps;i++){
    
    for(k=0;k<=poly_degree;k++){
      c_next[k] = c[k] + sigma_step * (drand48()-0.5);
    }
    like_now = loglikelihood(x_obs, y_obs, n_points, c, poly_degree);
    like_next = loglikelihood(x_obs, y_obs, n_points, c_next, poly_degree);
    r = exp(like_next - like_now);
    if(r>1){
      r=1.0;
    }
    u = drand48();
    if(u<r){
      for(k=0;k<poly_degree+1;k++){
	c[k] = c_next[k];
      }
    }
    for(k=0;k<poly_degree+1;k++){
      cout << c[k] << " ";
    }
    cout << "\n";

  }
} 

float loglikelihood(float *x_obs, float *y_obs, int n_points, float *c, int poly_degree){
  int i;
  float d=0;
  float *y_model;
  float sigma=0.1;
  y_model = new float[n_points];

  //calcula el modelo
  model(y_model, x_obs, n_points, c, poly_degree);

  //calcula la diferencia entre el modelo y las observaciones.
 for(i=0;i<n_points;i++){
    d += -0.5*pow(((y_obs[i] - y_model[i])/sigma), 2.0);
  }
  delete [] y_model; 
  return d;
}

float logprior(float *c, int poly_degree){
  return 0;
}

void model(float *y, float*x, int n_points, float *c, int poly_degree){
  int i,j;
  for (i=0;i<n_points;i++){
    y[i] = 0.0;
    for (j=0;j<=poly_degree;j++){
      y[i] = y[i] + c[j] * pow(x[i], j);
    }
  }
}

float * read_file(string filename, int *n_points){
  int n_lines=0;
  ifstream infile; 
  string line;
  int i;
  float *array;

  /*cuenta lineas*/
  infile.open(filename); 
  getline(infile, line);
  while(infile){
    n_lines++;
    getline(infile, line);
  }
  infile.close();
  *n_points = n_lines;

  /*reserva la memoria necesaria*/
  array = new float[n_lines];

  /*carga los valores*/
  i=0;
  infile.open(filename); 
  getline(infile, line);  
  while(infile){
    array[i] = atof(line.c_str());
    i++;
    getline(infile, line);
  }
  infile.close();

  return array;
}





