#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 1000

void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[N];
    srand(time(NULL));

    for (int i = 0; i < N; i++) {
        arr[i] = rand() % 1000;
    }

    clock_t start = clock();
    bubble_sort(arr, N);
    clock_t end = clock();

    double runtime = (double)(end - start) / CLOCKS_PER_SEC;
    printf("%f\n", runtime);
    return 0;
}

