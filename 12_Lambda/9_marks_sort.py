# Given marks = [45, 78, 32, 90, 59], use sorted() with a lambda to sort the marks from highest to lowest.

marks = [45, 78, 32, 90, 59]
sorted_marks = list(sorted(marks, key=lambda mark: mark))
print(sorted_marks)