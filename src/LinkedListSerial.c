#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/time.h>

#define MAX_VALUE 65536

struct list_node_s {
    int    data;
    struct list_node_s* next;
};

// Method declarations
int  Delete(int value);
int  Insert(int value);
int  Member(int value);

void doOperations();
void initialize(int);
int generateRandom(void);
long current_timestamp(void);

// Variables
struct list_node_s* head_p = NULL;
int noOfOperations;
int noOfMember;
int noOfInsert;
int noOfDelete;

int main(int arc, char *argv[]) {
    // Validate the arguments
    if (arc != 6) {
        printf("Invalid number of arguments %d\n", arc);
        return -1;
    }
    // Variables
    long start, finish, elapsed;

    // Collect and interpret the arguments
    int noOfVariables = atoi(argv[1]);
    noOfOperations = atoi(argv[2]);
    noOfMember = strtod(argv[3], NULL) * noOfOperations;
    noOfInsert = strtod(argv[4], NULL) * noOfOperations;
    noOfDelete = strtod(argv[5], NULL) * noOfOperations;

    // Initialize the linkedlist
    initialize(noOfVariables);

    // Get the starting time
    start = current_timestamp();

    // Do the operations
    doOperations();

    // Get the ending time
    finish = current_timestamp();

    // Calculate the elapsed time
    elapsed = finish - start;

    // Print the time to stdout
    printf("%ld", elapsed);
    return 0;
}

//get the current time
long current_timestamp() {
    struct timeval te;
    gettimeofday(&te, NULL); // get current time
    long milliseconds = te.tv_sec*1000LL + te.tv_usec/1000; // caculate milliseconds
    // printf("milliseconds: %lld\n", milliseconds);
    return milliseconds;
}

//to get random data for initial data and test data
int generateRandom() {
    int value = rand() % MAX_VALUE;
    return value;
}

//initialize the linked list
void initialize(int noOfVariables) {
    srand (time(NULL));
    int Inserted = 0;
    int i;
    for (i = 0; i < noOfVariables; i++) {
        Inserted = Insert(generateRandom());
        if (!Inserted) {
            i--;
        }
    }
}

//call menber, insert and delete.
void doOperations() {
    long i;
    for (i = 0; i < noOfOperations; i++) {
        if (i < noOfInsert) {
            int value = generateRandom();
            Insert(value);
        } else if (i < noOfInsert + noOfDelete) {
            int value = generateRandom();
            Delete(value);
        } else {
            int value = generateRandom();
            Member(value);
        }
    }
}

//delete an element from the linked list
int Delete(int value) {
    struct list_node_s* curr_p = head_p;
    struct list_node_s* pred_p = NULL;

    /* Find value */
    while (curr_p != NULL && curr_p->data < value) {
        pred_p = curr_p;
        curr_p = curr_p->next;
    }

    if (curr_p != NULL && curr_p->data == value) {
        if (pred_p == NULL) {
            head_p = curr_p->next;
            free(curr_p);
        } else {
            pred_p->next = curr_p->next;
            free(curr_p);
        }
        return 1;
    } else {
        return 0;
    }
}

//insert an element in a linked list
int Insert(int value) {
    struct list_node_s* curr_p = head_p;
    struct list_node_s* pred_p = NULL;
    struct list_node_s* temp_p;

    while (curr_p != NULL && curr_p->data < value) {
        pred_p = curr_p;
        curr_p = curr_p->next;
    }

    if (curr_p == NULL || curr_p->data > value) {
        temp_p = malloc(sizeof(struct list_node_s));
        temp_p->data = value;
        temp_p->next = curr_p;
        if (pred_p == NULL)
            head_p = temp_p;
        else
            pred_p->next = temp_p;
        return 1;
    } else {
        return 0;
    }
}

//check for the existing element in a linked list
int  Member(int value) {
    struct list_node_s* curr_p;

    curr_p = head_p;
    while (curr_p != NULL && curr_p->data < value)
        curr_p = curr_p->next;

    if (curr_p == NULL || curr_p->data > value) {
        return 0;
    } else {
        return 1;
    }
}
