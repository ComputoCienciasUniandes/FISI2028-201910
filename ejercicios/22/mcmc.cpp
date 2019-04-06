#include <iostream>
#include <cmath>
#include <stdlib.h>

using std::cout;
using std::endl;

void MCMC(int n);
float gauss(float x);

int main(){
  MCMC(10000);
  return 0;
}

float gauss(float x){
  return exp(-0.5*x*x);
}

void MCMC(int n){
  int i;
  float x, r, x_next, u;

  srand48(i);

  x = 0.0;
  for (i=0;i<n;i++){
    x_next = x + 2.0*(drand48()-0.5);
    r = gauss(x_next)/gauss(x);
    if(r>1.0){
      r = 1.0;
    }
    
    u = drand48();
    if(u<r){
      x = x_next;
    }

    cout << x << endl;
  }
}
