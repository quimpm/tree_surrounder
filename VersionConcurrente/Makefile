
CFLAGS= -I. -lm -pthread

comp: CalcArbolesConcurrent.c
	gcc CalcArbolesConcurrent.c -o CalcArbolesConcurrent $(CFLAGS)

ex: CalcArbolesConcurrent.c
	gcc CalcArbolesConcurrent.c -o CalcArbolesConcurrent $(CFLAGS)
	./CalcArbolesConcurrent ConjuntoPruebas/$(f) $(t)   
 

d: CalcArbolesConcurrent.c
	gcc CalcArbolesConcurrent.c -o CalcArbolesConcurrent $(CFLAGS)
	./CalcArbolesConcurrent ConjuntoPruebas/Ejemplo1.dat 3  
dc: CalcArbolesConcurrent.c
	clear
	gcc CalcArbolesConcurrent.c -o CalcArbolesConcurrent $(CFLAGS)
	./CalcArbolesConcurrent ConjuntoPruebas/Ejemplo1.dat 3  
