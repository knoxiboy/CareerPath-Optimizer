# CareerPath Optimizer

**A Greedy and Dynamic Programming Based Learning Roadmap Generator**

---

## Problem Statement

Students today face an overwhelming number of online courses and resources. Choosing the right combination of courses that maximizes learning value within limited study time is a classic optimization problem. Without a structured approach, students may waste time on low-impact courses or miss high-value ones.

## Objective

Build a clean, professional web application where students can:
1. Select a **career goal** (Full Stack Developer, Data Scientist, AI/ML Engineer, DevOps Engineer).
2. Choose their **skill level** (Beginner, Intermediate, Advanced).
3. Set **available study hours**.
4. Receive an **optimized learning roadmap** generated using two algorithmic approaches.

The app compares **Greedy Algorithm** and **Dynamic Programming (0/1 Knapsack)** to demonstrate the trade-offs between speed and optimality in course selection.

---

## Tech Stack

| Technology   | Purpose                        |
|-------------|-------------------------------|
| Python 3.10+ | Core programming language     |
| Streamlit    | Frontend / Web UI             |
| Pandas       | Data manipulation & display   |
| Matplotlib   | Bar chart visualizations      |
| JSON         | Course dataset storage        |

- No database required
- No authentication
- No external APIs
- No AI/LLM integration

---

## Algorithms Used

### 1. Greedy Algorithm

**Purpose:** Provide a fast recommendation by prioritizing courses with the highest benefit per hour.

**Formula:**
```
ratio = value / hours
```

**Steps:**
1. Calculate `value_per_hour` for each course.
2. Sort courses in **descending** order of ratio.
3. Iterate and select courses while `total_hours ≤ available_hours`.
4. Return the selected courses, total hours, and total value.

**Complexity:** O(n log n)
**Trade-off:** Fast but may not always produce the globally optimal solution.

---

### 2. Dynamic Programming — 0/1 Knapsack

**Purpose:** Find the mathematically optimal combination of courses that maximizes total value within the study hour budget.

**Knapsack Mapping:**
| Knapsack Concept | Course Equivalent     |
|------------------|-----------------------|
| Item             | Course                |
| Weight           | Course hours          |
| Profit           | Course value (1–10)   |
| Capacity         | Available study hours |

**DP State:**
```
dp[i][w] = maximum value using first i courses with capacity w
```

**Transition:**
```
if course_hours ≤ w:
    dp[i][w] = max(dp[i-1][w], value + dp[i-1][w - course_hours])
else:
    dp[i][w] = dp[i-1][w]
```

**Backtracking:**
1. Start from `dp[n][max_hours]`.
2. If `dp[i][w] ≠ dp[i-1][w]`, the course was selected.
3. Subtract its hours and continue backwards.
4. Reverse the list to restore original order.

**Complexity:** O(n × W)
**Trade-off:** Always optimal but uses more computation and memory.

---

## Project Structure

```
careerpath-optimizer/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── algorithms/
│   ├── __init__.py
│   ├── greedy_selector.py      # Greedy algorithm implementation
│   └── dp_knapsack.py          # 0/1 Knapsack DP implementation
│
├── data/
│   └── courses.json            # Course dataset (30 courses)
│
└── utils/
    ├── __init__.py
    └── data_loader.py          # JSON loader and course filtering
```

---

## Features

1. **Home Section** — Project overview explaining both algorithms.
2. **Sidebar Input** — Career goal, skill level, and study hours selection.
3. **Course Table** — View all relevant courses for your selection.
4. **Greedy Recommendation** — Fast, ratio-based course selection.
5. **DP Optimized Roadmap** — Mathematically optimal course combination.
6. **Side-by-Side Comparison** — Greedy vs DP metrics and course lists.
7. **Visual Roadmap** — Ordered learning steps from the optimal result.
8. **Bar Charts** — Matplotlib comparison of hours and value.
9. **Algorithm Explanations** — Detailed cards explaining how each algorithm works.
10. **Edge Case Handling** — Graceful handling of no courses, low hours, empty results.

---

## How to Run

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

```bash
# Clone or navigate to the project directory
cd careerpath-optimizer

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Sample Output

### User Inputs:
- **Career Goal:** Data Scientist
- **Skill Level:** Beginner
- **Available Hours:** 25

### Greedy Result:
| Course                    | Hours | Value | Val/Hr |
|--------------------------|-------|-------|--------|
| Statistics and Probability | 8     | 9     | 1.13   |
| Pandas and Data Wrangling  | 7     | 8     | 1.14   |
| Python for Data Science    | 10    | 10    | 1.00   |
| **Total**                  | **25**| **27**|        |

### DP Result:
| Course                    | Hours | Value | Val/Hr |
|--------------------------|-------|-------|--------|
| Python for Data Science    | 10    | 10    | 1.00   |
| Statistics and Probability | 8     | 9     | 1.13   |
| Pandas and Data Wrangling  | 7     | 8     | 1.14   |
| **Total**                  | **25**| **27**|        |

### Comparison:
| Algorithm            | Total Hours | Total Value | Nature                          |
|---------------------|-------------|-------------|---------------------------------|
| Greedy              | 25          | 27          | Fast but not always optimal     |
| Dynamic Programming | 25          | 27          | Optimal but uses more computation |

---

## Team Members

| Name          | Role                |
|--------------|---------------------|
| Team Member 1 | Algorithm Design    |
| Team Member 2 | UI Development      |
| Team Member 3 | Data & Testing      |

---

## Submission Note

> This project demonstrates the practical use of **Greedy Algorithm** and **Dynamic Programming** for solving a real-world learning path optimization problem. The application showcases how different algorithmic strategies yield varying results in terms of speed and optimality, providing students with actionable insights for their career development journey.
