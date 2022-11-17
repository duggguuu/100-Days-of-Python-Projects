from re import T
import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print (data["temp"])

# data_dict=data.to_dict()
# print(data_dict)

# temp_list=data["temp"].to_list()
# print(temp_list)
# total=0
# for t in temp_list:
#     total+=t
# average=total/(len(temp_list))
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())

# print(data["temp"].max())

# print(data[data.day=="Monday"])

# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# print(monday.condition)

# monday=data[data.day=="Monday"]
# monday_temp=int(monday.temp)
# monday_temp = monday_temp * (9/5) + 32
# print (monday_temp)

data_dict = {
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}

data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")