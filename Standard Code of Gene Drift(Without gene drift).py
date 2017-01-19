from random import *
def run():
    fa=0.2
    fb=0.2
    fc=0.2
    fd=0.2
    fe=0.2
    i=0
    j=0
    while i<30:
        aa=0
        bb=0
        cc=0
        dd=0
        ee=0
        while j<1000:
            ff=uniform(1, 0)
            if ff<fa:
                aa=aa+1
            if fa<=ff<fa+fb:
                bb=bb+1
            if fa+fb<ff<fa+fb+fc:
                cc=cc+1
            if fa+fb+fc<ff<fa+fb+fc+fd:
                dd=dd+1
            if ff>fa+fb+fc+fd:
                ee=ee+1
            j=j+1
        fa=  float(aa)/1000
        fb = float(bb) / 1000
        fc = float(cc) / 1000
        fd = float(dd )/ 1000
        fe = float(ee)/ 1000

        print "fa", fa,"fb", fb,"fc", fc,"fd", fd,"fe", fe
        i = i + 1
        j=0
        printi
        print "over"
run()