# This is to make comma seperate tags for wordpress

filename = input("File name to use: ")

with open(filename) as file_object:
	lines = file_object.readlines()

tags = []

for line in lines:
	tags.append(line.strip())

output = ''


for t in tags:
	output += t+","

print(output)

with open("tags_wp_"+filename, 'a') as file_object:
	file_object.write("==== TAGS START ====\n")
	file_object.write(output)
	file_object.write("\n==== TAGS END ====\n")


