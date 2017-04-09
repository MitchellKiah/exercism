#!/bin/bash
name=$1
if [ -z $name ]
then
  name="World"
fi
echo "Hello, ${name}!"
