with open('input.txt', 'r') as input:
    lines = input.readlines()
contents = []
for line in lines:
    contents.append(line[:-1])

unique_colors = []
my_color = 'shiny gold'
colors = [my_color]
while colors:
    for color in range(len(colors)):
        current_color = colors.pop()
        for content in contents:
            splited_content = content.split('contain')
            if current_color in splited_content[1]:
                add_color = " ".join(content.split('contain')[0].split(' ')[:2])
                if add_color in unique_colors:
                    continue
                else:
                    colors.append(add_color)
                    unique_colors.append(add_color)

print(len(unique_colors))