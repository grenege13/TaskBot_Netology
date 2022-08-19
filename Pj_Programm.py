HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи
запрашиваем у пользователя).
show - напечатать все добавленные задачи."""


today = []
tomorrow = []
other = []
tasks = [today, tomorrow, other]

run = True

while run:
    command = input("Введите команду: ")

    if command == "help":
        print(HELP)

    elif command == "show":
        print (tasks)

    elif command == "add":

        temp_task = input("На какой день записать задачу? \n ")
        if temp_task == "Сегодня":
            task = input("Введите название задачи: ")
            today.append(task)
            print("Задача добавлена! ")

        elif temp_task == "Завтра":
            task = input("Введите название задачи: ")
            tomorrow.append(task)
            print("Задача добавлена! ")

        else:
            task = input("Введите название задачи: ") 
            other.append(task)  
            print("Задача добавлена! ") 

    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break

    else:
        print("Неизвестная команда") 
        break
