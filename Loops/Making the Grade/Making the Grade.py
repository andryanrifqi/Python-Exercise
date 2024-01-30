"""Functions for organizing and calculating student exam scores."""
def round_scores(student_scores):
    """Round all provided student scores.
 
    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    new_list = []
    for score in student_scores:
        new_list.append(round(score))
    return new_list

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.
 
    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_student = 0
    for score in student_scores:
        if score <= 40:
            failed_student += 1
    return failed_student