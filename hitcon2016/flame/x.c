
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

const uint32_t cipher[35] = 
{
	0x00000cfe, 0x00000859, 0x0000095d, 0x00000871,
	0x0000040d, 0x00000006, 0x00000ade, 0x00000fa8,
	0x00000561, 0x000009da, 0x00000878, 0x00000682,
	0x00000fa9, 0x00000f5f, 0x0000025e, 0x00000db0,
	0x00000fbf, 0x00000bc6, 0x00000d38, 0x0000095d,
	0x00000d09, 0x000007ed, 0x00000307, 0x000001c0,
	0x00000399, 0x00000956, 0x00000a45, 0x00000292,
	0x00000c8a, 0x0000092f, 0x0000004a, 0x00000964,
	0x00000194, 0x000009da, 0x0000011f
};

int
main() {
	uint8_t buf[(sizeof(cipher)/sizeof(cipher[0]))+1];
	int i;

	srand(7777);
	buf[sizeof(buf)-1] = '\0';
	for (i = 0; i < sizeof(cipher)/sizeof(cipher[0]); i++)
		buf[i] = rand() ^ cipher[i];
	printf("%s\n", buf);
	return (0);
}
