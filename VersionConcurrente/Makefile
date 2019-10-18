
CFLAGS= -I. -lm -pthread


ex: CalcArbolesConcurrent.c
	gcc CalcArbolesConcurrent.c -o CalcArbolesConcurrent $(CFLAGS)
	./CalcArbolesConcurrent ConjuntoPruebas/$(f) $(t)   
 
conc: CalcArbolesConcurrent.c
	gcc CalcArbolesConcurrent.c -o CalcArbolesConcurrent $(CFLAGS)

d: CalcArbolesConcurrent.c
	gcc CalcArbolesConcurrent.c -o CalcArbolesConcurrent $(CFLAGS)
	./CalcArbolesConcurrent ConjuntoPruebas/Ejemplo1.dat 3  
dc: CalcArbolesConcurrent.c
	clear
	gcc CalcArbolesConcurrent.c -o CalcArbolesConcurrent $(CFLAGS)
	./CalcArbolesConcurrent ConjuntoPruebas/Ejemplo1.dat 3  
