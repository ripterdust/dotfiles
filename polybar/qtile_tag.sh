#!/bin/bash

# Obtener el estado de los tags de Qtile
tags=$(qtile-cmd tag_list)

# Formatear la salida para mostrar los tags activos
output=""
for tag in $tags; do
    if qtile-cmd tag_status $tag | grep -q '1'; then
        output="$output %{F#ffffff}%{B#0088ff}$tag%{F-}%{B-} "
    else
        output="$output $tag "
    fi
done

echo "$output"