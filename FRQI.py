import numpy as np
import math


def marycx(circ, t, c0, c1):
    circ.ry(np.pi/4, t)
    circ.cx(c0, t)
    circ.ry(np.pi/4, t)
    circ.cx(c1, t)
    circ.ry(-np.pi/4, t)
    circ.cx(c0, t)
    circ.ry(-np.pi/4, t)


def mary(circ, angle, t, c0, c1, c2):
    circ.h(t)
    circ.t(t)
    circ.cx(c0, t)
    circ.tdg(t)
    circ.h(t)
    circ.cx(c1, t)
    circ.rz(angle/4, t)
    circ.cx(c2, t)
    circ.rz(-angle/4, t)
    circ.cx(c1, t)
    circ.rz(angle/4, t)
    circ.cx(c2, t)
    circ.rz(-angle/4, t)
    circ.h(t)
    circ.t(t)
    circ.cx(c0, t)
    circ.tdg(t)
    circ.h(t)

# FRQI To Convert Image for 10 Qubits in Quantum Image Representation
def c10ry(circ, angle, bin, target, anc, controls):

    clist = []

    for i in bin:
        clist.append(int(i))

    for i in range(len(clist)):
        if clist[i] == 0:
            circ.x(controls[-i-1])

    marycx(circ, anc, controls[0], controls[1])
    circ.x(controls[0])
    circ.x(controls[1])
    marycx(circ, controls[1], controls[2], controls[3])
    circ.x(controls[2])
    circ.x(controls[3])
    marycx(circ, controls[3], controls[4], controls[5])
    circ.x(controls[4])
    circ.x(controls[5])

    marycx(circ, controls[5], controls[8], controls[9])
    marycx(circ, controls[4], controls[6], controls[7])
    marycx(circ, controls[2], controls[4], controls[5])
    marycx(circ, controls[0], controls[2], controls[3])

    mary(circ, angle, target, anc, controls[0], controls[1])

    marycx(circ, controls[0], controls[2], controls[3])
    marycx(circ, controls[2], controls[4], controls[5])
    marycx(circ, controls[4], controls[6], controls[7])
    marycx(circ, controls[5], controls[8], controls[9])

    circ.x(controls[5])
    circ.x(controls[4])
    marycx(circ, controls[3], controls[4], controls[5])
    circ.x(controls[3])
    circ.x(controls[2])
    marycx(circ, controls[1], controls[2], controls[3])
    circ.x(controls[1])
    circ.x(controls[0])
    marycx(circ, anc, controls[0], controls[1])

    for i in range(len(clist)):
        if clist[i] == 0:
            circ.x(controls[-i-1])

# FRQI To Convert Image in Quantum Image Representation
def cqry(circ, angle, bin, target, anc, controls,q):
    clist = []

    for i in bin:
        clist.append(int(i))

    for i in range(len(clist)):
        if clist[i] == 0:
            circ.x(controls[-i-1])
    i = 0
    while(i<=q/2):
        if(i==0):
            marycx(circ, anc, controls[0], controls[1])
            circ.x(controls[0])
            circ.x(controls[1])
            i = 1
        else:
            marycx(circ, controls[i], controls[i+1], controls[i+2])
            circ.x(controls[i+1])
            circ.x(controls[i+2])
            i = i+2

    j = 2 * math.floor(q/2) - 1
    while(j-3>=0):
        marycx(circ, controls[j-3], controls[j-1], controls[j])
        j-=2

    mary(circ, angle, target, anc, controls[0], controls[1])

    j=0
    while (j+3< q):
        marycx(circ, controls[j], controls[j+2], controls[j+3])
        j+=2
    i-=2
    while (i-2 >=0):
        if(i-2 !=0):
            circ.x(controls[i])
            circ.x(controls[i-1])
            marycx(circ, controls[i-2], controls[i-1], controls[i])
        else:
            circ.x(controls[1])
            circ.x(controls[0])
            marycx(circ, anc, controls[0], controls[1])
        i -= 2

    for i in range(len(clist)):
        if clist[i] == 0:
            circ.x(controls[-i-1])


# Convert the Quantum Image into Clasical Image only for 32 qubits
def generateImage(result, img, qc, numOfShots):
    genimg = np.array([])

    # decode
    for i in range(len(img)):
        try:
            genimg = np.append(
                genimg, [np.sqrt(result.get_counts(qc)[format(i, '010b')+'01']/numOfShots)])
        except KeyError:
            genimg = np.append(genimg, [0.0])

    # inverse nomalization
    genimg *= 32.0 * 255.0
    img = np.sin(img)
    img *= 255.0

    # convert type
    genimg = genimg.astype('int')

    # back to 2-dimentional data
    genimg = genimg.reshape((32, 32))
    return genimg
