def print_count(number):
    if(number%4) == 0:
        if(number%100) == 0:
            if (number%400) == 0:
                print("That year is a leap year")
                return("That year is a leap year")
