import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    print(ciscocsv.head())

    print(ciscojson.head())

    ciscodf = pd.concat([ciscocsv, ciscojson])

    print()

    ciscodf.to_excel("combined_ciscodata.xls")

    x = ciscodf.to_dict()
    print(x)

    # print(ciscodf)

main()