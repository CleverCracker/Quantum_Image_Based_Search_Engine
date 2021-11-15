import numpy as np
from qiskit import Aer, QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.monitor.job_monitor import job_monitor
from Preprocessing import image_normalization
import FRQI as FRQI
"""
# For 4x4
"""

imageDir = "images/4x4/"
imageNames = ["00","01","02","03","10","11","12","13","20","21","22","23","30","31","32","33"]
imageExt = ".jpg"


ref = QuantumRegister(5, 'ref')
anc = QuantumRegister(1, 'anc')
backend = Aer.get_backend('statevector_simulator')
numOfShots = 1024

c = ClassicalRegister(6)
data = []   

for imageName in imageNames:
    pathImage1 = imageDir + imageName + imageExt
    # Normalization of Image
    img = image_normalization(pathImage1, w=4, h=4)

    qc = QuantumCircuit(ref, anc, c)
    #Initilization of Qubit
    qc.h([ref[i] for i in range(1, len(ref))])

    # encode ref image
    for i in range(len(img)):
        if img[i] != 0:
            FRQI.cqry(qc, 2 * img[i], format(i, '04b'), ref[0],
                      anc[0], [ref[j] for j in range(1, len(ref))],4)

    result = execute(qc, backend, shots=numOfShots).result()

    statevector = result.get_statevector()
    data.append(statevector)
    print(imageName)
    
np.savetxt('data_4x4.csv', data, delimiter=',')


"""
# For 32x32
"""

imageDir = "images/"
imageNames = ["Fukuoka", "Nagoya", "Osaka",
              "Sapporo", "Sapporo", "Tokyo", "Black", "White"]
imageExt = ".JPG"


ref = QuantumRegister(11, 'ref')
anc = QuantumRegister(1, 'anc')
backend = Aer.get_backend('statevector_simulator')
numOfShots = 1024

c = ClassicalRegister(12)
data = []

for imageName in imageNames:
    pathImage1 = imageDir + imageName + imageExt
    img = image_normalization(pathImage1, w=4, h=4)

    qc = QuantumCircuit(ref, anc, c)
    qc.h([ref[i] for i in range(1, len(ref))])

    # encode ref image
    for i in range(len(img)):
        if img[i] != 0:
            FRQI.c10ry(qc, 2 * img[i], format(i, '04b'), ref[0],
                      anc[0], [ref[j] for j in range(1, len(ref))])

    result = execute(qc, backend, shots=numOfShots).result()

    statevector = result.get_statevector()
    data.append(statevector)
    print(imageName)

np.savetxt('data_32x32.csv', data, delimiter=',')
