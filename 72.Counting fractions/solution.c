#include <stdio.h>
#include <stdlib.h>

int main(){

    int limit=1000000;

    long *arr=calloc(limit+1,sizeof(long));

    for(int i=0;i<limit+1;i++){
        arr[i]=i-1;
    }

    for (int i=2;i<limit+1;i++){
        if (arr[i]==i-1){
            for (int j=2*i;j<limit+1;j+=i){
                arr[j]-=arr[j]/i;
            }
        }
    }
    long int count=0;
    for(int i=2;i<limit+1;i++){
        count+=arr[i];
    }
    printf("%ld",count);
    return 0;
}
// buddhi@DESKTOP-IQ34BAB:/mnt/d/ProjectEuler/72.Counting fractions$ ./solution
// 303963552391