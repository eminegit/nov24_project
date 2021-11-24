# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# def compute_area():
#     radius = 20.0
#     area = radius*radius*3.14159
#     print("The area of the circle is {} is {} area.".format(radius, area))


def convert_temp(f):
    celcius = (f-32)*(5.0/9.0)
    return float(celcius)


def sales_tax(input):
    sales_tax = (8.875/100) * (input)
    return sales_tax



if __name__ == '__main__':
    # print_hi('PyCharm')
    # compute_area()
    # my_value=input("enter your age:  ")
    # print("my age is {}.".format(my_value))

    result = convert_temp(90)
#    print(result)

    print(round(sales_tax(100),2))
    print(round(5.51423, 2))








