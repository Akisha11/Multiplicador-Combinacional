import subprocess
import os
#import shutil

# Crea un archivo con contenido LaTex y en estilo beamer
beamer_code = """\\documentclass{beamer}
\\begin{document}
\\begin{frame}
\\frametitle{Una prueba}
    Este es un ejemplo de un documento al estilo beamer creado por LaTex desde Python.
\\end{frame}
\\end{document}
"""

with open('documento.tex', 'w') as f: #'documento.tex' documento es el nombre del documento y .tex es el formato
    f.write(beamer_code)

#Apartado donde el código solo genera un documento en formato PDF y otro en formato TeX
# Compila el archivo LaTeX para generar el archivo auxiliar
subprocess.call(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'documento.tex', '-output-directory=output'])

# Compila el archivo LaTeX por segunda vez para generar el archivo PDF final
subprocess.call(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'documento.tex', '-output-directory=output'])

# Mueve el archivo PDF final a la carpeta raíz
subprocess.call(['mv', 'output/documento.pdf', '.'])

# Elimina los archivos intermedios generados por LaTeX
subprocess.call(['rm', '-r', 'output'])
for extension in ['aux', 'log', 'out']:
    os.remove(f'documento.{extension}')

# Mueve el archivo PDF a una ubicación específica
#shutil.move('documento.pdf', 'C:\Users\Fiorela\Desktop\documento.pdf') 