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