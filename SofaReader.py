import h5py
import numpy as np
import matplotlib.pyplot as plt

#filename = 'C:/Users/Paolo/Dropbox/UniSheffield/SofaExtraction/LISTEN_1002_IRC_1002_C_HRIR.sofa'
filename = 'LISTEN_1002_IRC_1002_C_HRIR.sofa'
f = h5py.File(filename, 'r')

print("Keys: %s" % f.keys())

N = 100;
for i in range(0,N):
    a_group_key = list(f.keys())[i]
    print (a_group_key)

    if a_group_key == 'ListenerUp':
        data = list(f[a_group_key])
        print(data)

    if a_group_key == 'ListenerPosition':
        data = list(f[a_group_key])
        print(data)

    if a_group_key == 'EmitterPosition':
        data = list(f[a_group_key])
        print(data)

    if a_group_key == 'SourcePosition':
        data = list(f[a_group_key])
        #print(data)
        position = np.asarray(data);
        print(position.shape)

    if a_group_key == 'Data.IR':
        data = list(f[a_group_key])
        #print(data)
        IRs = np.asarray(data);
        print(IRs.shape)
        plt.plot(IRs[0][0])
        plt.show()


    #print(data)
