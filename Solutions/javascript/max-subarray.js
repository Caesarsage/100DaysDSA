function max_subarray_of_sze_k(arr,k) {
  let curr_sum = 0;
  let max_sum = 0;
  let curr_start = 0

  for (let curr_end = 0; arr.length > curr_end; curr_end++) {
    curr_sum += arr[curr_end];
    if (curr_end >= k - 1) {
      max_sum = Math.max(max_sum, curr_sum); // update max_sum
      // sliding window
      curr_sum -= arr[curr_start]; // remove the first element
      curr_start++; // move the start pointer (sliding window)
    }
  }
}