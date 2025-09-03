
my_str = ' {{{}}'

open_count = my_str.count("{")
close_count = my_str.count("}")

if open_count > close_count:
    print("Closed bracket is exceed than open bracket")
else:
    total_count = open_count + close_count
    print("Total count of brackets given by user: ",total_count)
