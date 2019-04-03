#include <iostream>
#include <cstdlib>


using std::cout;
using std::endl;

void apuesta(int inicial, int *max, int *tiempo, int semilla);

int main(){
  int i, maximo, tiempo;
  
  for(i=0;i<100;i++){
    apuesta(100, &maximo, &tiempo, i);
    cout << maximo << " " << tiempo << endl;
  }
  return 0;
}

void apuesta(int inicial, int *max, int *tiempo, int semilla){
  int i, paso, maximo;
  srand(semilla);
  
  maximo = 0;
  i = 0;
  while(inicial>0){
    paso = rand()%3 -1;
    inicial += paso;
    if(inicial > maximo){
      maximo = inicial;
    }
    i++;
  }
  *max =  maximo;
  *tiempo= i;
}
