#include <iostream>
using namespace std;

int candidates[100];
int comb[100];           
int N, target;
int found = 0;           

void print_comb(int len) {
    cout << "{ ";
    for(int i = 0; i < len; i++) {
        cout << comb[i];
        if(i < len-1) cout << " ";
    }
    cout << " }" << endl;
}

void solve(int start, int sum_so_far, int pos) {
    if(sum_so_far == target) {
        print_comb(pos);
        found = 1;
        return;
    }
    
    if(sum_so_far > target) {
        return;
    }
    
    for(int i = start; i < N; i++) {
        comb[pos] = candidates[i];
        solve(i, sum_so_far + candidates[i], pos + 1);
    }
}

int main() {
    cout << "Enter number of candidates: ";
    cin >> N;

    cout << "Enter the candidates: ";
    for(int i = 0; i < N; i++) {
        cin >> candidates[i];
    }

    cout << "Enter the target: ";
    cin >> target;

    for(int i = 0; i < N-1; i++) {
        for(int j = 0; j < N-i-1; j++) {
            if(candidates[j] > candidates[j+1]) {
                int temp = candidates[j];
                candidates[j] = candidates[j+1];
                candidates[j+1] = temp;
            }
        }
    }

    cout << "Combinations are:" << endl;
    
    solve(0, 0, 0);

    if(found == 0) {
        cout << "No combination found." << endl;
    }

    return 0;
}