#include <iostream>
#include <string>

using namespace std;

int main () {

  //Cadenas de caracteres
  char pais[8] = {'E', 's', 't', 'o', 'n', 'i', 'a', '\0'};
  
  cout << "Un pais: ";
  cout << pais << endl; 
  
  char ciudad[256];
  strcpy(ciudad, "Barrancabermeja");
  cout << "Una ciudad: " ;
  cout << ciudad << endl;

  char color[256] = "Amarillo";
  cout << "Un color: ";
  cout << color << endl;


  //La clase string
  string s_pais = "Estonia";
  
  cout << "Un pais: ";
  cout << s_pais << endl; 
  
  string s_ciudad;
  s_ciudad = ciudad;
  cout << "Una ciudad: " ;
  cout << s_ciudad << endl;

  string s_color ;
  cout << "Una ciudad y un pais: ";
  cout << s_ciudad + s_pais << endl;  

  cout << "Size:" << s_ciudad.size() << " "<<s_pais.size() << endl;

  return 0;
}
