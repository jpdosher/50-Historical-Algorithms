
function quickSort(arr) {
    if (arr.length <= 1) { //caso base
        return arr;
    }
    var pivot = arr[Number(arr.length/2)];
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

console.log(quickSort([10, 50, 2, 3, 1]))