import pandas as pd
import os, numpy,math
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats
if __name__ == '__main__':
    gdpDataFrame=[]
    debtDataFrame=[]

    countriesDict={}
    gdpDataFrame=pd.read_excel("InputData/API_NY.GDP.PCAP.KD.ZG_DS2_en_excel_v2_2253153.xls")
    debtDataFrame=pd.read_excel("InputData/API_GC.DOD.TOTL.GD.ZS_DS2_en_excel_v2_2253033.xls")
    xLable=None
    yLable=None
    for i in range(3, len(gdpDataFrame)):

        gdpVector =  ((gdpDataFrame.iloc[i:i + 1, :].values).tolist()[0])
        debtVector =  ((debtDataFrame.iloc[i:i + 1, :].values).tolist()[0])
        year=((gdpDataFrame.iloc[2:3, :].values).tolist()[0])
        countriesDict[gdpVector[0]]=[gdpVector[4:],debtVector[4:],year[4:]]

    for i in countriesDict.keys():
        name=i


        x =countriesDict[i][1][0:min(len(countriesDict[i][1]),len(countriesDict[i][0]))]
        y =countriesDict[i][0][0:min(len(countriesDict[i][1]),len(countriesDict[i][0]))]
        names =countriesDict[i][2][0:min(len(countriesDict[i][1]),len(countriesDict[i][0]))]
        names=list(map(int, names))


        if not math.isnan(x[0]):
            tmp=0
            for i in range(len(x)):
                if math.isnan(x[i]):
                    tmp=i
                    break
            x=x[0:tmp]
            y=y[0:tmp]
            names=names[0:tmp]

            slope, intercept, r, p, std_err = stats.linregress(x, y)

            def myfunc(x):
                return slope * x + intercept
 
            mymodel = list(map(myfunc, x))

            fig, ax = plt.subplots()


            ax.scatter(x, y)


            for i, txt in enumerate(names):
                ax.annotate(txt, (x[i], y[i]))

            plt.xlabel("Central government debt, total (% of GDP)")
            plt.ylabel("GDP per capita growth (annual %)")
            plt.title(name)
            plt.scatter(x, y)
            plt.plot(x, mymodel)
            plt.show()
