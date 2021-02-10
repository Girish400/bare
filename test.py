print("Hello World")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
     print(x, y) 
     for x in adj:
        for y in fruits:
            print(x, y)
