#!/bin/bash

for i in {1..5}; do
	echo -e "Ejecucion $i thread----------------------------------------------------------------------------------------"
	i=0
	for d in $(ls ConjuntoPruebas/exemples/); do
		echo "EXEMPLE $d"
		echo -e "Ejecucion Concurrente"
		time ./calcArbolesConcu ./ConjuntoPruebas/exemples/$d $i > /dev/null
		echo -e "Ejecucion Seq"
		time ./calcArbolesConcu ./ConjuntoPruebas/exemples/$d 1 > /dev/null
		i=$(($i+1))
	done
done
