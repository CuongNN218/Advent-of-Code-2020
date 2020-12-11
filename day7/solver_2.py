with open('input.txt', 'r') as input:
    lines = input.readlines()
contents = {}
for line in lines:
    line = line[:-1]
    splited_line = line.split('contain')
    main_color = ' '.join(splited_line[0].split(' ')[:2]) 
    elements = {}
    splited_contains = splited_line[1].split(',')
    for contain in splited_contains:
        contain = contain.strip().split(' ')
        if contain[0] == 'no':
            elements = {}
        else:
            value = int(contain[0])
            sub_color = ' '.join(contain[1:3])
            elements[sub_color] = value
    contents[main_color] = elements

color_value = {}
def rev_fn(color, contents, color_value):
    main_color = color
    values = contents[main_color]
    if len(values.keys()) == 0:
        color_value[main_color] = 0
        return 0
    else:
        count = 0
        for sub_color in values.keys():
            if sub_color in color_value.keys():
                count += values[sub_color] * color_value[sub_color] + values[sub_color]
            else:
                count += values[sub_color] * rev_fn(sub_color, contents, color_value) + values[sub_color]
        color_value[main_color] = count
    return count
print('out', rev_fn('shiny gold', contents, color_value))

