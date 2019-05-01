#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(){
  int n_side = 101;
  int delta = 1.0;
  double u_old[n_side][n_side];
  double u_new[n_side][n_side];
  int i, j;
  int iteracion=0;
  ofstream outfile;
  double error=10;
  /*inicializa old_ud*/
  for(i=0;i<n_side;i++){
    for(j=0;j<n_side;j++){
      u_old[i][j]=0.0;
      if((i>20) && (i<80)){
	if(j==40){
	  u_old[i][j] = -100;
	}
	if(j==60){
	  u_old[i][j] = +100;
	}
      }
    }
  }

  while(error>1E-6){
    iteracion +=1;
    cout << iteracion << endl;
    /*calcula new*/
    for(i=1;i<n_side-1;i++){
      for(j=1;j<n_side-1;j++){
	u_new[i][j] = 0.25*(u_old[i+1][j]+u_old[i-1][j] + u_old[i][j-1]+ u_old[i][j+1]);
      }
    }

    /*deja las placas en su valor*/
    for(i=1;i<n_side-1;i++){
      for(j=1;j<n_side-1;j++){	
	if((i>20) && (i<80)){
	  if(j==40){
	    u_new[i][j] = -100;
	  }
	  if(j==60){
	    u_new[i][j] = +100;
	  }
	}
      }
    }
    
    error = 0.0;
    /*calcula el error total*/
    for(i=1;i<n_side-1;i++){
      for(j=1;j<n_side-1;j++){
	error += abs(u_old[i][j]-u_new[i][j]);
      }
    }

    /*copia new en old*/
    for(i=1;i<n_side-1;i++){
      for(j=1;j<n_side-1;j++){
	u_old[i][j] = u_new[i][j];
      }
    }
  }


  outfile.open("placas.dat");
  /*imprime*/
  for(j=0;j<n_side;j++){
    for(i=0;i<n_side;i++){
      outfile << u_old[i][j] << endl;
    }
  }
  outfile.close();
  return 0;
}
