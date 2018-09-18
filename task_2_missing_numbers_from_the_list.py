#form
def calculate_way(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

#place of adding the generated numbers
my_list= []

for i in calculate_way(2.0, 6.0, 0.5):
    my_list.append(i)

#write numbers
print(my_list)