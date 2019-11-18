#!/bin/bash

for n in {77..90}
do
   echo $n
   python coinpartitions.py $n
done

exit 0
