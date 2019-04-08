#include <iostream>
using namespace std;

int main (int argc, char **argv) {
   double* lista  = NULL; 
   int n_side;
   int i;

   cout << "Argumentos "<< endl;
   for(i=0;i<argc;i++){
     cout << i << " "<< argv[i] << endl;
   }

   n_side = atoi(argv[1]);


   lista  = new double[n_side * n_side];
   
   cout << "Lista sin inicializar"<< endl;
   for (int i=0;i<n_side*n_side;i++){
     cout << lista[i] << endl;
   }
   
   cout << "Lista inicializada"<< endl;
   for (int i=0;i<n_side*n_side;i++){
     lista[i] = i;
     cout << lista[i] << endl;
   }
   
   delete [] lista;
   return 0;
}
