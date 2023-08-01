"""
CP1404/CP5632 Practical
Project Management Program
"""
import datetime
from prac_07.project import Project


def main():
    """Read file of programming language details, save as objects, display."""
    # Loop through and display all languages (using their str method)
    display_menu()
    data = []
    get_menu_choice(input('>>> ').upper(), data)


def display_menu():
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new "
          "project\n- (U)pdate project\n- (Q)uit")


def get_menu_choice(choice, projects):
    """Check the user choice and pass to other function that used"""
    if choice == 'L':
        filename = input('Please enter the filename you want to load\n>>> ')
        projects = read_file(filename)
        display_menu()
        get_menu_choice(input('>>> ').upper(), projects)
    elif choice == 'S':
        save_file(projects)
        display_menu()
        get_menu_choice(input('>>> ').upper(), projects)
    elif choice == 'D':
        display_projects(projects)
        get_menu_choice(input('>>> ').upper(), projects)
    elif choice == 'F':
        filter_projects_by_date(projects)
        display_menu()
        get_menu_choice(input('>>> ').upper(), projects)
    elif choice == 'A':
        projects = add_new_project(projects)
        display_menu()
        get_menu_choice(input('>>> ').upper(), projects)
    elif choice == 'U':
        projects = change_project_percentage_and_priority(projects)
        display_menu()
        get_menu_choice(input('>>> ').upper(), projects)
    elif choice == 'Q':
        print('Thank you for using custom-built project management software.')
    else:
        print('Invalid menu choice')
        display_menu()
        get_menu_choice(input('>>> ').upper(), projects)


def read_file(filename):
    data = []
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for x in in_file:
            data.append(x.strip().split('\t'))
        for i in range(len(data)):
            projects.append(Project(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
    return projects


def display_projects(projects):
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            complete_projects.append(project)
        if project.completion_percentage < 100:
            incomplete_projects.append(project)
    incomplete_projects = sorted(incomplete_projects)
    complete_projects = sorted(complete_projects)
    print('Incomplete projects:')
    for line in incomplete_projects:
        print(line)
    print('Completed projects:')
    for line in complete_projects:
        print(line)


def filter_projects_by_date(projects):
    target_date = input('Show projects that start after date (dd/mm/yy): ')
    target_date = datetime.datetime.strptime(target_date, "%d/%m/%Y").date()
    lists = []
    for project in projects:
        if project.start_date >= target_date:
            lists.append(project)
    lists = sorted(lists, key=lambda x: x.start_date)
    for line in lists:
        print(line)


def add_new_project(projects):
    print("Let's add a new project")
    name = input('Name: ')
    Start_date = input("Start date (dd/mm/yy): ")
    Priority = input("Priority: ")
    Cost_estimate = input("Cost estimate: $")
    Percent_complete = input("Percent complete: ")
    projects.append(Project(name, Start_date, Priority, Cost_estimate, Percent_complete))
    return projects


def change_project_percentage_and_priority(projects):
    i = 0
    for line in projects:
        print(f"{i}{line}")
        i = i + 1
    project_choice = input("Project choice: ")
    print(projects[int(project_choice)])
    new_percentage = input("New Percentage: ")
    if new_percentage != ' ' and new_percentage != '':
        projects[int(project_choice)].completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority != ' ' and new_priority != '':
        projects[int(project_choice)].priority = int(new_priority)
    return projects


def save_file(projects):
    file_to_save = input("Enter filename of save: ")
    with open(file_to_save, 'w') as write_file:
        write_file.write('Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage')
        for line in projects:
            write_file.write('\n')
            write_file.write(f"{line.name}\t{line.start_date.strftime('%d/%m/%Y')}\t{line.priority}\t"
                             f"{line.cost_estimate:.2f}\t{line.completion_percentage}")


main()
