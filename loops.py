for a in range (2, 11, 2):
    print(a)


study_material = [["pencil", 'pen'], ['long size note']]

for day in study_material:
    print('day')
    for item in day:
        print(item)

for i, material in enumerate(study_material):
    print(i+1, material)



count = 1
while count<6:
    print('Day ')
    count += 1

print('end')
