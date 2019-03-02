# -*- coding: utf-8 -*-

import math
import numpy as np
import cmath as cm
import matplotlib.pyplot as plt

def stft(target_in, N,l):
    target_out = []
    frame_num = 4 #任意の整数
    S = int(N / frame_num)
    
    ffted = []
    f_out = []
    #print(range(int((l-N)/S))) #Sが繰り返せる回数
    for s in range(int((l-N)/S)+1): #Sが繰り返せる回数
        hamminged = []
        #print(hamminged)
        #print(range(int(s*S), int(N+s*S), 1))
        for n in range(int(s*S), int(N+s*S), 1):
            #print("a")
            hamminged.append(target_in[n] * hamming_w(n, N))
        plt.plot(hamminged)
        plt.show()
        print(hamminged)
        dfted = dft(hamminged)
        f_out.append(dfted)
        #print(f_out)
    return f_out

def hamming_w(t,N):
    return 0.54-0.46*np.cos(2*np.pi*t/N)

def dft(target):
    dfted = []
    N = len(target)
    for k in range(N):
        multi_out = 0
        w = cm.exp(-1j * 2 * cm.pi * k / float(N))
        for n in range(N):
            multi_out = multi_out + target[n] * (w ** n)
        dfted.append(abs(multi_out))
    return dfted

if __name__ == "__main__":
    N = 512 #1024,2048
    n = np.arange(1024) #1024の波形
    freq = 3
    target_wave = np.sin(freq * 2 * np.pi * (n / N))
    plt.plot(target_wave)
    plt.show()
    spectrogram = stft(target_wave, N,len(n))
    print(len(spectrogram))
    for i in range(4):
        plt.plot(spectrogram[i])
        plt.show()
    plt.plot(spectrogram)
    plt.show()
