#include "nmpp.h"
#include "time.h"
#include "stdio.h"
#include "stdlib.h"

#pragma data_section ".data_imu0"
    long long im1[2048];
#pragma data_section ".data_imu1"
    long long im2[2048];
#pragma data_section ".data_imu2"
    long long im3[2048];
#pragma data_section ".data_imu3"
    long long im4[2048];

#pragma data_section ".data_emi"
    long long emi[2048];

int main()
{
	printf("sdf");
  return 0;
}
