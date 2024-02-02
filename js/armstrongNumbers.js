// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function() {
    
};

function findArmstrongNumbers(num) {
    let strNum = num.toString();
    let digits = [];
    let answer = 0;

    for (let i = 0; i < strNum.length; i++) {
        digits.push(parseInt(strNum[i]));
    }

    for (let i = 0; i < digits.length; i++) {
        answer += digits[i] * strNum.length;
    }
    
    return answer
}

console.log(findArmstrongNumbers(16))