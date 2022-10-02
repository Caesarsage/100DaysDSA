function countUniqueChars(str) {
  let uniqueChars = new Set();
  for (let char of str) {
    uniqueChars.add(char);
  }
  return uniqueChars.size;
}

function SearchingChallenge(str) {
  // code goes here
  const k = Number(str[0]);
  str = str.slice(1);

  for (let size = str.length; size > 0; size--) {
    for (let i = 0; i <= str.length - size; i++) {
      let subStr = str.slice(i, i + size);
      if (countUniqueChars(subStr) === k) {
        let ans = (subStr + "psqow8ba42").split("");
        // return ans
        for (i = 3; i < ans.length; i += 4) {
          ans[i] = "_";
        }
        return ans.join("");
      }
    }
  }
}

// keep this function call here
console.log(SearchingChallenge(readline()));
