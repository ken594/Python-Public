/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected3 = true;

const queue4 = [];
const expected4 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */
function socialDistancingEnforcer(queue) {
    if (queue.length < 1) return true;
    let seen = [];
    for (let i=0; i < queue.length; i++) {
        if (queue[i] == 1) {
            seen.push(i);
        }
    }
    for (let i = seen.length - 1; i > 1; i--) {
        if (seen[i] - seen[i-1] < 6) return false;
    }
    return true;
    // let res = true;
    // let mode = 0;
    // for (let i = 0; i < queue.length; i++) {
    //     while (queue[i] == 0 && mode == 0) {
    //         i++;
    //     }
    //     if (queue[i] == 1) {
    //         mode = 1;
    //         let start = i;
    //         let end = i++;
    //         while (queue[end] != 1 && end < queue.length) {
    //             i++;
    //         }
            
    //     }
    // }
    // console.log(seen);
}

// socialDistancingEnforcer(queue2);

console.log(socialDistancingEnforcer(queue1)) // false
console.log(socialDistancingEnforcer(queue2)) // true
console.log(socialDistancingEnforcer(queue3)) // true
console.log(socialDistancingEnforcer(queue4)) // true

/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/ //[4,1,0,5]
// 0   1  2  3  4
const numsA = [-2, 5, 7, 0, 3];
const expectedA = 2;

const numsB = [9, 9];
const expectedB = -1;

const numsC = [1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1]
const expectedC = 5





/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
    if (nums.length < 3) return -1;
    let sum = 0;
    for (let num of nums) {
        sum += num;
    }
    let left = nums[0];
    let right = sum-nums[0];
    for (let i=1; i < nums.length; i++) {
        right -= nums[i];
        if (left == right) return i;
        left += nums[i];
    }
    return -1;
}

console.log(balanceIndex(numsA)) // 2
console.log(balanceIndex(numsB)) // -1
console.log(balanceIndex(numsC)) // 5