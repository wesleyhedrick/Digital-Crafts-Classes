function printNums(a, b) {
    printNumbers = document.querySelector('.printNumbers');
    let p;
    numArray = []
    for (i = a; i < b+1; i++) {
        p = document.createElement('p')
        p.textContent = i;
        printNumbers.append(p)
    }
}

printNums(1, 10);