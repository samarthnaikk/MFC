#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

void bubble_sort(vector<int>& arr) {
    int n = arr.size();
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

void selection_sort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = temp;
    }
}

void insertion_sort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void manual_sort(vector<int>& arr) {
    int n = arr.size();
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

double measure_time(void (*sort_function)(vector<int>&), vector<int> arr) {
    clock_t start_time = clock();
    sort_function(arr);
    return double(clock() - start_time) / CLOCKS_PER_SEC;
}

int main() {
    int size = 1000;
    vector<int> test_array(size);
    for (int& num : test_array) {
        num = rand() % 10000 + 1;
    }
    vector<pair<string, void (*)(vector<int>&)>> algorithms = {
        {"Bubble Sort", bubble_sort},
        {"Selection Sort", selection_sort},
        {"Insertion Sort", insertion_sort},
        {"Manual Sort", manual_sort}
    };
    for (auto& algo : algorithms) {
        vector<int> arr_copy = test_array;
        double time_taken = measure_time(algo.second, arr_copy);
        cout << algo.first << ": " << time_taken << " seconds" << endl;
    }
    return 0;
}
