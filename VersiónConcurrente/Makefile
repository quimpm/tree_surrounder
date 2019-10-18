
CFLAGS= -I. -lm -pthread


ex: calcArbolesConcu.c
	gcc calcArbolesConcu.c -o calcArbolesConcu $(CFLAGS)
	./calcArbolesConcu ConjuntoPruebas/$(f) $(t)   
 
conc: calcArbolesConcu.c
	gcc calcArbolesConcu.c -o calcArbolesConcu $(CFLAGS)

d: calcArbolesConcu.c
	gcc calcArbolesConcu.c -o calcArbolesConcu $(CFLAGS)
	./calcArbolesConcu ConjuntoPruebas/Ejemplo1.dat 3  
dc: calcArbolesConcu.c
	clear
	gcc calcArbolesConcu.c -o calcArbolesConcu $(CFLAGS)
	./calcArbolesConcu ConjuntoPruebas/Ejemplo1.dat 3  
