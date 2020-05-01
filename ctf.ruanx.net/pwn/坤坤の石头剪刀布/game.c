#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void printWelcomeMsg() {
    puts("Are you good at the game `Rock, Paper, Scissors`?");
    puts("I'm going to play the game 100 times with you, and only if you win 100 times, I will give you the flag.");
    puts("That's quite easy, isn't it?");
    puts("");
    puts("input: 0 = Rock, 1 = Paper, 2 = Scissors");
    fflush(stdout);
}

void printFlag() {
    puts(getenv("flag"));
    fflush(stdout);
}

int getInput() {
    char s[100];
    scanf("%s", s);
    char ch = s[0];

    if(ch < '0' || ch > '2') {
        puts("Oh, input is invalid.");
        exit(1);
    }

    return ch - '0';
}

// Linux下的rand()与Windows下的rand()表现不同。
// 为了防止坑选手，我们自己造了一个rand.

int num = 0;

int myRand() {
    num = (num * num + 233) % 23333;
}

int mySrand(unsigned int seed) {
    num = seed;
}

int playOnce() {
    printf("Input your choice> ");
    fflush(stdout);

    int ai = myRand() % 3;
    int player = getInput();

    if(player == 1 && ai == 0)
        return 1;
    if(player == 2 && ai == 1)
        return 1;
    if(player == 0 && ai == 2)
        return 1;
    
    return 0;
}

void work() {
    mySrand(time(0) % 10);

    for(int x=0; x<100; x++)
        if(playOnce()) {
            printf("nice try (%d/100)\n", x+1);
            fflush(stdout);
        }
        else {
            puts("Oh no... You failed.");
            fflush(stdout);
            exit(0);
        }
    
    printFlag();
}

int main(void) {
    printWelcomeMsg();

    work();

    return 0;
}
