# Multiplicador combinacional
Este es un programa de línea de comandos que permite realizar la multiplicación binaria de dos factores de longitud que escoja el usuario. Los factores pueden ser ingresados en formato decimal, hexadecimal o binario. El programagenera un archivo PDF que muestra el proceso de la multiplicación binaria y el resultado final.

## Especificaciones de entrada
- Cantidad de bits de los factores a multiplicar
- Los valores de cada factor (exclusivamente dos valores)
- Los factores se forma decimal, hexadecimal y binario
- La base numérica de los factores se indicará con la letra delante del número. La letra d indica un número decimal, h sería para el hexadecimal y b para los binarios.

        Ejemplo: d25, h2a, b10
- En caso de no indicarse, se tomará el número como decimal.
- El programa debe ser ejecutado desde comando de consola. Las entradas descritas se ingresarán como argumentos.

        Ejemplo: mult.py --bits 6 -a d21 -b h10
- Debe tener una opción para ingresar los datos requeridos como archivo de configuración de texto.

        Ejemplo: mult.py -f archivo.f
Cuyo contenido debe seguir el siguiente formato: `bits 6 a d21 b h10`. En una sola línea como se muestra en el ejemplo.

## Especificaciones de salida

- El programa debe generar un archivo.pdf con la solución del cálculo de la multiplicación binaria.
- El pdf debe ser generado por medio de LaTeX. El documento debe ser estilo Beamer, es decir, con diapositivas.

## Requerimientos

- Python 3.10.10
- LaTeX
 