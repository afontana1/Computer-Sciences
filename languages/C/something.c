#include <stdio.h>
#include <math.h>

typedef struct 
{
	int xCoord;
	int yCoord;
} tuple;

double distance(tuple x, tuple y)
{
	int yComponent = x.yCoord - y.yCoord;
	int xComponent = x.xCoord - y.xCoord;
	int temp = (int)pow(yComponent,2) + (int)pow(xComponent,2);
	return sqrtl(temp);
}

int main(void)
{
	tuple x = {1,2};
	tuple y = {3,4};
	double result = distance(x,y);
	/* be aware of the different string formatting
	for printing out different data types*/
	printf("it works: %lf\n", result);
	return 0;
}
