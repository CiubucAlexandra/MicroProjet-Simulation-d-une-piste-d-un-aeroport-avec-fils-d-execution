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
q  = Queue ()
qAttente = Queue()
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
    verrou = threading.Lock()
    
    def __init__(self,n):
        threading.Thread.__init__(self)
        self.name = n;
        print n + " este pregatita."
 
    def add(self,f):
        q.put(f);
        print "Zborul " + f.fName + " este pregatit."

    def getRunway(self):
        return self.name;

    def run(self):
        self.verrou.acquire()
        try: 
            while q.qsize() != 0:
                if (q.qsize() > 0):
                    f = q.get()
                    temps = f.getTemps()
                    #pour a ateriza il faut justement 5 minutes
                    if(temps > 5):
                        qAttente.put(f)
                        #print temps
                        try:
                            Thread.currentThread()
                            Thread.sleep(100);
                            print "food"
                        except: 
                            pass
                    elif temps < 5:
                        #print temps
                        print self.getRunway() + ": " + f.getName() + " a aterizat."

            while qAttente.qsize() != 0:
                t = qAttente.get()
                print self.getRunway() + ": " + t.getName() + " a parasit pista."

        finally:
            self.verrou.release()


def main():
    #tThread = []
    print "Avioanele care aterizeaza au o prioritate mai mare fata de cele care parasesc aeroportul"
    zbor1 = Flights("z1",round(random.random() * 10))
    zbor2 = Flights("z2",round(random.random() * 10))
    zbor3 = Flights("z3",round(random.random() * 10))
    zbor4 = Flights("z4",round(random.random() * 10))
    zbor5 = Flights("z5",round(random.random() * 10))
    zbor6 = Flights("z6",round(random.random() * 10))
    zbor7 = Flights("z7",round(random.random() * 10))
    
    pista1 = Runway("Pista BV-128")
    pista1.add(zbor1)
    pista1.add(zbor2)
    pista1.add(zbor3)
    pista1.add(zbor4)
    pista1.add(zbor5)
    pista1.add(zbor6)
    pista1.add(zbor7)
    
    pista1.run()

main()


