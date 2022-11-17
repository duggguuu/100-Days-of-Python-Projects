import pandas

data=pandas.read_csv("squirrel_count.csv")
gray_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
print(gray_squirrels_count)
red_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(red_squirrels_count)
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
print(black_squirrels_count)

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("my_sq_count")