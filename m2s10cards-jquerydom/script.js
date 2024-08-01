$(document).ready(function () {
    const destinosInfo = {
        "Buenos Aires": {
            "img": "img/Buenos aires.jpg",
            "titulo": "Buenos Aires",
            "descripcion": "Descubre la magia de Buenos Aires, la vibrante capital de Argentina. Sus calles empedradas, su apasionado tango, su deliciosa gastronomía y su rica historia cultural te esperan."
        },
        "Machu Picchu": {
            "img": "img/machu pichu.jpg",
            "titulo": "Machu Picchu",
            "descripcion": "Explora las majestuosas ruinas incas de Machu Picchu en Perú. Este sitio histórico ofrece vistas impresionantes y una experiencia inolvidable para los aventureros."
        },
        "Río de Janeiro": {
            "img": "img/Rio de janeiro.jpg",
            "titulo": "Río de Janeiro",
            "descripcion": "Disfruta de las playas soleadas, el vibrante carnaval y la icónica estatua del Cristo Redentor en Río de Janeiro, Brasil. La ciudad ofrece una mezcla única de cultura y naturaleza."
        }
    };

    $('.ver-mas').on('click', function (event) {
        event.preventDefault();
        const destino = $(this).closest('.card').data('destino');
        const info = destinosInfo[destino];

        $('#info-contenido').html(`
            <img src="${info.img}" class="img-fluid mb-3" alt="${info.titulo}">
            <h2>${info.titulo}</h2>
            <p>${info.descripcion}</p>
        `);

        $('#info-recuadro').removeClass('recuadro-oculto');
    });

    $('#cerrar-recuadro').on('click', function () {
        $('#info-recuadro').addClass('recuadro-oculto');
    });

    $('#info-recuadro').on('click', function (event) {
        if (event.target === this) {
            $(this).addClass('recuadro-oculto');
        }
    });
});
