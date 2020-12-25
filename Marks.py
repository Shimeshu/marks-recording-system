import os
import matplotlib.pyplot as plt

def recordMarks(name, std, section, rollno, school, english, hindi, maths, science, history_civics, geography, computer, save):
    try:
        cwd = os.getcwd()
        os.mkdir("{}/Students".format(cwd))
    except FileExistsError:
        print("")
    cwd = os.getcwd()
    file = open("{}/Students/{}.txt".format(cwd, name.capitalize()), "w+")
    file.write("Mark Sheet of %s\n\n" % name.capitalize())
    file.write('Name of the Student -> %s\n\n' % name)
    file.write("Class -> {}\n\n".format(std))
    file.write("Section -> {}\n\n".format(section))
    file.write("Roll Number -> {}\n\n".format(rollno))
    file.write("School Name -> {}\n\n".format(school))
    file.write("Marks in English : {}\n\n".format(english))
    file.write("Marks in Hindi : {}\n\n".format(hindi))
    file.write("Marks in Maths : {}\n\n".format(maths))
    file.write("Marks in Science : {}\n\n".format(science))
    file.write("Marks in History and Civics : {}\n\n".format(history_civics))
    file.write("Marks in Geography : {}\n\n".format(geography))
    file.write("Marks in Computer : {}\n\n".format(computer))
    total = english + hindi + maths + science + history_civics + geography + computer
    percentage = total/1000*100
    file.write("Total Marks : {}\n\n".format(total))
    file.write("Percentage = {}\n\n".format(percentage))
    file.close()
    file = open("{}/Students/{}.txt".format(cwd, name.capitalize()), "r")
    print(file.read())
    if save == "y":
        file.close()
    else:
        file.close()
        os.remove("{}.txt".format(name.capitalize()))

try:
    name = input('Enter Your Name -> ').capitalize()
    std = int(input('Enter Your Class [Without Section] -> '))
    section = input('Enter your Section -> ').upper()
    rollno = int(input("Enter your Roll Number -> "))
    school = input("Enter Your School Name -> ").capitalize()
    english = int(input("Enter Marks in English -> "))
    hindi = int(input("Enter Marks in Hindi -> "))
    maths = int(input("Enter Marks in Maths -> "))
    science = int(input("Enter Marks in Science -> "))
    history_civics = int(input("Enter Marks in History and Civics -> "))
    geography = int(input("Enter Marks in Geography -> "))
    computer = int(input("Enter Marks in Computer -> "))
    save = input("Do you want the keep the file [y/n] -> ").lower()
except ValueError:
    print("Enter The Details Properly!!\nGive Integer Values for Class, Roll Number and Marks")
except TypeError:
    print("All the Details are Mandatory!!")
else:
    recordMarks(name, std, section, rollno, school, english, hindi, maths, science, history_civics, geography, computer, save)

    graph = input("Do you want to see your Marks Graph [y/n] -> ").lower()

    if graph == "y":
        plt.pie([english, hindi, maths, science, history_civics, geography, computer], labels=['English', 'Hindi', 'Maths', 'Science', 'History/Civics', 'Geography', 'Computer'])
        savegraph = input("Do you Want to Save the Graph [y/n] -> ").lower()
        if savegraph == "y":
            plt.savefig("Graph.jpg")
            plt.show()
        else:
        	plt.show()
    elif graph == "n":
        print("Thank You for Using The Marks System!! :)")
    else:
        print("Thank You for Using The Marks System!! :)")
