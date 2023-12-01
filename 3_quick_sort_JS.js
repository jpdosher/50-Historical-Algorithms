//quicksort in JavaScript
function quickSort(arr) {
    if (arr.length <= 1) { //cao base
        return arr;
    }
    var pivot = arr[0];
    var left = [];
    var right = [];
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }
    return quickSort(left).concat(pivot, quickSort(right));
    
}

console.log(quickSort([10, 5, 2, 3]))