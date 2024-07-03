class Student():
    def __init__(self, name: str, email: str, ID: str) -> None:
        self.__name: str = name
        self.__email: str  = email
        self.__ID: str = ID
        self.__courses: dict = {"CLI": 0, "PYTHON": 0, "DATABASES": 0, "DJANGO": 0}
    
    def get_ID(self):
        return self.__ID
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_courses(self):
        return self.__courses
    
    def update_courses(self, course_name: str, score: int):
        if course_name in self.__courses:
            self.__courses[course_name] = score
        else:
            raise KeyError(f"Course '{course_name}' does not exist for this student.")