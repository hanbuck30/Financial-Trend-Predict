import numpy as np

def FNC_Func_Extrema(x):
    xmax = []
    imax = []
    xmin = []
    imin = []

    # Vector input?
    Nt = np.size(x)
    if Nt != np.shape(x)[0]:
        raise ValueError('Entry must be a vector.')

    # NaN's:
    inan = np.argwhere(np.isnan(x))
    indx = np.array(range(Nt))
    if inan.size > 0:
        indx = np.delete(indx, inan)
        x = np.delete(x, inan)
        Nt = np.size(x)

    # Difference between subsequent elements:
    dx = np.diff(x)

    # Is an horizontal line?
    if not np.any(dx):
        return xmax, imax, xmin, imin

    # Flat peaks? Put the middle element:
    a = np.argwhere(dx!=0).flatten() # Indexes where x changes
    lm = np.argwhere(np.diff(a)!=1).flatten() + 1 # Indexes where a do not changes
    d = a[lm] - a[lm-1] # Number of elements in the flat peak
    a[lm] = a[lm] - d//2 # Save middle elements
    a = np.append(a, Nt-1) # Python's indexing starts at 0

    # Peaks?
    xa  = x[a] # Serie without flat peaks
    b = (np.diff(xa) > 0) # 1  =>  positive slopes (minima begin)
    # 0  =>  negative slopes (maxima begin)
    xb  = np.diff(b.astype(int)) # -1 =>  maxima indexes (but one)
    # +1 =>  minima indexes (but one)
    imax = (np.argwhere(xb == -1) + 1).flatten() # maxima indexes
    imin = (np.argwhere(xb == 1) + 1).flatten() # minima indexes
    imax = a[imax]
    imin = a[imin]

    nmaxi = np.size(imax)
    nmini = np.size(imin)

    # Maximum or minumim on a flat peak at the ends?
    if (nmaxi==0) and (nmini==0):
        if x[0] > x[Nt-1]:
            xmax = [x[0]]
            imax = [indx[0]]
            xmin = [x[Nt-1]]
            imin = [indx[Nt-1]]
        elif x[0] < x[Nt-1]:
            xmax = [x[Nt-1]]
            imax = [indx[Nt-1]]
            xmin = [x[0]]
            imin = [indx[0]]
        return xmax, imax, xmin, imin

    # Maximum or minumim at the ends?
    if (nmaxi==0):
        imax = [0, Nt-1]
    elif (nmini==0):
        imin = [0, Nt-1]
    else:
        if imax[0] < imin[0]:
            imin = np.concatenate(([0], imin))
        else:
            imax = np.concatenate(([0], imax))

        if imax[-1] > imin[-1]:
            imin = np.concatenate((imin, [Nt-1]))
        else:
            imax = np.concatenate((imax, [Nt-1]))

    xmax = x[imax].tolist()
    xmin = x[imin].tolist()

    # NaN's:
    if inan.size > 0:
        imax = indx[imax].tolist()
        imin = indx[imin].tolist()

    # Descending order:
    imax = [x for _,x in sorted(zip(xmax,imax), reverse=True)]
    xmax.sort(reverse=True)
    imin = [x for _,x in sorted(zip(xmin,imin))]
    xmin.sort()

    return xmax, imax, xmin, imin
