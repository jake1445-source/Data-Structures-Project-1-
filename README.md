# 🗓️ Campus Event Scheduler

## 📘 Overview
The **Campus Event Scheduler** is a Python-based application that helps manage, sort, and detect conflicts among scheduled campus events. It supports both **array-based** and **linked list-based** data structures for storing event data, allowing comparisons of performance and efficiency. Additionally, a **parallelized conflict detection** module enhances performance for large datasets.

---

## 📁 Project Structure

```
CAMPUS-EVENT-SCHEDULER/
│
├── src/
│   ├── EventsList.py              # Defines the Event class and event management logic
│   ├── LinkedList.py              # Implements linked list structure for event storage
│   ├── Sorting.py                 # Provides sorting algorithms (e.g., merge, quick, bubble)
│   ├── Search_and_Conflict.py     # Detects scheduling conflicts (sequential + parallelized)
│
├── testing/
│   ├── Sorting_Test.py            # Unit tests for sorting algorithms
│
├── Final_Report.ipynb             # Detailed report notebook
├── Report_Notebook.ipynb          # Exploratory and analysis notebook
└── Readme.md                      # Project documentation
```

---

## ⚙️ Features

- 📅 **Event Management** – Create, view, and organize campus events.
- 🔗 **Linked List & Array Support** – Compare event operations using different data structures.
- 🧩 **Sorting Algorithms** – Implements multiple sorting methods to order events by date/time.
- ⚔️ **Conflict Detection** – Identify overlapping or conflicting events.
- 🚀 **Parallelized Conflict Search** – Uses Python’s multiprocessing to speed up conflict detection.
- 🧪 **Testing Suite** – Unit tests to validate sorting and searching functionalities.

---

## 🧠 Core Concepts

| Module | Description |
|--------|--------------|
| **EventsList.py** | Contains the `Event` class and helper functions for creating and managing events. |
| **LinkedList.py** | Implements a custom singly linked list structure. |
| **Sorting.py** | Houses different sorting algorithms and benchmarking utilities. |
| **Search_and_Conflict.py** | Detects overlapping events sequentially and in parallel. |

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Campus-Event-Scheduler.git
   cd Campus-Event-Scheduler
   ```

2. Run the main script or notebooks:
   ```bash
   python src/EventsList.py
   ```

   Or explore results in Jupyter:
   ```bash
   jupyter notebook Report_Notebook.ipynb
   ```

---

## 🧪 Running Tests
To execute all tests:
```bash
python -m unittest discover testing
```

---

## 📈 Future Improvements
- Add a GUI or web dashboard using Flask/Streamlit.
- Integrate with a real database (e.g., SQLite/PostgreSQL).
- Implement user authentication for personalized scheduling.

---

## 👨‍💻 Contributors
**Atharva Zodpe** – Developer & Author

---

## 📜 License
This project is released under the MIT License.
