#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            val_1 = my_list_1[i] if i < len(my_list_1) else 0
            val_2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(val_1, (int, float)) or not isinstance(val_2, (int, float)):
                raise TypeError("wrong type")

            if val_2 == 0:
                raise ZeroDivisionError("division by 0")

            result = val_1 / val_2
        except TypeError as e:
            print(e)
            result = 0
        except ZeroDivisionError as e:
            print(e)
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
