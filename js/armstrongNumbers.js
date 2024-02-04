// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function() {
    
};

function createArrayOfNum(maxValue) {
    return [...Array(maxValue).keys()];
  }


function findArmstrongNumbers(arr) {
    let answer = [];
    for (let i = 0; i < arr.length; i++) {
        let numCompare = arr[i];
        let strNum = arr[i].toString();
        let digits = [];
        let num = 0;
        // console.log('numCompare:', numCompare);
        // console.log('strNum:', strNum);

        for (let j = 0; j < strNum.length; j++) {
            digits.push(parseInt(strNum[j]));
        }
        // console.log('digits:', digits)

        for (let j = 0; j < digits.length; j++) {
            let singleDigit = digits[j];
            let expo = digits.length
            num += Math.pow(singleDigit, expo)
        }
        // console.log('num:', num);

        if (num === numCompare) {
            answer.push(num)
        }
    }

    return answer;
}

console.log(findArmstrongNumbers(createArrayOfNum(999)))