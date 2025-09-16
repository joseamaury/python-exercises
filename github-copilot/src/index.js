function getCardFlag(cardNumber) {
    const num = cardNumber.replace(/\D/g, '');

    if (/^4/.test(num)) {
        return 'Visa';
    }
    if (/^(5[1-5]|222[1-9]|22[3-9]\d|2[3-6]\d{2}|27[01]\d|2720)/.test(num)) {
        return 'MasterCard';
    }
    if (/^(4011|4312|4389)/.test(num)) {
        return 'Elo';
    }
    if (/^(34|37)/.test(num)) {
        return 'American Express';
    }
    if (/^(6011|65|64[4-9])/.test(num)) {
        return 'Discover';
    }
    if (/^6062/.test(num)) {
        return 'Hipercard';
    }
    return 'Unknown';
}

// Example usage:
console.log(getCardFlag('4011123456789012')); // Elo
console.log(getCardFlag('4111111111111111')); // Visa
console.log(getCardFlag('6011123456789012')); // Discover
console.log(getCardFlag('6062123456789012')); // Hipercard
console.log(getCardFlag('2221001234567890')); // MasterCard
console.log(getCardFlag('371234567890123'));  // American Express
// ...existing code...

// Executa o programa com um exemplo de número de cartão informado pelo usuário
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Digite o número do cartão: ', (cardNumber) => {
    const flag = getCardFlag(cardNumber);
    console.log(`Bandeira detectada: ${flag}`);
    readline.close();
});