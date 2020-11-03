function cipher(msg, offset) {
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetArray = Array.from(alphabet);
    encodedArray = []
    msg = Array.from(msg)
    msg.forEach((letter) => {
        alphabetArrayLength = alphabetArray.length;
        indx = alphabetArray.indexOf(letter) 
        
        if (indx == -1) {
            encodedArray.push(letter)
        } else if(indx + offset < alphabetArrayLength) {
            encodedArray.push(alphabetArray[indx+offset])
        } else {
            indx = indx + offset - alphabetArrayLength;
            encodedArray.push(alphabetArray[indx])
        }
    });

    cipheredMsg = encodedArray.join('')
    return cipheredMsg
}
myMsg = 'I really love Ariel, my little cat. ';

input = document.querySelector('.caesarCipher>p.input')
input.textContent = myMsg

output = document.querySelector('.caesarCipher>p.output');
output.textContent = cipher(myMsg, 13)
