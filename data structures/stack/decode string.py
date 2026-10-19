s="2[abc]3[cd]ef"
count_stack=[]
prev_string_stack=[]
repeat=0
curr_string=""

for item in s:
    if item.isdigit():
        repeat = repeat*10 + int(item)
    elif item == "[":
        count_stack.append(repeat)
        prev_string_stack.append(curr_string)
        repeat=0
        curr_string=""
    elif item.isalpha():
        curr_string = curr_string + item
    elif item == "]":
        curr_string = prev_string_stack.pop() + curr_string * count_stack.pop()

print(curr_string)