class Menu:
    
    def __init__(self) -> None:
        pass

    def display_main_menu(self):
        print(f" ------------------------------------------------\n"
          "|                    Main Menu                   |\n"
          "|You can see the commands  available to you below|\n"
          " ------------------------------------------------\n"
          "0: Exit            1: Add student   2: List students\n"
          "3: Update progress 4: View progress 5: Statistics")
        
    def display_add_student(self):
        print(f" -----------------------------------------------\n"
          "|                   Add Student                 |\n"
          "|Add a student's details or go back to main menu|\n"
          " -----------------------------------------------\n"
          "        0: Back to the previous menu       ")
    
    def display_student_list(self):
        print(f" ---------------------------------------------------\n"
          "|                   List Student(s)                 |\n"
          "|You are viewing the list of all registered students|\n"
          " ---------------------------------------------------")
        
    def display_update_progress(self):
        print(f" -----------------------------------------------------\n"
          "|                    Update Progress                  |\n"
          "|Update a student's progress on all 4 courses using ID|\n"
          "|Courses available:  CLI   PYTHON   DATABASES   DJANGO|\n"
          " -----------------------------------------------------\n"
          "              0: Back to the previous menu       ")
        
    def display_view_progress(self):
        print(f" ------------------------------------------------\n"
          "|                   View Progress                |\n"
          "|Enter the ID of a student to view their progress|\n"
          " ------------------------------------------------\n"
          "             0: Back to the previous menu       ")
        
    def display_statistics(self):
        print(f" ------------------------------------------\n"
          "|                Statistics                |\n"
          "|View statistics about the courses provided|\n"
          " ------------------------------------------\n"
          "         0: Back to the previous menu       ")
        
if __name__ == "__main__":
    menu = Menu()
    menu.display_main_menu()
    menu.display_add_student()
    menu.display_student_list()
    menu.display_update_progress()
    menu.display_view_progress()
    menu.display_statistics()