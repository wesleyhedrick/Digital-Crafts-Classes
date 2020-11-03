function positiveNumbers(num) {
    return num > 0;
}
myArray = [-1,2,3,-5,10]
myFilteredArray = myArray.filter(positiveNumbers);

posNumbers = document.querySelector('.positiveNumbers');
let p = document.createElement('p');
p.textContent = `Original Array: ${myArray}`;
posNumbers.append(p)

p = document.createElement('p');
p.textContent = `Array with all the negatives taken out: ${myFilteredArray}`
posNumbers.append(p);

