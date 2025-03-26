import pandas as pd
import re

def clean_table(df: str):
    header, data = df.split("\n")[0], df.split("\n")[1:]

    columns = header.split("\t")
    arr = []
    for datum in data:
        entries = datum.split("\t")

        team_loc = -1
        for i in range(len(entries)):
            if len(entries[i]) == 3 and bool(re.match(r'[A-Z]+$', entries[i])):
                team_loc = i
                break
        
        name = " ".join(entries[:team_loc])
        arr = arr + [[name] + entries[team_loc:]]

    return pd.DataFrame(arr, columns=columns)
    

if __name__ == "__main__":
    with open('defensive-impact.txt', 'r') as f:
        s = f.read()
        df = clean_table(s)

        df.to_csv("data/defensive-impact.csv")
    
    with open('defensive-rebounding.txt', 'r') as f:
        s = f.read()
        df = clean_table(s)

        df.to_csv("data/defensive-rebounding.csv")