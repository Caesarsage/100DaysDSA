function longest_substring_with_k_dinstnct(str, k) {
  let windowStart = 0
  let maxLength = 0
  let charsFreq = {}

  // first we make a hash map to keep track of the characters and their frequencies
  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    const rightChar = str[windowEnd]
    
    if (!(rightChar in charsFreq)) {
      charsFreq[rightChar] = 0
    }
    charsFreq[rightChar]++

    // shrink the window until we are left with k distinct characters
    while (Object.keys(charsFreq).length > k) {
      const leftChar = str[windowEnd]
      charsFreq[leftChar] -= 1
      
      if (charsFreq[leftChar] === 0) {
        delete charsFreq[leftChar]
      }
      windowStart++
    }
    maxLength= Math.max(maxLength, windowEnd - windowStart + 1)
    
    
  }
}