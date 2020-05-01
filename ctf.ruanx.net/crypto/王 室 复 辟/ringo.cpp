#include <cstdio>
#include <cstring>

char map[256];
char s[] = "synt{Pnrfne_Hfvat_Bssfrg_guvegrra_vf_Pnyyrq_EBG}";

inline void mark(char s, char e) {
	printf("%d %d : %d\n", s, e, s - e);
	map[s] = e;
}

int main() {
	for (int i = 0; i < 256; i++) map[i] = i;

	mark('s', 'f');
	mark('y', 'l');
	mark('n', 'a');
	mark('t', 'g');

	for (int i = 0; i < 2; i++) {
		int base = i ? 'A' : 'a';

		for (int j = 0; j < 26; j++) { mark(base + j, base + (j + 13) % 26); }
	}

	for (int i = 0; i < strlen(s); i++) {
		auto c = s[i];
		auto o = map[(size_t)c];

		if (c == o) {
			printf("\e[31m%c\e[0m", o);
		} else {
			putchar(o);
		}
	}
	putchar('\n');
}