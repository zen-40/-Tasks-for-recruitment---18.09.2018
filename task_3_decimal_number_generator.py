missing_elements_list = [] #lost values ​​added here

start_num = int(input("Podaj liczbę początkową:\n"))

end_num = int(input("Podaj liczbę kńcową:\n"))
end_num = end_num+1 #needed to get the result from the example on the website

user_list = [int(x) for x in input("Podaj watości w liście w formacie 1 3 5 itd.:\n").split()]
# the ability to add 're.sub' to added values such as 1, 3, 5 (with a comma between)

# checks the values
for i in range(start_num,end_num):
    if i not in user_list:
        missing_elements_list.append(i)

# returns good values
print("Brakujące elementy w Twojej liscie to:")
print(missing_elements_list)
