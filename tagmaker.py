# This is to make hashtags for instagram and twitter from a wordlist
# Read in
import random

filename = input("Enter filename > ")

with open(filename) as file_object:
	lines = file_object.readlines()

tags = []

for line in lines:
	tags.append("#"+line.strip())

output = ''

# pick 30 at random since thats limit for insta
if len(lines) > 30:
	new_tags = random.sample(tags, 30)
else:
	new_tags = random.sample(tags, len(lines))
for t in new_tags:
	output += t+" "

print(output)

with open("tags_insta_"+filename, 'a') as file_object:
	file_object.write("==== TAGS START ====\n")
	file_object.write(output)
	file_object.write("\n==== TAGS END ====\n")


