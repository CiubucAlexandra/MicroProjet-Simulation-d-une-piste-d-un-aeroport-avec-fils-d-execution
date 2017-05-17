""" 
Projet_Piste_aeroport

Ciubuc Alexandra-Cristina
Simuleac Ioana-Veronica
Stefan Cipriana-Elena
"""


import sys, os, threading
import multiprocessing
import random
from multiprocessing import Queue
q  = list()
qAttente = list()
i = 0

class Flights:
    fName = None
    fTemps = None
    
    def __init__(self, n,t):
        self.fName = n
        self.fTemps = t
     
    def getName(self):
        return self.fName

    def getTemps(self):
        return self.fTemps


class Runway(threading.Thread):
    name = None;
    
    def __init__(self,n):
        threading.Thread.__init__(self)
        self.name = n;
        print n + " este pregatita."
 
    def add(self,f):
        q.append(f);
        print "Zborul " + f.fName + " este pregatit."

    def getRunway(self):
        return self.name;

    def run(self):
        try: 
            while len(q) != 0:
                f = q.pop()
                temps = f.getTemps()
                #print temps
                #pour a ateriza il faut justement 5 minutes
                if(temps > 5):
                    qAttente.append(f)
                    #print f.fName
                else:
                    print self.getRunway() + ": " + f.getName() + " a aterizat."
    
            while len(qAttente) != 0:
                t = qAttente.pop()
                print self.getRunway() + ": " + t.getName() + " a parasit pista."
                
        finally:
            pass


def main():
    print "Avioanele care aterizeaza au o prioritate mai mare fata de cele care parasesc aeroportul"
    pista = Runway("Pista BV-128")
    pista.start()
    j = 0
#deci la un moment dat apare un vol urgent
    for j in range(10):
        if j == 5 :
            print """Flight YR-CA589:
                    MAYDAY MAYDAY MAYDAY. Avem o problema!
                    Cerem permisiunea de a ateriza!"""
            zbor = Flights("YR-CA589", 4)
            pista.add(zbor)
            print "Zborul "+ zbor.getName() + " are timpul " + str(zbor.getTemps()) + " minute"
        else:
            nume = "Z" + str(j)    
            zbor = Flights(nume, random.randint(1,10))
            pista.add(zbor)
            print "Zborul "+ nume + " are timpul " + str(zbor.getTemps()) + " minute"

        
        pista.join(10)
        pista.run()
        print
        j = j+1
        

main()
