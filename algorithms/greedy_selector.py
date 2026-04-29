"""
Greedy Algorithm - Course Selector
====================================
Selects courses with the highest value-per-hour ratio first,
filling the available study hours greedily.

This approach is fast (O(n log n) due to sorting) but may not
always produce the globally optimal solution.
"""


def greedy_select_courses(courses, max_hours):
    """
    Select courses using a Greedy approach based on value/hour ratio.

    Parameters
    ----------
    courses : list[dict]
        List of course dictionaries, each with 'hours' and 'value' keys.
    max_hours : int
        Maximum total study hours available.

    Returns
    -------
    tuple
        (selected_courses, total_hours, total_value)
    """
    if not courses or max_hours <= 0:
        return [], 0, 0

    # Step 1: Calculate the value-per-hour ratio for every course
    for course in courses:
        course["ratio"] = round(course["value"] / course["hours"], 4)

    # Step 2: Sort courses in descending order of ratio (best bang-for-buck first)
    sorted_courses = sorted(courses, key=lambda c: c["ratio"], reverse=True)

    selected_courses = []
    total_hours = 0
    total_value = 0

    # Step 3: Iterate and greedily pick courses that fit
    for course in sorted_courses:
        if total_hours + course["hours"] <= max_hours:
            # Course fits within remaining budget → select it
            selected_courses.append(course)
            total_hours += course["hours"]
            total_value += course["value"]

    return selected_courses, total_hours, total_value
