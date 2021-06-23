import pandas as pd
import os,math
import numpy as np
import statsmodels.api as sm
from numpy import NaN

if __name__ == '__main__':

    result_file = "output.xls"
    inputDataFrames = []
    numberOfInputFiles = 15
    for filename in os.listdir("InputData"):

            inputDataFrames.append(pd.read_excel("InputData/" + filename))

    outputDataFrame = pd.DataFrame(columns=(inputDataFrames[0]).columns)

    pd.set_option("display.max_rows", None, "display.max_columns", None)

    for i in range(0, 3):
        vector = ((inputDataFrames[0].iloc[i:i + 1, :].values).tolist()[0])
        outputDataFrame.loc[i] = vector

    x = 0
    decomposedInputData = []
    xNames=[]
    for i in range(3, len(inputDataFrames[0])):
        y = 0
        for inputDataFrame in inputDataFrames:
            xNames.append((inputDataFrame.iloc[7:8,2:3 ].values).tolist()[0])
            k = list(inputDataFrame.iloc[i:i + 1, :].keys())
            v = ((inputDataFrame.iloc[i:i + 1, :].values).tolist()[0])
            outputDataFrame.loc[(x * len(inputDataFrames)) + i + y] = v
            decomposedInputData.append(v)

            y += 1
        x += 1
    try:
        outputDataFrame.to_excel(result_file, index=False)
    except  FutureWarning:
        print("FutureWarning!")

    tmp = []
    countriesInputDict = {}
    countriesOutputDict = {}
    countriesInputDict[decomposedInputData[0][1]] = []
    for i in range(len(decomposedInputData)):
        # decomposedInputData[i]=decomposedInputData[i][4:]
        if "GDP per capita growth (annual %)" not in decomposedInputData[i][2]:
            countriesInputDict[decomposedInputData[i][1]].append(decomposedInputData[i][4:])
        else:
            countriesOutputDict[decomposedInputData[i][1]] = decomposedInputData[i][4:]



        if (i + 1) % numberOfInputFiles == 0 and i != len(decomposedInputData) - 1:
            countriesInputDict[decomposedInputData[i + 1][1]] = []


    countriesInputDictPlus = {}
    for i in countriesInputDict.keys():
        tmp1=[]
        tempo=None
        for t in countriesInputDict.keys():
            tempo=t
            break
        # print("---")


        for j in range (0,len(countriesInputDict[tempo][0])):
            tmp2=[]
            for k in range(0,len(list(countriesInputDict[i]))):
                # print(i,"   -   ",k,"   -   ",j)
                tmp2.append(countriesInputDict[i][k][j])
            tmp1.append(tmp2)
        countriesInputDictPlus[i]=tmp1

    for i in countriesOutputDict.keys():

        for j in countriesInputDictPlus[i]:
          
            for x in range(len(j)):
                if math.isnan(j[x]):
                    countriesInputDictPlus[i][j][x]=NaN



    for i in range(len(xNames)):
        xNames[i]=xNames[i][0]

    xNames.remove('GDP per capita growth (annual %)')


    for i in range(len(xNames)):
        while len(xNames[i])<=70:
            xNames[i]=xNames[i]+" "
    xNames=set(xNames)


    for i in countriesOutputDict.keys():

        x=countriesInputDictPlus[i]
        y=countriesOutputDict[i]
        x, y = np.array(x), np.array(y)
        x = sm.add_constant(x)
        model = sm.OLS(y, x,missing="drop")
        results = model.fit()
        print(results.summary(xname=xNames))




