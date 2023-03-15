#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
The right upper diagonal goes in a series as 3^2,5^2,7^2,9^2
Left upper follows 3^2-2,5^2-4,7^2-6
left lower follows 3^2-4,5^2-8,7^2-12
right lower follows 3^2-6,5^2-12,7^2-18
*/

int main(){
    int sum;
    int n;
    scanf("%d",&n); // n should be odd

    int upperrows;
    upperrows=(n-1)/2;
    for (int i=0;i<=upperrows;i++){
        if(i==0){
            sum+=1;
        }
        else{
            int rightup,rightdown,leftup,leftdown;
            rightup=pow((2*i+1),2.0);
            leftup=rightup-2*i;
            leftdown=rightup-4*i;
            rightdown=rightup-6*i;
            sum+=rightup+rightdown+leftup+leftdown;
        }

    }
    printf("%d\n",sum);
    return 0;
}