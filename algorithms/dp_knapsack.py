"""
Dynamic Programming - 0/1 Knapsack Course Optimizer
=====================================================
Finds the optimal combination of courses that maximizes
total value within the available study hours.

Mapping:
    Course   → Item
    Hours    → Weight
    Value    → Profit
    Max Hours → Knapsack Capacity

Time Complexity : O(n * W)  where n = number of courses, W = max_hours
Space Complexity: O(n * W)  for the DP table
"""


def dp_optimize_courses(courses, max_hours):
    """
    Optimize course selection using 0/1 Knapsack Dynamic Programming.

    Parameters
    ----------
    courses : list[dict]
        List of course dictionaries, each with 'hours' and 'value' keys.
    max_hours : int
        Maximum total study hours (knapsack capacity).

    Returns
    -------
    tuple
        (selected_courses, total_hours, total_value, dp_table)
    """
    if not courses or max_hours <= 0:
        return [], 0, 0, []

    n = len(courses)
    W = int(max_hours)

    # ----- Step 1: Build the DP table -----
    # dp[i][w] = maximum value using first i courses with capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        course_hours = int(courses[i - 1]["hours"])   # weight of current item
        course_value = int(courses[i - 1]["value"])    # profit of current item

        for w in range(W + 1):
            if course_hours <= w:
                # Option A: skip this course  →  dp[i-1][w]
                # Option B: take this course  →  course_value + dp[i-1][w - course_hours]
                dp[i][w] = max(
                    dp[i - 1][w],
                    course_value + dp[i - 1][w - course_hours]
                )
            else:
                # Course doesn't fit → inherit previous row
                dp[i][w] = dp[i - 1][w]

    # ----- Step 2: Backtrack to find which courses were selected -----
    selected_courses = []
    w = W

    for i in range(n, 0, -1):
        # If the value changed from the row above, course i was included
        if dp[i][w] != dp[i - 1][w]:
            selected_courses.append(courses[i - 1])
            w -= int(courses[i - 1]["hours"])  # reduce remaining capacity

    # Reverse to maintain original order
    selected_courses.reverse()

    # ----- Step 3: Compute totals from selected courses -----
    total_hours = sum(int(c["hours"]) for c in selected_courses)
    total_value = sum(int(c["value"]) for c in selected_courses)

    return selected_courses, total_hours, total_value, dp
