import pandas as pd

df = pd.read_csv("Day1/day1_input.csv", low_memory=False)

def func(df):
    counter = 0

    for i in range(len(df)):
        try:
            a = int(df.iloc[i])
            b = int(df.iloc[i+1])
        except:
            print("Out of bounds")
        if a<b:
            counter+=1

    return counter

print(func(df))