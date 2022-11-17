import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict={}
for (index,row) in data.iterrows():
    nato_dict={row.letter:row.code for (index,row) in data.iterrows()}

def gen():
    word=input("Enter a word.").upper()
    try:
        nato_words=[nato_dict[letter] for letter in word]
    except KeyError:
        print ("Sorry, wrong input.")
        gen()
    else:
        print(nato_words)

gen()
