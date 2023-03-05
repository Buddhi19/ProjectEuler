#include <stdio.h>

int main(){
    int input;
    scanf("%d",&input);
    int linearsum;
    linearsum=input*(input+1)/2;
    int linsquare=linearsum*linearsum;
    int squaresum;
    squaresum=input*(input+1)*(2*input+1)/6;
    int ans= linsquare-squaresum;
    printf("%d\n",ans);
    return 0;
}