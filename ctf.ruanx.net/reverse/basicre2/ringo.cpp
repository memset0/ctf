#include <bits/stdc++.h>

int main() {
	std::vector<int> data = {1211396208, 2034593380, 1765043792, 878930775,
							 1769236560, 2037672047, 1851749236, 1920295796};
	// std::vector<int> data = {1633837924, 1701209960, 1768581996, 1852665712,
	// 						 1903326068, 1970698104, 2038051122, 858862131};
	std::vector<int> result(data.size() << 2);

	const int magic_number = (1 << 8) - 1;
	for (int i = 0; i < data.size(); i++) {
		result[i << 2] = data[i] >> 24 & magic_number;
		result[i << 2 | 1] = data[i] >> 16 & magic_number;
		result[i << 2 | 2] = data[i] >> 8 & magic_number;
		result[i << 2 | 3] = data[i] & magic_number;
	}
	for (int i = 0; i < result.size(); i++)
		printf("%d%c", result[i], " \n"[i + 1 == result.size()]);

	for (int i = 0; i < result.size(); i++) putchar(result[i]);
	putchar('\n');
}