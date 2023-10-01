import pandas
get_info=input()  #input information from terminal

fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()
# write your program code here
#Excel
info_list = fails.loc[fails['Description'] == get_info]
if not info_list.empty :
    AreaXl = info_list.iloc[0, 0]
else:
    AreaXl = 0
#CSV
data = pandas.read_csv("data.csv")
filter_data = data[data["Area"] == AreaXl]
if not filter_data.empty:
    geo_count:int = filter_data["geo_count"].sum()
    print(geo_count)
else:
    print(0)