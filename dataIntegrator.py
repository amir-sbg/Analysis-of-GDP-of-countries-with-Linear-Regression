import pandas as pd
import os, numpy

if __name__ == '__main__':

    result_file = "output.xls"
    inputDataFrames = []
    numberOfInputFiles = 15
    for filename in os.listdir("InputData"):
        if "WEO" not in filename:
            inputDataFrames.append(pd.read_excel("InputData/" + filename))

    outputDataFrame = pd.DataFrame(columns=(inputDataFrames[0]).columns)

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    for i in range(0, 3):
        vector = ((inputDataFrames[0].iloc[i:i + 1, :].values).tolist()[0])
        outputDataFrame.loc[i] = vector

    x = 0
    decomposedInputData = []
    for i in range(3, len(inputDataFrames[0])):
        y = 0
        for inputDataFrame in inputDataFrames:
            k = list(inputDataFrame.iloc[i:i + 1, :].keys())
            v = ((inputDataFrame.iloc[i:i + 1, :].values).tolist()[0])
            outputDataFrame.loc[(x * len(inputDataFrames)) + i + y] = v
            # print((x * len(inputDataFrames)) + i + y, "    ,    ", v)
            decomposedInputData.append(v)

            y += 1
        x += 1
    try:
        outputDataFrame.to_excel(result_file, index=False)
        print("hello")
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


        # print(i, "    :    ", (decomposedInputData[i]))#,"  ->  ",(decomposedInputData[i][4:]))

        if (i + 1) % numberOfInputFiles == 0 and i != len(decomposedInputData) - 1:
            countriesInputDict[decomposedInputData[i + 1][1]] = []

    # print(decomposedInputData)
    # decomposedInputData=numpy.array((decomposedInputData[i][4:]))
    # print(len(countriesInputDict.keys()))
    for i in countriesInputDict.keys():
        print(i)  # ,"    -   ",countriesDict[i])
        countriesOutputDict[i]
        for j in countriesInputDict[i]:
            print("\t",j)

    for i in countriesOutputDict.keys():
        print(i," : ",countriesOutputDict[i])
