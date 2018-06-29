/*
 ============================================================================
 Name        : Esercizio3.cu
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : CUDA compute reciprocals
 ============================================================================
 */

#include <stdio.h>
#include <cuda_runtime.h>
#define N 1024 // vector size
#define TxB 32 // threads x block

/*
* kernel: somma di vettori
*/
 /*__global__ void add_vect(int *a, int *b, int *c) {
	int idx = blockDim.x * blockIdx.x + threadIdx.x;
	if (idx < N)
		c[idx] = a[idx] + b[idx];
}*/

__global__ void add_mat(int *a, int *b, int *c) {
	int ix = blockDim.x * blockIdx.x + threadIdx.x;
	int iy = blockDim.y * blockIdx.y + threadIdx.y;
	int idx = iy * gridDim.x + ix;
	if (ix < gridDim.x || iy < gridDim.y)
 		c[idx] = a[idx] + b[idx];
 }


int main(void) {
	const int dimx1 = 80;
	const int dimy1 = 64;
	const int dimx2 = 76;
	const int dimy2 = 62;

	int *a, *b, *c;
	int *dev_a, *dev_b, *dev_c;
	int nBytes1 = (dimx1 * dimy1) * sizeof(int);
	int nBytes2 = (dimx2 * dimy2) * sizeof(int);


	// malloc host memory
	a = (int *) malloc(nBytes1);
	b = (int *) malloc(nBytes2);
	c = (int *) malloc(nBytes2);

	// malloc device memory
	cudaMalloc((void**) &dev_a, nBytes1);
	cudaMalloc((void**) &dev_b, nBytes2);
	cudaMalloc((void**) &dev_c, nBytes2);

	// fill the arrays 'a' and 'b' on the CPU
	memset(a, 1, nBytes1);
	memset(b, 1, nBytes2);
	memset(c, 1, nBytes2);

	// copy the arrays 'a' and 'b' to the GPU
	cudaMemcpy(dev_a, a, nBytes1, cudaMemcpyHostToDevice);
	cudaMemcpy(dev_b, b, nBytes2, cudaMemcpyHostToDevice);

	dim3 dimBlock(16,16,1);
	dim3 dimGrid(5,4,1);

	add_mat<<<dimBlock, dimGrid>>>(dev_a, dev_b, dev_c);
	// copy the array 'c' back from the GPU to the CPU
	cudaMemcpy(c, dev_c, nBytes2, cudaMemcpyDeviceToHost);
	// display the results
	for (int i = 0; i < (dimx2*dimy2); i++) {
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

