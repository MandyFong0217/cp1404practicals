"""
CP1404/CP5632 Practical
Project Management Program
"""
import datetime
from prac_07.project import Project


def main():
    display_menu()
    projects = []
    get_menu_choice(input('>>> ').upper(), projects)


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
    """Prompt the user for a filename to load projects from and load them"""
    temp_od_projects = []
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for x in in_file:
            temp_od_projects.append(x.strip().split('\t'))
        for i in range(len(temp_od_projects)):
            projects.append(Project(temp_od_projects[i][0], temp_od_projects[i][1], temp_od_projects[i][2],
                                    temp_od_projects[i][3], temp_od_projects[i][4]))
    return projects


def display_projects(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
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
    """Ask the user for a date and display only projects that start after that date, sorted by date"""
    target_date = input('Show projects that start after date (dd/mm/yy): ')
    target_date = datetime.datetime.strptime(target_date, "%d/%m/%Y").date()
    filter_projects = []
    for project in projects:
        if project.start_date >= target_date:
            filter_projects.append(project)
    filter_projects = sorted(filter_projects, key=lambda x: x.start_date)
    for line in filter_projects:
        print(line)


def add_new_project(projects):
    """Ask the user for the inputs and add a new project to memory"""
    print("Let's add a new project")
    new_name = input('Name: ')
    new_start_date = input("Start date (dd/mm/yy): ")
    new_priority = input("Priority: ")
    new_cost_estimate = input("Cost estimate: $")
    new_percent_complete = input("Percent complete: ")
    projects.append(Project(new_name, new_start_date, new_priority, new_cost_estimate, new_percent_complete))
    return projects


def change_project_percentage_and_priority(projects):
    """Choose a project, then modify the completion % and/or priority"""
    index_of_project = 0
    for line in projects:
        print(f"{index_of_project}{line}")
        index_of_project = index_of_project + 1
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
    """Prompt the user for a filename to save projects to and save them"""
    file_to_save = input("Enter filename of save: ")
    with open(file_to_save, 'w') as write_file:
        write_file.write('Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage')
        for line in projects:
            write_file.write('\n')
            write_file.write(f"{line.name}\t{line.start_date.strftime('%d/%m/%Y')}\t{line.priority}\t"
                             f"{line.cost_estimate:.2f}\t{line.completion_percentage}")


main()
