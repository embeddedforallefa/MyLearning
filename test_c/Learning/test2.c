#include <stdio.h>

int main (int argc, char *argv[])
{
	int distance = 100;
	float power = 2.143f;
	double super_power = 1254.12548;
	char initial = 'P';
	char first_name[] = "Veeresh";
	char last_name[]= "Sharanappa";
	char empty[]= "";

	printf("you are %d miles away.\n", distance);
	printf("you have %f levels of power.\n", power);
	printf("you have %f awesome super power.\n", super_power);
	printf("I have an initial %c.\n",initial);
	printf("I have a first name %s.\n", first_name);
	printf("I have a last name %s.\n", last_name);
	printf("My full name is %s %c %s.\n",first_name,initial,last_name);
	printf("empty string is %s.\n", empty);

	return 0;
}
