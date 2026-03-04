
def list_of_names(student_dictionary,/):
    """Displays A Sorted Dictionary By Last Name"""
    #Check if there is values in the dictionary
    if student_dictionary == {}:
        print("WARNING: DICTIONARY IS EMPTY!")
        return None
    #Sort the dictionary by last name
    output_list = []
    sorted_student_dictionary = sorted(student_dictionary.items(), key = lambda x: x[1]["lastname"])
    for first_and_last in sorted_student_dictionary:
       first_name = first_and_last[1]["firstname"]
       last_name = first_and_last[1]["lastname"]
       new_entry = [last_name, first_name]
       output_list.append(new_entry)
    return output_list

def student_hw_avg(student_dictionary,/,*,id):
    """Averages All Homework Scores"""
    #Check if the value exists
    if id not in student_dictionary:
        print("WARNING: INVALID ID!")
        return None
    total_homework_scores = student_dictionary[id]["HW_scores"]
    return (sum(total_homework_scores)/len(total_homework_scores))

def class_hw_avg(student_dic,/,*,hw_index):
    """Averages Homework Based On Class"""
    scores_in_class = []
    for student in student_dic.items():
        # Check if the index is in range
        if hw_index in range(len(student[1]["HW_scores"])):
            score_to_add = student[1]["HW_scores"][hw_index]
            scores_in_class.append(score_to_add)
        else:
            print("WARNING: INDEX OUT OF RANGE!")
            return None
    return (sum(scores_in_class)/len(scores_in_class))




