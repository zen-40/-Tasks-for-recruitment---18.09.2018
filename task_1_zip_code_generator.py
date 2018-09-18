import re

def zip_code_return():
    #zip code is the beginning (and conversion into a numerical value)
    initial_zip_code = input("Podaj początkowy kod pocztowy w formie np. '41-500':\n")
    clear_i_zip_code = re.sub('-', '', initial_zip_code) # postal code without "-"
    clear_i_zip_code = int(clear_i_zip_code)

    #zip code is the end (and conversion into a numerical value)
    final_zip_code = input("Podaj końcowy kod pocztowy w formie np. '41-700':\n")
    clear_f_zip_code = re.sub('-', '', final_zip_code) # postal code without "-"
    clear_f_zip_code = int(clear_f_zip_code)

    #zip code generator (and converting the number to a zip code)
    for zip_code in range(clear_i_zip_code, clear_f_zip_code):
        # creates zip codes such as 00-xxx
        if zip_code <= 999:
            print("00", "-", zip_code)
        # creates zip codes such as 0x-xxx
        if zip_code <= 9999 and zip_code > 999:
            change = str(zip_code)
            l = int(len(change) / 3)
            part_a, part_b = change[:l], change[l:]
            print("0" + part_a, "-", part_b)
        # creates all zip such as xx-xxx
        if zip_code >= 9999:
            change1 = str(zip_code)
            y = int(len(change1) / 2)
            part_c, part_d = change1[:y], change1[y:]
            print(part_c, "-", part_d)



zip_code_return()
