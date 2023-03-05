#include <stdio.h>

int checkprime(int a){
    for(int i=2;i<a;i++){
        if (a%i==0){
            return 0;
        }
    }
    return 1;
}

int main(){
    int input;
    scanf("%d",&input);
    int begin=3;
    int prime=2;
    int primenum=1;
    while(1){
        if(primenum==input){
            break;
        }
        if(checkprime(begin)==1){
            prime=begin;
            primenum+=1;
        }
        begin+=1;

    }
    printf("%d\n",prime);
    return 0;
}
/*
buddhi@DESKTOP-IQ34BAB:/mnt/d/ProjectEuler/10001stPrime$ ./solution
10001
104743
*/