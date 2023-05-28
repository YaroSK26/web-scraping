with open("./input/letter.txt") as letter:
    letter_content = letter.read()

with open("./input/names.txt") as names:
    list = names.readlines()

for one_name in list:
    one_name = one_name.strip()

    replace_text = letter_content.replace("[name]" , one_name)

    with open(f"./output/letter_{one_name}.txt", mode="w") as final_letter:
        final_letter.write(replace_text)