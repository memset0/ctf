/**
 * Get correct input to make program print Congratulations!
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXBUF 0x100

static char password[MAXBUF];

// Do you know this algorithm ?
void Encrypt(void* dest, const void* v, const void* k) {
	uint8_t i;
	uint32_t v0 = ((uint32_t*)v)[0], v1 = ((uint32_t*)v)[1];
	uint32_t sum = 0, delta = 0x9E3779B9;

	for (i = 0; i < 8; i++) {
		printf("%d%c", ((uint8_t*)dest)[i], " \n"[i == 7]);
	}

	for (i = 0; i < 32; i++) {
		printf("%u : %u %u %u\n", i, sum, sum & 3, sum >> 11 & 3);
		v0 += ((v1 << 4 ^ v1 >> 5) + v1) ^ (sum + ((uint32_t*)k)[sum & 3]);
		sum += delta;
		printf("%u : %u %u %u\n", i, sum, sum & 3, sum >> 11 & 3);
		v1 +=
			((v0 << 4 ^ v0 >> 5) + v0) ^ (sum + ((uint32_t*)k)[sum >> 11 & 3]);
	}
	((uint32_t*)dest)[0] = v0;
	((uint32_t*)dest)[1] = v1;
	for (i = 0; i < 8; i++) printf("%u%c", ((uint8_t*)dest)[i], " \n"[i == 7]);
}

int CheckPassword(const char* password) {
	int length = strlen(password);
	uint8_t* buf = malloc(length);
	memcpy(buf, password, length);

	const uint32_t key[] = {1634494796, 1818840163, 1766613857, 6513004};

	uint8_t target[] = {0x6f, 0x7d, 0xcf, 0x96, 0x9d, 0x31, 0x1f, 0x9b,
						0xa0, 0x82, 0x9e, 0x2a, 0x73, 0xe6, 0xde, 0xb3,
						0xab, 0x99, 0xbb, 0x88, 0x29, 0xa6, 0xa3, 0xcd};

	for (int i = 0; i < length; i += 8) { Encrypt(buf + i, buf + i, key); }

	return !memcmp(buf, target, sizeof(target));
}

char* GetInput(void) {
	puts("Password please:");
	fgets(password, MAXBUF, stdin);
	strtok(password, "\n");
	return password;
}

int main(void) {
	char* input = GetInput();
	if (CheckPassword(input) == 1) {
		puts("Congratulations!");
	} else {
		puts("Try harder.");
	}
	return 0;
}