#include <stdio.h>
#include <stdlib.h>


int steps(long int n){
    if (n==1){
        return 0;
    }
    if (n%2==0){
        return (1+steps(n/2));
    }
    else{
        return (1+steps(3*n +1));
    }
}



int main(){
    int n;
    int longest=1;
    int starting=1;
    scanf("%d",&n);
    for(int i=2;i<n;i++){
        int num;
        num=steps(i);
        //printf("%d %d\n",i ,num);
        if (num>=longest){
            longest=num;
            starting=i;
        }
    }
    printf("%d\n",starting);
    return 0;
}

/*
buddhi@DESKTOP-IQ34BAB:/mnt/d/ProjectEuler/14.Longest Collatz sequence$ ./solution
1000000
837799
*/