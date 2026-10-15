alert("Bienvenido al generador de tablas de multiplicar!");
var numerox = prompt("Qué número quieres multiplicar?");
var numeroy = prompt("¿Cuántas veces deseas multiplicarlo?");

for (i = 1; i <= numeroy; i++) {
    var multi = numerox * i;
    
    document.write(numerox+" x "+i+" = "+multi+"<br>")
}