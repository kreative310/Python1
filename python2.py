fruits = ["apple", "banana", "cherry"]

print(fruits)

#create a tuple(doesnt change)
words = ("spam", "eggs", "susages")
print(words[1])

#create a tuple with info about a person

person = ('Keti', "18", "software engineer")

name, age, proffesion = person

print(name, "'s", "proffesion is", proffesion, "and she is", age, "years old.")


#creating dictionary

my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",

    #more keys more values pairs

}

contact_info = {
    "Blerta": "7893-993",
    "drini": "2764765489"
}

#create a variable called kreatives phone and use [] we can specify which key we want to access

kreative_phone = contact_info ["Blerta"]

print(kreative_phone)
print(contact_info)

contact_info ["Drini"] = "0294-48575"

print(contact_info)

#we want to add another friend to contact_info

contact_info ["Eros"] = "9843-117348"

print(contact_info)

#delete a contact info

del contact_info ["Blerta"]
print(contact_info)