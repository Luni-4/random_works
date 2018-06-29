#include "common/common.h"
#include <cuda_runtime.h>
#include <stdio.h>
#include <math.h>

#define N 32
#define TxB 32

__global__ void scan_GPU(float *x, float *y){
	__shared__ float smem[TxB];
	unsigned int tid = threadIdx.x + blockIdx.x * blockDim.x;

	if (tid < N)
		smem[threadIdx.x] = x[tid];

	// albero di riduzione: scan iterativo
	for (unsigned int stride = 1; stride <= threadIdx.x; stride *= 2) {
		__syncthreads();
		smem[threadIdx.x] += smem[threadIdx.x - stride];
	}

	y[tid] = smem[threadIdx.x];
}

int main(int argc, char **argv) {
	cudaEvent_t start, stop;

	float *h_a, *h_b;
	float *d_a, *d_b;

	// start the timers
	cudaEventCreate(&start);
	cudaEventCreate(&stop);

	int nBytes = N  * sizeof(float);

	// malloc host memory
	h_a = (float *) malloc(nBytes);
	h_b = (float *) malloc(nBytes);

	// fill the arrays 'a' on the CPU
	for	(int i= 0; i< N; i++) {
			h_a[i] = i;
	}

	CHECK(cudaMalloc((void**)&d_a, nBytes));  // device
	CHECK(cudaMalloc((void**)&d_b, nBytes));  // device

	cudaMemcpy(d_a, h_a, nBytes, cudaMemcpyHostToDevice);

	cudaEventRecord(start, 0);

	scan_GPU<<<N/TxB, TxB>>>(d_a, d_b);

	cudaDeviceSynchronize();

	cudaMemcpy(h_b, d_b, nBytes, cudaMemcpyDeviceToHost);

	// Registro i tempi
	cudaEventRecord(stop);

	// Sincronizzo i tempi
	cudaEventSynchronize(stop);

	for	(int i= 0; i< N; i++) {
			printf("%.0f ",h_b[i]);
	}

	// calculate the elapsed time between two events
	float time;
	cudaEventElapsedTime(&time, start, stop);

	printf("Tempo Gpu: %f\n",time);

	// free memories both host and device
	cudaEventDestroy(start);
	cudaEventDestroy(stop);
	free(h_a);
	free(h_b);
	CHECK(cudaFree(d_a));
	CHECK(cudaFree(d_b));

	// reset device
	CHECK(cudaDeviceReset());
	return EXIT_SUCCESS;
}
