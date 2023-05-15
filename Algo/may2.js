/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(N).
 * - Space: O(1).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */

function reverseString(str) {
  var newStr = "";
  for (var i = str.length - 1; i >= 0; i--) {
    newStr += str[i];
  }
  return newStr;
}

function reverseString(str) {
  result = "";
  for (let i in str) {
    result = str[i] + result;
  }
  return result;
}

// build-in
//   split method to return a new array
//   reverse method to reverse the new created array
//   join method to join all elements into a string
// function reverseString(str) {
//   return str.split("").reverse().join("");
// }

//TEST CODE FOR REVERSE
console.log(reverseString(str1)); // Expected: erutaerc
console.log(reverseString(str2)); // Expected: god
console.log(reverseString(str3)); // Expected: olleh
console.log(reverseString(str4)); // Expected: ""

// function reverseString(str) {
//   if (str === "") return "";
//   else return reverseString(str.substr(1)) + str.charAt(0);
// }

// python
// def reverseString(str):
//   newStr = ""
//   for char in str:
//     newStr = char + newStr
//   return newStr
