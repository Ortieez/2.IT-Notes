function bubblesort(arr){
    var swapped;
    do {
        swapped = false;
        for (var i = 0; i < arr.length; i++) {
        if (arr[i] > arr[i+1]) {
            var temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
            swapped = true;
        }
        }
    } while (swapped);
    console.log(arr);
}

var arr = [];
for (var i = 0; i < 10; i++) {
    arr.push(Math.floor(Math.random() * 100));
}

bubblesort(arr);