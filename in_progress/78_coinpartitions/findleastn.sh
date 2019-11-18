#!/bin/bash

poss=1
n=61

while [ "${poss: -6}" != "000000" ]
do
   n=$((n+1))
   echo $n
   poss=$(python coinpartitions.py $n)
   if [ "${n: -1}" == "0" ];
   then
      echo $n
   fi
done

echo answer: $n

exit 0
