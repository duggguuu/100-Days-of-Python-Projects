numbers=[1,2,3]
new_numbers=[n+1 for n in numbers]
print(new_numbers)

name="Yash"
new_name=[letter for letter in name]
print(new_name)

range_list=[n*2 for n in range(1,5)]
print(range_list)

names=["Yash","Nakul","Mudita","Krish"]
long_names=[name.upper() for name in names if len(name)>4]
print(long_names)

numbers=[1,1,2,3,5,8,13,21,34,55]
squared_numbers=[n*n for n in numbers]
print(squared_numbers)

numbers=[1,1,2,3,5,8,13,21,34,55]
even_numbers=[n for n in numbers if n%2==0]
print(even_numbers)

with open ('.\\file_1.txt','r') as a:
    list1=a.readlines()
    print(list1)
with open ('.\\file_2.txt','r') as a:
    list2=a.readlines()
    print(list2)

common_numbers=[int(n) for n in list1 if n in list2]
print(common_numbers)

import random
names=["Yash","Nakul","Mudita","Krish"]
scores={student:random.randint(1,100) for student in names}
print(scores)
passed={student:score for(student,score) in scores.items() if score>=60}
print(passed)

sentence="What is the Airspeed Velocity of an Unladen Swallow?"
words=sentence.split()
result={word:len(word) for word in words}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f={day:c*9/5+32 for(day,c) in weather_c.items()}
print(weather_f)

too_hot={day:f for(day,f) in weather_f.items() if f>=65}
print(too_hot)

