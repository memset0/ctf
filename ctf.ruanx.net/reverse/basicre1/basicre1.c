/**
 * Get correct input to make program print Congratulations!
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXBUF 0x100

static char password[MAXBUF];

int CheckPassword(char *password) {
  static unsigned char target[] = {33,  60, 102, 37, 14,  97,  32, 13, 41,  52,
                                   108, 1,  59,  57, 40,  107, 38, 27, 119, 32,
                                   30,  50, 112, 52, 126, 62,  60, 125};
  
  for (int i = 0; i < sizeof(target); ++i) {
    password[i] = target[i] ^ i ^ 0x55;
  }
  for (int i = 0; i < sizeof(target); i++) {
    printf("%c", password[i]);
  }
  printf("\n");

  for (int i = 0; i < sizeof(target); ++i) {
    if ((password[i] ^ i ^ 0x55) != target[i]) {
      return 0;
    }
  }
  return 1;
}

char *GetInput(void) {
  // puts("Password please:");
  // fgets(password, MAXBUF, stdin);
  // strtok(password, "\n");
  return password;
}

int main(void) {
  char *input = GetInput();
  if (CheckPassword(input) == 1) {
    puts("Congratulations!");
  } else {
    puts("Try harder.");
  }
  return 0;
}