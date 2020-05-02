#include <cstdio>
#include <vector>
#include <cstdlib>

std::vector<uint8_t> solve(std::vector<uint8_t> source) {
	std::vector<uint32_t> sum;
	std::vector<uint32_t> key = {1634494796, 1818840163, 1766613857, 6513004};

	uint32_t tmp = 0, delta = 0x9E3779B9;
	for (int i = 0; i <= 32; i++) sum.push_back(tmp), tmp += delta;

	uint32_t v0 = ((uint32_t*)&source[0])[0];
	uint32_t v1 = ((uint32_t*)&source[0])[1];
	for (int i = 31; i >= 0; i--) {
		v1 -= ((v0 << 4 ^ v0 >> 5) + v0) ^
			(sum[i + 1] + (key[sum[i + 1] >> 11 & 3]));
		v0 -= ((v1 << 4 ^ v1 >> 5) + v1) ^ (sum[i] + (key[sum[i] & 3]));
	}

	std::vector<uint8_t> dest(source.size());
	((uint32_t*)&dest[0])[0] = v0;
	((uint32_t*)&dest[0])[1] = v1;
	return dest;
}

int main() {
	// std::vector<uint8_t> prob = {75, 232, 45, 195, 72, 91, 212, 64};
	std::vector<uint8_t> prob = {0x6f, 0x7d, 0xcf, 0x96, 0x9d, 0x31,
								 0x1f, 0x9b, 0xa0, 0x82, 0x9e, 0x2a,
								 0x73, 0xe6, 0xde, 0xb3, 0xab, 0x99,
								 0xbb, 0x88, 0x29, 0xa6, 0xa3, 0xcd};
	for (int i = 0; i < prob.size(); i += 8) {
		auto vec = solve(std::vector<uint8_t>(&prob[i + 0], &prob[i + 8]));
		// for (int i = 0; i < vec.size(); i++)
		// 	printf("%d%c", vec[i], " \n"[i == 7]);
		for (int i = 0; i < vec.size(); i++) putchar(vec[i]);
	}
}