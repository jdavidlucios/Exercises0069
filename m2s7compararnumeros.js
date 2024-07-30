const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Ingresa el primer número: ', (input1) => {
    const numero1 = parseFloat(input1);

    rl.question('Ingresa el segundo número: ', (input2) => {
        const numero2 = parseFloat(input2);

        if (numero1 > numero2) {
            console.log("El número " + numero1 + " es mayor que el número " + numero2);
        } else if (numero2 > numero1) {
            console.log("El número " + numero2 + " es mayor que el número " + numero1);
        } else {
            console.log("Ambos números son iguales: " + numero1);
        }

        rl.close();
    });
});
