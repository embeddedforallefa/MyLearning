#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

struct Person
{
    char *name;
    int age;
    int height;
    int weight;
};

struct Person *Person_create(char *name, int age, int height, int weight)
{
    struct Person *who = malloc(sizeof (struct Person));
    assert(who != NULL);

    who->name = strdup (name);
    who->age = age;
    who->height = height;
    who->weight = weight;

    return who;
};

void Person_Destroy(struct Person *who)
{
    assert(who!=NULL);

    free(who->name);
    free(who);
}

void   Person_Print(struct Person *who)
{
    printf("Name: %s\n", who->name);
    printf("\tAge: %d\n", who->age);
    printf("\tHeight: %d\n", who->height);
    printf("\tWeight: %d\n", who->weight);
}

int main(int argc, char *argv[])
{
    //Make two people structure
    struct Person *veer = Person_create("veeresh", 29, 157, 59);
    struct Person *madhu = Person_create("Madhushree", 27, 153, 45);

    // print them out and where they are in memory
    printf("veeresh is at memory location %p:\n", veer);
    Person_Print(veer);
    printf("Madhu is at memory location %p:\n", veer);
    Person_Print(madhu);

    // make everyone age 20 years and print them again
    veer->age = 20;
    veer->height -= 2;
    veer->weight -=5;

    madhu->age = 20;
    madhu->height -= 2;
    madhu->weight -=3;

    printf("People at 20");
    Person_Print(veer);
    Person_Print(madhu);
    //Destroy them both so we clean up
    Person_Destroy(veer);
    Person_Destroy(madhu);

    return 0;
}
