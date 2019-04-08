#include <iostream>
using namespace std;

int main (int argc, char **argv) {
   double* lista  = NULL; 

   int n_side  = 2;


   lista  = new double[n_side * n_side];

   for (int i=0;i<n_side*n_side;i++){
     cout << lista[i] << endl;
   }

   for (int i=0;i<n_side*n_side;i++){
     lista[i] = i;
     cout << lista[i] << endl;
   }
   
   delete [] lista;
   return 0;
}
