//Selection Sort
#include<stdio.h>
void main(){
    int n,i,j,temp,a[100];
    printf("Enter the number of elements:");
    scanf("%d",&n);
    printf("Enter the elements:");
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++){
        for(j=i+1;j<n;j++){
            if(a[i]>a[j]){
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
    printf("Sorted array:");
    for(i=0;i<n;i++)
        printf("%d ",a[i]);
}
//Time Complexity: O(n^2)
//Space Complexity: O(1)
//The above code sorts the array in ascending order using the Selection Sort algorithm.
//The key steps are:
//1. Find the minimum element in the unsorted array
//2. Swap it with the first element of the unsorted array
//3. Repeat the process for the remaining elements
//4. The array will be sorted in ascending order
//5. Print the sorted array
//6. End of the program
