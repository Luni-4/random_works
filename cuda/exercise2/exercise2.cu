/*
 ============================================================================
 Name        : Esercizio2.cu Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : CUDA compute reciprocals
 ============================================================================
 */

#include <stdio.h>
#include <cuda_runtime.h>
/*
* Mostra DIMs e IDs di grid, block e thread
*/
__global__ void checkIndex(void) {
	if ((threadIdx.x + threadIdx.y) % 5 == 0) {
	printf("threadIdx:(%d, %d, %d) blockIdx:(%d, %d, %d) "
			"blockDim:(%d, %d, %d) gridDim:(%d, %d, %d)\n",
			threadIdx.x, threadIdx.y, threadIdx.z,
			blockIdx.x, blockIdx.y, blockIdx.z,
			blockDim.x, blockDim.y, blockDim.z,
			gridDim.x,gridDim.y,gridDim.z);
	}
}

int main(int argc, char **argv) {
	// definisce grid e struttura dei blocchi
	dim3 block(8, 7, 1);
	dim3 grid(2, 2, 1);
	// controlla dim. dal lato host
	printf("grid.x %d grid.y %d grid.z %d\n", grid.x, grid.y, grid.z);
	printf("block.x %d block.y %d block.z %d\n", block.x, block.y, block.z);
	// controlla dim. dal lato device
	checkIndex<<<grid, block>>>();
	// reset device
	cudaDeviceReset();
	return(0);
}
