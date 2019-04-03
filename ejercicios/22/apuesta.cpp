#include <iostream>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::endl;

int main(){
  int posicion;
  int step;
  int i;
  srand(time(0));

  posicion = 100;
  i = 0;
  while(posicion>0){
    step = rand()%3 -1;
    posicion += step;
    cout << i << " "<< posicion << endl;
    i++;
  }
  return 0;
}
