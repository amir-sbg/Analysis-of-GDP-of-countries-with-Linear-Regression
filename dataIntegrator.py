import pandas as pd
import os

if __name__ == '__main__':

    result_file = "output.xls"
    inputDataFrames = []

    for filename in os.listdir("InputData"):
        if "WEO" not in filename:
            inputDataFrames.append(pd.read_excel("InputData/" + filename))

    outputDataFrame = pd.DataFrame(columns=(inputDataFrames[0]).columns)

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    for i in range(0, 3):
        v = ((inputDataFrames[0].iloc[i:i + 1, :].values).tolist()[0])
        outputDataFrame.loc[i] = v

    x = 0
    for i in range(3, len(inputDataFrames[0])):
        y = 0
        for inputDataFrame in inputDataFrames:
            k = list(inputDataFrame.iloc[i:i + 1, :].keys())
            v = ((inputDataFrame.iloc[i:i + 1, :].values).tolist()[0])
            outputDataFrame.loc[(x * len(inputDataFrames)) + i + y] = v
            print((x * len(inputDataFrames)) + i + y, "    ,    ", v)
            y += 1
        x += 1
    outputDataFrame.to_excel(result_file, index=False)
