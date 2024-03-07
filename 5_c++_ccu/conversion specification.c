#include <stdio.h>

int main()
{
    int i=321;
    printf("%d", i);
    printf("%04d", i);
    printf("%2d", i);
    /*
    here is display the spirit, %m.pX
    and in this case the .p is omitted
    */

    return 0;
}


#include <stdio.h>
int month=0, year=0;
{
printf("please input month and year:"); 
scanf("%d %d", &month , &year );
printf("month:%d\n", month);
printf("year: %d", year);

return 0;
} 