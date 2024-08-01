// Obtener los elementos del DOM
const text1 = document.getElementById('text1');
const text2 = document.getElementById('text2');
const caja2 = document.getElementById('caja2');
const img = document.getElementById('img');
const caja3 = document.getElementById('caja3');

// Agregar evento mouseover y mouseout a text1
text1.addEventListener('mouseover', () => {
  text2.style.display = 'block';
});

text1.addEventListener('mouseout', () => {
  text2.style.display = 'none';
});

// Agregar evento click a caja2
caja2.addEventListener('click', () => {
  img.style.width = '100%';
});

caja2.addEventListener('mouseleave', () => {
  img.style.width = '20%';
});

// Agregar evento dblclick a caja3
caja3.addEventListener('dblclick', () => {
  caja3.style.fontSize = '24px';
});