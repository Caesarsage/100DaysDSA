const smallest_subarray_sum = function(s, arr) {
  // TODO: Write your code here
  let min = Infinity
  let curr_sum = 0
  let start = 0

  for(let end=0; end < arr.length; end++) {
    curr_sum += arr[end]

    while(end >= s) {
      min = Math.min(min, end - start + 1)
      curr_sum -= arr[start]
      start +=1
    }
  }
  return min;
};

