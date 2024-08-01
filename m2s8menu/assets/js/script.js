function menu() {
    let opcion = prompt("¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel.\nEstoy aquí para ayudarte en lo que necesides.\nEscribe el número de la opción que buscas:\n1. Boletas y Pagos\n2. Señal y llamadas\n3. Oferta comercial\n4. Otras consultas\n5. Salir");
  
    switch (opcion) {
      case "1":
        boletasYPagos();
        break;
      case "2":
        senalYLlamadas();
        break;
      case "3":
        ofertaComercial();
        break;
      case "4":
        otrasConsultas();
        break;
      case "5":
        alert("Fin de ejecución.");
        break;
      default:
        alert("Opción no válida, por favor intenta nuevamente.");
        menu();
    }
  }
  
  function boletasYPagos() {
    let opcion = prompt("Selecciona una opción:\n1. Ver Boleta\n2. Pagar Cuenta");
  
    switch (opcion) {
      case "1":
        alert("Haga click para descargar su boleta");
        break;
      case "2":
        alert("Usted está siendo transferido, por favor espere");
        break;
      default:
        alert("Opción no válida, por favor intenta nuevamente.");
        boletasYPagos();
    }
  }
  
  function senalYLlamadas() {
    let opcion = prompt("Selecciona una opción:\n1. Problemas con la señal\n2. Problemas con las llamadas");
  
    switch (opcion) {
      case "1":
        alert("Guía de conexión");
        break;
      case "2":
        alert("Detalles");
        break;
      default:
        alert("Opción no válida, por favor intenta nuevamente.");
        senalYLlamadas();
    }
  }
  
  function ofertaComercial() {
    alert("Un ejecutivo se contactará con usted en la brevedad");
  }
  
  function otrasConsultas() {
    let consulta = prompt("A continuación, escriba su consulta:");
    alert("Su consulta ha sido ingresada con éxito");
  }
  
  menu();