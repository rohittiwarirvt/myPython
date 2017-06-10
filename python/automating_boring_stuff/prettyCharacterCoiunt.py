import pprint

characters = "This is Rohit Tiwari From Pune."
count ={}
for character in characters:
  count.setdefault(character,0)
  count[character] = count[character] +1

print(pprint.pformat(count))
