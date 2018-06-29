#include <stdio.h>
#include <cuda_runtime.h>
#define N 1024 // vector size
#define TxB 32 // threads x block

/*
* kernel: branch
*/


__global__ void pari_dispari_1(int *c) {
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	int a,b;
	a = b = 0;

	if (tid % 2 == 0)
		a = 2;
	else
		b = 1;
	c[tid] = a + b;
}



int main(void) {
	int *c;
	int *dev_c;
	int	nBytes = N * sizeof(int);

	// malloc host memory
	c = (int *)malloc(nBytes);

	// malloc device memory
	cudaMalloc((void**) &dev_c, nBytes);

	pari_dispari_1<<<N, TxB>>>(dev_c);

	// copy the array 'c' back from the GPU to the CPU
	cudaMemcpy(c, dev_c, nBytes, cudaMemcpyDeviceToHost);

	// display the results
	for (int i = 0; i < N; i++) {
		printf("%d\n", c[i]);
	}

	// Free host memory
	free(c);
	// free the memory allocated on the GPU
	cudaFree(dev_c);

	return 0;

}
