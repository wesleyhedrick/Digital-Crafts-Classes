function decipher(msg, offset) {
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetArray = Array.from(alphabet);
    decodedArray = []
    msg = Array.from(msg)

    msg.forEach((letter) => {
        alphabetArrayLength = alphabetArray.length;
        indx = alphabetArray.indexOf(letter) 
        
        if (indx == -1) {
            decodedArray.push(letter)
        } else if(indx - offset > -1) {
            decodedArray.push(alphabetArray[indx-offset])
        } else {
            indx = indx - offset + alphabetArrayLength;
            decodedArray.push(alphabetArray[indx])
        }
    });

    decipheredMsg = decodedArray.join('')
    return decipheredMsg
    // return 'hello world'
}

myMsg = 'V ErnyyL yBIr NEvry, zL yvGGyr pnG.';
input = document.querySelector('.caesarCipher2>p.input')
input.textContent = myMsg
output = document.querySelector('.caesarCipher2>p.output');
output.textContent = decipher(myMsg, 13)
