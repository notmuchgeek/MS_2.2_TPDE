import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import pandas as pd

def successImport():
    return print('''import numpy as np\nimport matplotlib.pyplot as plt\nimport scipy.optimize as opt\nimport pandas as pd\nFunctions successfully imported!\n''')

def yld_rawdata(fileName,skiprow=6):
    fileName = str(fileName)
    skiprow = int(skiprow)
    dataExample = pd.read_csv(fileName,skiprows = skiprow)
    return dataExample.values.tolist()

def yld_xy_sliced(rawDataList,sliceStart=None,sliceEnd=None):
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

def yld_curve_fit_Y(para_curve,wv_fit01,inten_fit01,initGuess):
    fit1 = opt.curve_fit(para_curve,wv_fit01,inten_fit01,initGuess)
    a_fitted = fit1[0][0]
    b_fitted = fit1[0][1]
    c_fitted = fit1[0][2]
    print('Wavelength for the maximum point =',-b_fitted,'nm')
    return para_curve(wv_fit01,a_fitted,b_fitted,c_fitted)


def V_water_toluene_ethanol(V_h2o,V_tol,V_eth):
    global ρ_h20,ρ_tol,ρ_eth
    m_h20 = V_h2o*ρ_h20
    m_tol = V_tol*ρ_tol
    m_eth = V_eth*ρ_eth
    mTotal = m_h20+m_tol+m_eth
    
    frac_h20 = m_h20/mTotal
    frac_tol=m_tol/mTotal
    frac_eth=m_eth/mTotal
    
    frac_h20 = "{0:.3g}".format(frac_h20)
    frac_tol="{0:.3g}".format(frac_tol)
    frac_eth="{0:.3g}".format(frac_eth)
    return print(
                'Table format for mass fraction:','|', frac_eth, '|',frac_h20, '|',frac_tol,'|\n',\
                'Table format for component volume:','|', V_h2o, '|',V_tol, '|',V_eth,'|'
                )


successImport()
