#!/usr/bin/env bash
# Retos platzi

new_line(){
echo -e '\n'
echo "****************"
echo -e '\n'
}

new_line

echo "Hello World"

new_line

read -p -r "Cual es tu nombre?: " name
read -p -r "Cual es tu apellido: " last_name

echo "Hola, $name $last_name"
