#include <iostream>
#include <fstream>
using namespace std;


void solve_equation_euler(float t_init, float t_end, float delta_t, float omega, string filename);
void solve_equation_rk4(float t_init, float t_end, float delta_t, float omega, string filename);
void solve_equation_leapfrog(float t_init, float t_end, float delta_t, float omega, string filename);

float dzdt(float t, float y, float z, float omega);
float dydt(float t, float y, float z, float omega);

int main(){
  float omega=1.0;
  solve_equation_euler(0.0, 10000.0, omega/2, omega, "euler.dat");
  solve_equation_rk4(0.0, 10000.0, omega/2, omega, "rk4.dat");
  solve_equation_leapfrog(0.0, 10000.0, omega/2, omega, "leapfrog.dat");
  return 0;
}

float dzdt(float t, float y, float z, float omega){
  return -omega * omega * y;
}

float dydt(float t, float y, float z, float omega){
  return z;
}

void solve_equation_euler(float t_init, float t_end, float delta_t, float omega, string filename){
  float t=t_init;
  float y=1.0;
  float z=0.0;
  float y_old = 0.0, z_old=0.0;
  ofstream outfile;
  outfile.open(filename);
  while(t<t_end){    
    z_old = z;
    y_old = y;
    outfile << t << " " << y << " " << z << endl;
    z  = z_old + delta_t * dzdt(t, y_old, z_old, omega);
    y = y_old + delta_t * dydt(t, y_old, z_old, omega);
    t = t + delta_t;
  }
  outfile.close();
}


void solve_equation_rk4(float t_init, float t_end, float delta_t, float omega, string filename){
  float t=t_init;
  float y=1.0;
  float z=0.0;
  float y_old = 0.0, z_old=0.0, t_old=0;
  float k_0_z, k_1_z, k_2_z, k_3_z;
  float k_0_y, k_1_y, k_2_y, k_3_y;
  float k_z, k_y;
  ofstream outfile;
  outfile.open(filename);
  while(t<t_end){    
    t_old = t;
    y_old = y;
    z_old = z;
    
    outfile << t << " " << y << " " << z << endl;
    
    k_0_y = dydt(t, y_old, z_old, omega);
    k_0_z = dzdt(t, y_old, z_old, omega);

    t = t_old + delta_t*0.5;
    y = y_old + 0.5 * delta_t * k_0_y;
    z = z_old + 0.5 * delta_t * k_0_z;
    k_1_y = dydt(t, y, z, omega);
    k_1_z = dzdt(t, y, z, omega);

    t = t_old + delta_t*0.5;
    y = y_old + 0.5* delta_t * k_1_y;
    z = z_old + 0.5* delta_t * k_1_z;
    k_2_y = dydt(t, y, z, omega);
    k_2_z = dzdt(t, y, z, omega);

    t = t_old + delta_t;
    y = y_old + delta_t * k_2_y;
    z = z_old + delta_t * k_2_z;
    k_3_y = dydt(t, y, z, omega);
    k_3_z = dzdt(t, y, z, omega);

    k_y  = k_0_y/6.0 + k_1_y/3.0 + k_2_y/3.0 + k_3_y/6.0;
    k_z  = k_0_z/6.0 + k_1_z/3.0 + k_2_z/3.0 + k_3_z/6.0;


    y = y_old + delta_t * k_y ;
    z = z_old + delta_t * k_z ;
    t = t_old + delta_t;
  }
  outfile.close();
}


void solve_equation_leapfrog(float t_init, float t_end, float delta_t, float omega, string filename){
  float t=t_init;
  float y=1.0;
  float z=0.0;
  ofstream outfile;
  outfile.open(filename);
  while(t<t_end){    
    outfile << t << " " << y << " " << z << endl;
    y = y + 0.5 * delta_t * dydt(t, y, z, omega);
    z  = z + delta_t * dzdt(t, y, z, omega);
    y  = y + 0.5 * delta_t * dydt(t, y, z, omega);
    t = t + delta_t;
  }
  outfile.close();
}
