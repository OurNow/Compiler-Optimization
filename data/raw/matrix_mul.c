#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100

void matrix_mul(int A[N][N], int B[N][N], int C[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            C[i][j] = 0;
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    int A[N][N], B[N][N], C[N][N];
    srand(time(NULL));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] = rand() % 10;
            B[i][j] = rand() % 10;
        }
    }

    clock_t start = clock();
    matrix_mul(A, B, C);
    clock_t end = clock();

    double runtime = (double)(end - start) / CLOCKS_PER_SEC;
    printf("%f\n", runtime);
    return 0;
}

