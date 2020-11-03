console.log('madlib.js is up and running')

function madlib(name, subject) {
    return `${name}'s favorite subject is ${subject}.`
}

myName = 'Wes'
mySubject = 'WebDev'
console.log(madlib(myName, mySubject))

myMadLib = document.querySelector('p:first-of-type');
myMadLib.textContent = madlib(myName, mySubject)



