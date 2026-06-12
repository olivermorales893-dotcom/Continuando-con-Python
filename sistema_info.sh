#!/bin/bash

echo "Usuario: $(whoami)"
echo "Fecha y hora: $(date)"
echo "Directorio actual: $(pwd)"
echo "Espacio en disco:"
df -h

echo "Contando del 1 al 5:"
for i in 1 2 3 4 5; do
    echo "Número: $i"
done
