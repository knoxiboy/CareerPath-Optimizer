"""
Data Loader Utility
=====================
Loads course data from the JSON dataset and provides
filtering by career goal and skill level.
"""

import json
import os
import copy


def load_courses(filepath=None):
    """
    Load all courses from the JSON file.

    Parameters
    ----------
    filepath : str, optional
        Path to courses.json. Defaults to data/courses.json
        relative to the project root.

    Returns
    -------
    list[dict]
        List of course dictionaries.
    """
    if filepath is None:
        # Resolve path relative to this file's location
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(base_dir, "data", "courses.json")

    with open(filepath, "r", encoding="utf-8") as f:
        courses = json.load(f)

    return courses


def filter_courses(courses, career_goal, level):
    """
    Filter courses by career goal and skill level.

    Parameters
    ----------
    courses : list[dict]
        Full list of courses.
    career_goal : str
        Target career goal (e.g. "Full Stack Developer").
    level : str
        Skill level: "Beginner", "Intermediate", or "Advanced".

    Returns
    -------
    list[dict]
        Deep-copied list of matching courses so algorithm mutations
        (like adding a 'ratio' key) don't affect the originals.
    """
    filtered = [
        copy.deepcopy(c)
        for c in courses
        if c["career_goal"] == career_goal and c["level"] == level
    ]
    return filtered
