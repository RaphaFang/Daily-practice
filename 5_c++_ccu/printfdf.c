#include <stdio.h>

int main()
{
    /* 1. Declare three int variables and assign them the following values:
        num1 = 100
        num2 = 200
        float1 = 123.412
    */
    int num1 = 100;
    int num2 = 200;
    float float1 = 123.412;
    
    /* 2. Using the printf function:
        2.1 print the outcome of num1 + num2
        2.2 print the 123.4 using float 1
        2.3 print the outcomes of 2.1 and 2.2 in one line
    */
    
    printf("%d\n", num1 + num2);
    printf("%.1f\n", float1);
    printf("%d %.1f", num1 + num2, float1 );

    /* 3. Your out put should look like this
       300
       123.4
       300 123.4
    */
    
    return 0;
}
/*
formatted I/O
*/

#include <stdio.h>
int main()
{
    int score_per_test = 1, total_num_test = 6
    for(int num_test = 0, final_score = 0;
        num_test < total_num_per_test;
        num_test++, final_score += score_per_test){
        printf("%d", final_score);
    }
    return 0;
}

#include <stdio.h>

int main() 
{
    int score_per_test = 1;
    int total_num_tests = 6;

    for (int num_test = 0, final_score = 0; 
        num_test < total_num_tests; 
        num_test++, final_score += score_per_test) 
        {
        printf("%d ", final_score);
        }

    return 0;
}