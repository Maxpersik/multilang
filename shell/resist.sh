#!/bin/bash

S=0
for r in $@
do
    S=$(echo $S+1/$r | bc -l)
done
R=$(echo "scale=2;if(1/$S<1) print 0; 1/$S" | bc -l)  
echo "Общее сопротивление равно: $R Ом"
