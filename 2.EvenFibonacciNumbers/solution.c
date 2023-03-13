#include <stdio.h>


int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long n; 
        scanf("%ld",&n);
        int a=0;
        int b=1;
        int sum=0;
        int temp;
        while(b<n){
            temp=b;
            b=temp+a;
            a=temp;
            if (a%2==0){
                sum+=a;
            }
        }
        printf("%d\n",sum);
    }
    return 0;
}

/*
buddhi@DESKTOP-IQ34BAB:/mnt/d/ProjectEuler/EvenFibonacciNumbers$ ./solution
1
4000000
4613732
*/