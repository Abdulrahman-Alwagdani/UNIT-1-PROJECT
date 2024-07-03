from students import Student
from students_manager import StudentManager
from colorama import Fore
from menus import Menu
from validation import Validate

# Used to display menus
menu: Menu = Menu()
# Used to validate user input
validate: Validate = Validate()
# Used to manage students
student_manager: StudentManager = StudentManager()
print(f"{Fore.CYAN}\nWelcome to The Simplified Python Bootcamp Learning Platform!{Fore.RESET}")
input()

def add_student():
    while True:
        menu.display_add_student()
        name: str = input("Enter the student's name: [0 to go back] ")
        if name.lower() == "0":
            print()
            return
        elif validate.is_alphabetic(name):
            while True:
                email: str = input("Enter the student's email address: [0 to go back] ")
                if email.lower() == "0":
                    print()
                    return
                elif validate.is_email(email):
                    student: Student = Student(name, email, student_manager.generate_ID())
                    student_manager.add_student(student)
                    print(f"{Fore.GREEN}{student.get_name()} has been added successfully!{Fore.RESET}")
                    print(f"{student.get_name()}'s ID is: {Fore.YELLOW}{student.get_ID()}{Fore.RESET}")
                    input()
                    return
                else:
                    print(f"{Fore.RED}The email should look like this: \"email@domain.TLD\".{Fore.RESET}")
                    input()
        else:
            print(f"{Fore.RED}The name must be alphabetical.{Fore.RESET}")
            input()

def update_progress():
    while True:
        menu.display_update_progress()
        if student_manager.num_of_students() != 0:
            id: str = input("Enter the student's ID: [0 to go back] ")
            if id.lower() == "0":
                print()
                return
            elif validate.is_ID(id):
                    while True:
                        try:
                            course: str = input("Course name: ").upper()
                            progress: int = int(input(f"{course} Progress: "))
                            student_manager.update_student_courses(id, course, progress)
                            print(f"{Fore.GREEN}{(student_manager.get_student(id)).get_name()}'s progress has been saved!{Fore.RESET}")
                            input()
                        except KeyError as e:
                            print(f"{Fore.RED}Course '{course}' does not exist for this student.{Fore.RESET}")
                            input()
                        except Exception as e:
                            print(e)
                            print(f"{Fore.RED}Please enter the progress in integers!{Fore.RESET}")
                            input()
                        else:
                            choice: str = input("Enter 0 to go back to the main menu, anything else to continue updating: ")
                            if choice.lower() == "0":
                                return
                            else:
                                continue
            else:
                print(f"{Fore.RED}The ID must be unsplit digits!.{Fore.RESET}")
                input()
        else:
            print(f"{Fore.RED}The database is empty! Please add a student first{Fore.RESET}")
            input()
            return

def view_progress():
    while True:
        if student_manager.num_of_students() != 0:
            menu.display_view_progress()
            id: str = input("Enter the student's ID: [0 to go back] ")
            if id.lower() == "0":
                print()
                return
            elif validate.is_ID(id):
                student_manager.get_progress(id)
            else:
                print(f"{Fore.RED}The ID must be unsplit digits!.{Fore.RESET}")
                input()
        else:
            print(f"{Fore.RED}The database is empty! Please add a student first{Fore.RESET}")
            input()
            return

def statistics():
    menu.display_statistics()
    print(f"Average number of {Fore.BLUE}CLI{Fore.RESET} modules completed: {Fore.GREEN}{student_manager.get_cli_avg()}{Fore.RESET}")
    print(f"Average number of {Fore.BLUE}Python{Fore.RESET} modules completed: {Fore.GREEN}{student_manager.get_python_avg()}{Fore.RESET}")
    print(f"Average number of {Fore.BLUE}Databases{Fore.RESET} modules completed: {Fore.GREEN}{student_manager.get_databases_avg()}{Fore.RESET}")
    print(f"Average number of {Fore.BLUE}Django{Fore.RESET} modules completed: {Fore.GREEN}{student_manager.get_django_avg()}{Fore.RESET}")
          

while True:
    try:
        menu.display_main_menu()
        command: str = input("\nPlease enter a command: ")
        # Exit
        if command.lower() == "0":
            print("\nThank you for using our platform. We hope to see you soon!\n")
            break
        # Add student
        elif command.lower() == "1":
            add_student()
        # List students
        elif command.lower() == "2":
            menu.display_student_list()
            student_manager.list_students()
        # Update student progress
        elif command.lower() == "3":
            update_progress()
        # View student progress
        elif command.lower() == "4":
            view_progress()
        # Statistics
        elif command.lower() == "5":
            statistics()
        else:
            print(f"{Fore.RED}Error: invalid input!{Fore.RESET}")
            input()
    except Exception as e:
        print(e)
        print(f"{Fore.RED}Something went wrong. Try again.{Fore.RESET}")
        input()
