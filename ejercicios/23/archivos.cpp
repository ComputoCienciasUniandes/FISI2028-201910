#include <fstream>
#include <iostream>
using namespace std;
 
void ejemplo_lee(string filename);
void ejemplo_escribe(string filename);

int main () {
  string filename;
  filename = "datos.dat";
  ejemplo_lee(filename);

  filename = "secuencia.dat";
  ejemplo_escribe(filename);
  return 0;
}

void ejemplo_lee(string filename){
  ifstream infile; 
  string line;

  infile.open(filename); 
  
  cout << "Leyendo de " << filename << endl; 
  getline(infile, line);
  while(infile){
    cout << line << endl;
    getline(infile, line);
  }

  infile.close();
}

void ejemplo_escribe(string filename){
  ofstream outfile;


  outfile.open(filename);

  cout << "Escribiendo en " << filename << endl; 
  for (int i=0; i < 10; i++){
    outfile << i << endl;
  }
  outfile.close(); 
}
