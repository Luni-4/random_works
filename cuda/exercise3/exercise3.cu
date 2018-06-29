#include "common/common.h"
#include <cuda_runtime.h>
#include <stdio.h>
#include <math.h>

#define M_PI 3.14159265358979323846


__global__ void tabular(float *a) {
	int i = threadIdx.x + blockIdx.x * blockDim.x;
	//if (i < n) {
		float x = a[i];
		float s = sinf(x);
		float c = cosf(x);
		a[i] = sqrtf(abs(s * s - c * c));
	//}
}

int main(int argc, char **argv) {
	cudaEvent_t start, stop;

	float *h_a, *hp_a;
	float *d_a;
	int N = 1<<15;
	int M = 1<<12;
	int blockSize = 1024;

	// start the timers
	cudaEventCreate(&start);
	cudaEventCreate(&stop);

	int nStreams = N / M;

	int nBytes =  N * sizeof(float);
	int bytesPerStream = M * sizeof(float);

	// malloc host memory
	h_a = (float *) malloc(nBytes);

	// malloc device memory
	//cudaMalloc((void**) &d_a, nBytes);

	CHECK( cudaMallocHost((void**)&hp_a, nBytes) ); // host pinned
	CHECK( cudaMalloc((void**)&d_a, nBytes) );  // device

	float step = M_PI / N;

	for(int i = 0; i < N; i++){
		h_a[i] = i * step;
	}

	// creazione degli stream asincroni non-NULL
	cudaStream_t streams[nStreams];

	for (int i = 0; i < nStreams; ++i) {
		CHECK(cudaStreamCreate(&streams[i]));
	}

	cudaEventRecord(start, 0);

	double iStart, iElaps;
	iStart = seconds();

	for (int i = 0; i < nStreams; i++) {
		int offset = i * bytesPerStream;
		cudaMemcpyAsync(&d_a[offset], &h_a[offset], bytesPerStream, cudaMemcpyHostToDevice, streams[i]);
		tabular<<<M / blockSize, blockSize, 0, streams[i]>>>(d_a);
		cudaMemcpyAsync(&h_a[offset], &d_a[offset], bytesPerStream, cudaMemcpyHostToDevice, streams[i]);
	}

	for (int i = 0; i < nStreams; i++) {
		cudaStreamSynchronize(streams[i]);
	}

	iElaps = seconds() - iStart;

	// Registro i tempi
	cudaEventRecord(stop);

	// Sincronizzo i tempi
	cudaEventSynchronize(stop);

	// cleaup finale
	for (int i = 0; i < nStreams; ++i)
		CHECK(cudaStreamDestroy(streams[i]));

	// Stampa a
	for(int i = 0; i < N; i++){
			printf("%f\n",h_a[i]);
	}

	// calculate the elapsed time between two events
	float time;
	cudaEventElapsedTime(&time, start, stop);

	printf("Tempo CPU: %f\n", iElaps);
	printf("Tempo Gpu: %f\n",time);

	// free memories both host and device
	cudaEventDestroy(start);
	cudaEventDestroy(stop);
	free(h_a);
	cudaFreeHost(hp_a);
	CHECK(cudaFree(d_a));

	// reset device
	CHECK(cudaDeviceReset());
	return EXIT_SUCCESS;
}
