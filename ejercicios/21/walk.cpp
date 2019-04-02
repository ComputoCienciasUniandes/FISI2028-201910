#include <iostream>
#include <random>
#include <stdlib.h>

int main(){
  int i;
  float pi = 2.0*asin(1.0);
  float theta;
  float x;
  float y;
  
  srand48(8);

  for (i=0;i<1000;i++){  
    theta = drand48()*2.0*pi;
    x = x + cos(theta);
    y = y + sin(theta);
    std::cout << x << " " << y << std::endl;
  }
  
  return 0;
}

