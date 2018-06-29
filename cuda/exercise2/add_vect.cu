/**
 * Copyright 1993-2012 NVIDIA Corporation.  All rights reserved.
 *
 * Please refer to the NVIDIA end user license agreement (EULA) associated
 * with this source code for terms and conditions that govern your use of
 * this software. Any use, reproduction, disclosure, or distribution of
 * this software and related documentation outside the terms of the EULA
 * is strictly prohibited.
 */

#include <stdio.h>
#include <cuda_runtime.h>
#define N 1024 // vector size
#define TxB 32 // threads x block

/*
* kernel: somma di vettori
*/
__global__ void add_vect(int *a, int *b, int *c) {
	int idx = blockDim.x * blockIdx.x + threadIdx.x;
	if (idx < N)
		c[idx] = a[idx] + b[idx];
}


int main(void) {
	int *a, *b, *c;
	int *dev_a, *dev_b, *dev_c;
	int nBytes = N * sizeof(int);


	// malloc host memory
	a = (int *) malloc(nBytes);
	b = (int *) malloc(nBytes);
	c = (int *) malloc(nBytes);

	// malloc device memory
	cudaMalloc((void**) &dev_a, nBytes);
	cudaMalloc((void**) &dev_b, nBytes);
	cudaMalloc((void**) &dev_c, nBytes);

	// fill the arrays 'a' and 'b' on the CPU
	for	(int i= 0; i< N; i++) {
		a[i] =	rand() % 10;
		b[i] = 	rand() % 10;
	}

	// copy the arrays 'a' and 'b' to the GPU
	cudaMemcpy(dev_a, a, nBytes, cudaMemcpyHostToDevice);
	cudaMemcpy(dev_b, b, nBytes, cudaMemcpyHostToDevice);


	add_vect<<<N /TxB, TxB>>>(dev_a, dev_b, dev_c);

	// copy the array 'c' back from the GPU to the CPU
	cudaMemcpy(c, dev_c, nBytes, cudaMemcpyDeviceToHost);

	// display the results
	for (int i = 0; i < N; i++) {
		printf("%d\n", c[i]);
	}

	// Free host memory
	free(a);
	free(b);
	free(c);
	// free the memory allocated on the GPU
	cudaFree(dev_a);
	cudaFree(dev_b);
	cudaFree(dev_c);

	return 0;

}
