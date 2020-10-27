#include <stdio.h>
#include <math.h>
#include <stdbool.h>

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

int calculate_distance(void)
{
	tuple x = {1,2};
	tuple y = {3,4};
	double result = distance(x,y);
	/* be aware of the different string formatting
	for printing out different data types*/
	printf("it works: %lf\n", result);
	return 0;
}

int booleans(void)
{
	int x = -1*-2;
	int y = 14%4;
	bool value = x==y;
	printf("%d\n",value);

	int z = 6;
	bool val = (-3 < 5 && !(z % 3 == 0));
	printf("%d\n",val);

	bool j = (-2 * -1 == 9 % 4);
	printf("%d\n",val);
	return 0;
}

int g(int x, int y) {
  switch(x - y) {
  case 0:
    return x;
  case 4:
    y = y + 1;
    break;
  case 7:
    x = x - 1;
  case 9:
    return x*y;
  case 3:
    y = x + 9;
  default:
    return y - x;
  }
return y;
}

int f(int x, int y) {
  if (x + 2 < y) {
    x = x + 3;
    return y * x;
  }
  else {
    return x + y + 2;
  }
}

int switch_cases()
{
	int x =  g(14, 7);
	int y = f(5, 7);
	printf("%d\n %d\n",x,y);
}

void function(int x, int y){
  while (x < y) {
    printf("%d ", y - x);
    x = x + 1;
    y = y - 1;
  }
}

int practice_loop1(int n) {
  int ans = 0;
  for (int i = 1; i < n; i++) {
    if (i < n/2) {
      ans -= i;
    }
    else {
      ans += i;
    }
  }
  return ans;
}

int practice_loop2(int x, int n) {
  for (int i = 0; i < n; i++) {
    if (i % 2 == 0) {
      x *= i + 1;
      continue;
    }
    x--;
    if (x == 0) {
      break;
    }
  }
  return x;
}

int practice_loop3(int x, int y){
	int j = 0;
	while(j < x){
		for(int i = j; i<y; i++){
			printf("%d,%d\n",j,i);
		}
		switch(j % 2 == 0){
			case 0:
				j+=3;
			default:
				j+=1;
		}
	}
}

int run_loops()
{
	int x = practice_loop1(7);
	int y = practice_loop2(1,3);
	printf("%d, %d\n",x,y);
}

int some_function(void) {
  int a = 2;
  int b = 6;
  while (a <= b) {
    if (a % 2 == 1) {
      printf("a is %d\n", a);
    }
    else {
      printf("b is %d\n", b);
      for (int i = 0; i < b - a ; i++) {
        printf("a * i + b = %d\n", a * i + b);
      }
    }
    a++;
    b--;
  }
  return 0;
}

int anotherFunction(int a, int b) {
  int answer = 2;
  int x = 0;
  printf("In anotherFunction(%d,%d)\n",a,b);
  while (b > a) {
    printf("a is %d, b is %d\n", a, b);
    answer = answer + (b - a);
    b -= x;
    a += x / 2;
    x++;
  }
  return answer;
}

int someFunction(int x, int y) {
  int a = x + y;
  if (x < y) {
    for (int i = 0; i < x; i++) {
      printf("In the loop with i = %d, a = %d\n", i, a);
      a = a + x;
    }
  }
  else {
    y = anotherFunction(y,a+1);
  }
  return a * (y-10);
}

int main(void) {
  int x = 2;
  int b = someFunction(3,x);
  printf("b = %d\n", b);
  printf("x = %d\n", x);
  return 0;
}