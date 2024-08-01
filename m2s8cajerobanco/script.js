const clientes = [
    { nombre: 'Juan Perez', identificador: 'jperez', clave: '1234', saldo: 5000 },
    { nombre: 'Ana Gómez', identificador: 'agomez', clave: 'abcd', saldo: 3000 },
    { nombre: 'Luis Martinez', identificador: 'lmartinez', clave: '5678', saldo: 7000 }
];

let clienteActual = null;

function login() {
    const identificador = document.getElementById('identificador').value;
    const clave = document.getElementById('clave').value;
    const cliente = clientes.find(c => c.identificador === identificador && c.clave === clave);

    if (cliente) {
        clienteActual = cliente;
        document.getElementById('login').style.display = 'none';
        document.getElementById('menu').style.display = 'block';
        document.getElementById('welcomeMessage').innerText = `Bienvenido/a ${cliente.nombre}`;
    } else {
        document.getElementById('loginError').innerText = 'Identificador o clave incorrectos';
    }
}

function mostrarSaldo() {
    document.getElementById('acciones').innerHTML = `<p>Saldo actual: ${clienteActual.saldo}</p>`;
}

function realizarGiro() {
    const monto = prompt('Ingrese el monto a girar:');
    const montoGiro = parseFloat(monto);
    if (isNaN(montoGiro) || montoGiro <= 0) {
        alert('Monto inválido');
        return;
    }
    if (montoGiro > clienteActual.saldo) {
        alert('Saldo insuficiente');
    } else {
        clienteActual.saldo -= montoGiro;
        alert('Giro realizado con éxito');
        mostrarSaldo();
    }
}

function realizarDeposito() {
    const monto = prompt('Ingrese el monto a depositar:');
    const montoDeposito = parseFloat(monto);
    if (isNaN(montoDeposito) || montoDeposito <= 0) {
        alert('Monto inválido');
        return;
    }
    clienteActual.saldo += montoDeposito;
    alert('Depósito realizado con éxito');
    mostrarSaldo();
}

function salir() {
    clienteActual = null;
    document.getElementById('login').style.display = 'block';
    document.getElementById('menu').style.display = 'none';
    document.getElementById('identificador').value = '';
    document.getElementById('clave').value = '';
    document.getElementById('loginError').innerText = '';
    document.getElementById('acciones').innerHTML = '';
}
