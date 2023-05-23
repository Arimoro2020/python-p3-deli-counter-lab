


def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        for_print = "The line is currently:"
        for name in katz_deli:
            new_index = (katz_deli.index(name)) + 1
            new_index = str(new_index)
            f_string = f" {new_index}. {name}"
            for_print += f_string
        print(for_print)

def take_a_number(katz_deli, new_name):
    katz_deli.append(new_name)
    count = len(katz_deli)
    print(f"Welcome, {new_name}. You are number {count} in line.")

def now_serving(katz_deli):
    try:
        name = katz_deli.pop(0)
        print(f"Currently serving {name}.")
    except IndexError:
        print("There is nobody waiting to be served!")
    
    