#include <iostream>
using namespace std;
 
int main () {
  double a[4] = {-3.0, 1, 2.0, 200.0, };
  double *puntero;
  int i;

  puntero = a;
  for ( i = 0; i < 4; i++ ) {
    cout << a[i] << endl;
  }

  for ( i = 0; i < 4; i++ ) {
    cout << *(puntero + i) << endl;
  }
   return 0;
}
