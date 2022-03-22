import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import pandas as pd

def successImport():
    return print('''import numpy as np\nimport matplotlib.pyplot as plt\nimport scipy.optimize as opt\nimport pandas as pd\nFunctions successfully imported!\n''')


def yld_rawdata(fileName:str,skiprow:int=6)->list:
    fileName = str(fileName)
    skiprow = int(skiprow)
    dataExample = pd.read_csv(fileName,skiprows = skiprow)
    return dataExample.values.tolist()

def yld_xy_sliced(rawDataList:list,sliceStart=None,sliceEnd=None):
    wvlExp = []
    intenExp = []
    for i in rawDataList:
        wvlExp.append(i[0])
        intenExp.append(i[1])
    if sliceStart:
        sliceStart = wvlExp.index(sliceStart)
    if sliceEnd:
        sliceEnd = wvlExp.index(sliceEnd)
    return wvlExp[sliceStart:sliceEnd],intenExp[sliceStart:sliceEnd]

def para_curve(x,a,b,c):
    return a*((x + b)**2) + c

def yld_curve_fit_Y(para_curve,wv_fit01,inten_fit01,initGuess:list):
    fit1 = opt.curve_fit(para_curve,wv_fit01,inten_fit01,p0=initGuess)
    a_fitted = fit1[0][0]
    b_fitted = fit1[0][1]
    c_fitted = fit1[0][2]
    print('Wavelength for the maximum point =',-b_fitted,'nm')
    return para_curve(wv_fit01,a_fitted,b_fitted,c_fitted)


successImport()
