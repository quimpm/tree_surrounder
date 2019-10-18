#Pasar per els arguments el nombre d'exemples que vols que es generin
import sys
import random

def randomTreeNum():
    return random.randint(2,33) #De 2 a 32

def randomTree():
    return str(random.randint(0,10))+" "+str(random.randint(0,10))+" "+str(random.randint(0,30))+" "+str(random.randint(0,30))+"\n"



def main(num_exemples):
    files=[]
    i=0
    while i<num_exemples:
        files.append(open("./exemples/exemple"+str(i)+".dat","w+"))
        n_trees=randomTreeNum()
        files[i].write(str(n_trees)+"\n")
        j=0
        while j<n_trees:
            files[i].write(randomTree())
            j+=1
        files[i].close()    
        i+=1
        


if  __name__=="__main__":
    main(int(sys.argv[1]))
