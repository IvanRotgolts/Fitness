import random
FILE_NAME=r"C:\MyPrograms\individual_projects\fitness\questions.txt"

def read(file_name):
    try:
        with open(file_name,"r",encoding="utf-8") as file:
            lines=file.readlines()
        return lines
    except FileNotFoundError as err:
        print("Невозможно открыть файл")
        return ["не работает"]

def convert(lines):
    questions=list()
    for line in lines:
        line_list=line.split("|")
        questions.append(line_list)
    return questions

def shuffle(lines):
    for i in range(0,len(lines)):
        random_index=random.randint(0,len(lines)-1)
        lines[i],lines[random_index]=lines[random_index],lines[i]

def delete_new_line_sign(lines):
    for i in range(0,len(lines)):
        lines[i]=lines[i].replace("\n","")

def shuffle_2(lines):
    
    for element in lines:
        random_index=random.randint(0,len(lines)-1)
        lines[random_index].append(element)
        index_element=lines.index(element)
        lines.remove(index_element)

def shuffle_answers(lines):
    for line in lines:
        for i in range(2,len(line)):
            index=random.randint(2,len(line)-1)
            line[index],line[i]=line[i],line[index]




read_result=read(FILE_NAME)
delete_new_line_sign(read_result)
convert_result=convert(read_result)
shuffle(convert_result)
shuffle_answers(convert_result)
#shuffle_2(convert_result)
print(convert_result)