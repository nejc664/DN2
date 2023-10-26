our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

remove_value = our_list[3]

our_dict["d"] = remove_value

result_tube = tuple(our_dict.values())

primer = remove_value == our_dict

print("Primerjava izračuna:", primer)
