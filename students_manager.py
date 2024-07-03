from students import Student
from colorama import Fore
import pickle

class StudentManager:

    __students_record = "students_record.pickle"

    def __init__(self) -> None:
        self.__students: dict = {}
        self.__load_from_file(StudentManager.__students_record)

    def add_student(self, student: Student):
        if student.get_ID() in self.__students:
            raise Exception(f"{Fore.RED}Error: ID already registered!{Fore.RESET}")
        else:
            self.__students[student.get_ID()] = student
            self.__save_to_file(StudentManager.__students_record)
    
    def update_student_courses(self, ID: str, course_name: str, score: int):
        if ID in self.__students:
            try:
                self.__students[ID].update_courses(course_name, score)
                self.__save_to_file(StudentManager.__students_record)
            except KeyError as e:
                raise KeyError(f"{Fore.RED}Error: {e}{Fore.RESET}")
        else:
           raise KeyError(f"{Fore.RED}Error: Student with ID '{Fore.YELLOW}{ID}{Fore.RED}' not found.{Fore.RESET}")

    def generate_ID(self) -> str:
        affix: str = str(self.num_of_students() + 1)
        prefix: str = ""
        for x in range(5 - len(affix)):
            prefix += "0"
        ID: str = prefix + affix
        return ID
    
    def list_students(self):
        if self.num_of_students() == 0:
            print("There are no registered students.")
            input()
        else:
            print(f"Students registered: {self.num_of_students()}")
            for index, student in enumerate(self.__students.values(),start=1):
                print(f"{index}. {Fore.YELLOW}ID: {student.get_ID()}{Fore.RESET} - Name: {student.get_name()} - Email: {student.get_email()}")
            input()

    def num_of_students(self):
        return len(self.__students)
    
    def get_student(self, ID: str):
        if ID in self.__students:
            return self.__students[ID]
        else:
            return -1

    def get_progress(self, ID: str):
        student = self.get_student(ID)
        if student != -1:
            print(f"{Fore.YELLOW}ID: {student.get_ID()}{Fore.RESET} - Name: {student.get_name()}")
            keys: list = list(student.get_courses().keys())
            for key in keys:
                print(f"{key}: {student.get_courses()[key]}")
            input()
        else:
            print(f"There is no registered student with {Fore.YELLOW}ID: {ID}{Fore.RESET}")
            input()


    def get_cli_total(self):
        if self.num_of_students() == 0:
            return 0
        else:
            sum: int = 0
            for student in self.__students:
                sum += self.get_student(str(student)).get_courses()["CLI"]
            return sum
        
    def get_python_total(self):
        if self.num_of_students() == 0:
            return 0
        else:
            sum: int = 0
            for student in self.__students:
                sum += self.get_student(str(student)).get_courses()["PYTHON"]
            return sum
    
    def get_databases_total(self):
        if self.num_of_students() == 0:
            return 0
        else:
            sum: int = 0
            for student in self.__students:
                sum += self.get_student(str(student)).get_courses()["DATABASES"]
            return sum
        
    def get_django_total(self):
        if self.num_of_students() == 0:
            return 0
        else:
            sum: int = 0
            for student in self.__students:
                sum += self.get_student(str(student)).get_courses()["DJANGO"]
            return sum
    
    def get_cli_avg(self):
        if self.num_of_students() == 0:
            return 0
        else:
            sum: int = self.get_cli_total()
            return (sum / self.num_of_students())

    def get_python_avg(self):
        if self.num_of_students() == 0:
            return 0
        else:
            sum: int = self.get_python_total()
            return (sum / self.num_of_students())

    def get_databases_avg(self):
        if self.num_of_students() == 0:
            return 0
        else:
            sum: int = self.get_databases_total()
            return (sum / self.num_of_students())

    def get_django_avg(self):
        if self.num_of_students() == 0:
            return 0
        else:
            sum: int = self.get_django_total()
            return (sum / self.num_of_students())

    def __save_to_file(self, filename: str):
        with open(filename, "wb") as file:
            pickle.dump(self.__students, file)

    def __load_from_file(self, filename: str):
        try:
            with open(filename, "rb") as file:
                self.__students = pickle.load(file)
        except:
            pass
