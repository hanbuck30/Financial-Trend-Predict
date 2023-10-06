import numpy as np
from scipy.signal import argrelextrema

def FNC_Func_PST(T, P, c):
    c = np.array(c, dtype=float)
    n = len(c)

    c_min = argrelextrema(c, np.less)[0]
    c_max = argrelextrema(c, np.greater)[0]

    cp1 = np.concatenate((c_max, c_min))
    cp2 = np.concatenate((c[c_max], c[c_min]))
    cp = np.column_stack((cp1[np.argsort(cp1)], cp2[np.argsort(cp1)]))

    if len(cp) == 0:
        return [], 0

    index = 0
    sp = np.zeros((len(cp), 2))
    sp[index] = cp[index]

    i = 1
    while i < len(cp) - 1:
        if (cp[i+1,0] - cp[i,0] < T) and (abs(cp[i+1,1] - cp[i,1]) / ((cp[i,1] + cp[i+1,1]) / 2) < P):
            i += 2
        else:
            index += 1
            sp[index] = cp[i]
            i += 1

    sp = sp[:index+1]

    if len(sp) == 1:
        out_arg1 = np.zeros(n)
        out_arg2 = 0
    else:
        temp = sp[:,1]
        temp_min = argrelextrema(temp, np.less)[0]
        temp_max = argrelextrema(temp, np.greater)[0]

        t1 = np.concatenate((temp_max, temp_min))
        t2 = np.concatenate((temp[temp_max], temp[temp_min]))
        rp_t = np.column_stack((sp[t1[np.argsort(t1)],0], t2[np.argsort(t1)]))

        if len(rp_t) == 0:
            return [], 0

        rp = np.zeros_like(rp_t)
        rp[0,0] = rp_t[0,0]
        rp[1,0] = rp_t[1,0]
        if rp_t[0,1] < rp_t[1,1]:
            rp[0,1] = -1
            rp[1,1] = 1
        else:
            rp[0,1] = 1
            rp[1,1] = -1

        for i in range(2, len(rp_t)):
            rp[i,0] = rp_t[i,0]
            if rp_t[i-1,1] < rp_t[i,1]:
                rp[i,1] = 1
            else:
                rp[i,1] = -1

        out_arg1 = np.zeros(n)
        for i in range(len(rp)-1):
            a = np.polyfit(rp[i:i+2,0], rp[i:i+2,1], 1)
            
            for j in range(int(rp[i,0]), int(rp[i+1,0])):
                out_arg1[j] = j*a[0] + a[1]

        for i in range(int(rp[-1,0]), n):
            out_arg1[i] = 0

        out_arg1[rp[:,0].astype(int)] = rp[:,1]

        out_arg2 = rp[-1,0]

    return out_arg1, out_arg2
