"""Task 4.3. File data/students.csv stores information about students in CSV format.
This file contains the student’s names, age and average mark.

Implement a function which receives file path and returns names of top performer students
Implement a function which receives the file path with students info and writes CSV student information
to the new file in descending order of age"""
import pandas as pd


def get_top_performers(file_path, number_of_top_students=5):
    result_list = []
    df = pd.read_csv(file_path, delimiter=',', names=['name', 'age', 'mark'], index_col='name', skiprows=1)
    df = df.sort_values(by=['mark', 'name'], ascending=[False, True])
    words = df.index
    words = words.tolist()
    for word in words[:number_of_top_students]:
        result_list.append(word)
    return result_list


def get_top_performers2(file_path):

    df = pd.read_csv(file_path, delimiter=',', names=['Student name', 'age', 'average mark'], index_col='Student name',
                     skiprows=1)
    df = df.sort_values(by=['age', 'Student name'], ascending=[False, True])
    df.to_csv('result.csv', sep=',', header=True, mode='w')
