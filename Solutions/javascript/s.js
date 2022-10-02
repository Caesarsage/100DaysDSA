
// Javascript program to find the longest
// substring with k unique characters in
// a given string
let MAX_CHARS = 26;

// This function calculates number of
// unique characters using a associative
// array count[]. Returns true if no. of
// characters are less than required else
// returns false.
function isValid(count, k) {
	let val = 0;
	for(let i = 0; i < MAX_CHARS; i++)
	{
		if (count[i] > 0)
		{
			val++;
		}
	}

	// Return true if k is greater
	// than or equal to val
	return (k >= val);
}

// Finds the maximum substring
// with exactly k unique chars
function kUniques(s){
	
	// Number of unique characters
  let k = s[0]
	let u = 0;
	let n = s.length;
	let count = new Array(MAX_CHARS);
	
	for(let i = 0; i < MAX_CHARS; i++){
		count[i] = 0;
	}
	
	// Traverse the string, Fills
	// the associative array
	// count[] and count number
	// of unique characters
  for (let i = 0; i < n; i++){
		if (count[s[i].charCodeAt(0) - 'a'.charCodeAt(0)] == 0){
			u++ 
		}
		count[s[i].charCodeAt(0) -
			'a'.charCodeAt(0)]++ 
	}

	// If there are not enough
	// unique characters, show
	// an error message.
	if (u < k){
		console.log("Not enough unique characters")
		return 
	}

	// Otherwise take a window with
	// first element in it.
	// start and end variables.
	let curr_start = 0, curr_end = 0 

	// Also initialize values for
	// result longest window
	let max_window_size = 1
	let max_window_start = 0 

	// Initialize associative
	// array count[] with zero
  for (let i = 0; i < MAX_CHARS; i++){
		count[i] = 0;
	}
	
	// put the first character
	count[s[0].charCodeAt(0) -
		'a'.charCodeAt(0)]++;

	// Start from the second character and add
	// characters in window according to above
	// explanation
	for(let i = 1; i < n; i++){
		
		// Add the character 's[i]'
		// to current window
		count[s[i].charCodeAt(0) - 'a'.charCodeAt(0)]++;
		curr_end++;

		// If there are more than k
		// unique characters in
		// current window, remove from left side
		while (!isValid(count, k)){
			count[s[curr_start].charCodeAt(0) -
							'a'.charCodeAt(0)]--;
			curr_start++;
		}

		// Update the max window size if required
		if (curr_end - curr_start + 1 > max_window_size){
			max_window_size = curr_end - curr_start + 1;
			max_window_start = curr_start;
		}
	}

	console.log("Max substring is : " +
				s.substring(max_window_start,
				max_window_start +
				max_window_size + 1) +
				" with length " + max_window_size);
}

// Driver Code
let s = "3aabacbebee";
// let k = 2;

kUniques(s)

// This code is contributed by rag212