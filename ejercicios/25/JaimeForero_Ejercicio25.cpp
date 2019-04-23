#include <iostream>
#include <fstream>
using namespace std;


void solve_equation_euler(float t_init, float t_end, float delta_t, float omega, string filename);
void solve_equation_implicit(float t_init, float t_end, float delta_t, float omega, string filename);
int main(){
  float omega=0.1;
  solve_equation_euler(0.0, 4.0/omega, 0.1/omega, omega, "euler_01.dat");
  solve_equation_euler(0.0, 4.0/omega, 0.01/omega, omega, "euler_001.dat");
  solve_equation_euler(0.0, 4.0/omega, 1.0/omega, omega, "euler_1.dat");
  solve_equation_implicit(0.0, 4.0/omega, 0.1/omega, omega, "implicit_01.dat");
  solve_equation_implicit(0.0, 4.0/omega, 0.01/omega, omega, "implicit_001.dat");
  solve_equation_implicit(0.0, 4.0/omega, 1.0/omega, omega, "implicit_1.dat");
  return 0;
}

void solve_equation_euler(float t_init, float t_end, float delta_t, float omega, string filename){
  float t=t_init;
  float y=1.0;
  ofstream outfile;
  outfile.open(filename);

  while(t<t_end){    
    outfile << t << " " << y << endl;
    y = y - delta_t * omega  * y;
    t = t + delta_t;
  }
  outfile.close();
}

void solve_equation_implicit(float t_init, float t_end, float delta_t, float omega, string filename){
  float t=t_init;
  float y=1.0;
  ofstream outfile;
  outfile.open(filename);

  while(t<t_end){    
    outfile << t << " " << y << endl;
    y = y/(1+delta_t*omega);
    t = t + delta_t;
  }
  outfile.close();
}
