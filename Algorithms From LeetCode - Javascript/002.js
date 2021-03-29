// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Example 1:

// Input: 121
// Output: true
// Example 2:

// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
// Follow up:

// Coud you solve it without converting the integer to a string?

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0){
        return false;
    }
    let newX = x;
    let listX = [];
    let countX = 0;
    if(x < 100 && x > 9 && Math.floor(x/11) != x/11){
        return false;
    }
    while( newX > 0){
        while( newX / 10 != Math.floor(newX/10)){
            newX--;
            countX++;
        }
        listX.push(countX);
        countX = 0;
        newX /= 10;
    }
    for(i = 0; i < Math.floor(listX.length/2) ; i++ ){
        if(listX[i] != listX[listX.length-i-1]){
            return false;
        }
    }
    console.log(listX);
    return true;
};