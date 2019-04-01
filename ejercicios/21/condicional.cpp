#include <iostream>
#include <random>
#include <stdlib.h>

int main(){
  int i;
  float r;
  
  srand48(42);

  for (i=0;i<20;i++){  
    r = drand48();
    if(r < 0.5){
      std::cout << i << " " << r << std::endl;
    }
  }
  
  return 0;
}

