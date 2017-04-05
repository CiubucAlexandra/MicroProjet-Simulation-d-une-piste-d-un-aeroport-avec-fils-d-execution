""" Projet_Piste_aeroport"""
import sys, os, threading
import multiprocessing
from multiprocessing import Queue
q  = Queue ()
i = 0

class Flights:
    fName = None
     
    def __init__(self, n):
        self.fName = n
     
    def getName(self):
        return self.fName
     
    def compareTo(f):
        return this.getName().compareTo(f.getName())

class Runway(threading.Thread):
    name = None;
    verrou = threading.Lock()
    
    def __init__(self,n):
        threading.Thread.__init__(self)
        self.name = n;
        print n + " este pregatita."
 
    def add(self,f):
        q.put(f);
        print "Zborul " + f.fName + " este pregatit sa aterizeze."

    def getRunway(self):
        return self.name;

    def run(self):
        self.verrou.acquire()
        try: 
            while q.qsize() != 0:
                if (q.qsize() > 0):
                    f = q.get();
                    print self.getRunway() + ": " + f.getName()+ " este pe punctul de a ateriza."

                    try:
                        Thread.currentThread();
                        Thread.sleep(1000);
                    except Exception as e:
                        print
            
                    print self.getRunway() + ": " + f.getName() + " a aterrizat."
        finally:
            self.verrou.release()


tThread = []
zbor1 = Flights("Z1")
zbor2 = Flights("Z2")

pista1 = Runway("Pista")
pista1.add(zbor1)
pista1.add(zbor2)

pista1.run()

