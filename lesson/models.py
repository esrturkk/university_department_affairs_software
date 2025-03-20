from django.db import models
from user.models import User,Student
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    course_credit = models.IntegerField()
    course_level = models.IntegerField()

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"

    
class Classroom(models.Model):
    classroom_name = models.CharField(max_length=50, unique=True)
    classroom_capacity = models.IntegerField()

    def __str__(self):
        return f"{self.classroom_name} (Capacity: {self.classroom_capacity})"
    


class CourseSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.course_name} on {self.get_day_of_week_display()} at {self.start_time}"

class ExamSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    note = models.TextField(blank=True, null=True)  # yorum alanı

    def __str__(self):
        return f"{self.course.course_name} Exam on {self.exam_day}"

class InvigilatorAssignment(models.Model):
    exam = models.ForeignKey(ExamSchedule, on_delete=models.CASCADE)
    invigilator = models.ForeignKey(User, on_delete=models.CASCADE)  # öğretim üyesi veya bölüm başkanı

    def __str__(self):
        return f"{self.invigilator.username} - {self.exam.course.course_name} Exam"


class ExamSeatingArrangement(models.Model):
    exam = models.ForeignKey(ExamSchedule, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=20)
    seat_number = models.IntegerField()

    def __str__(self):
        return f"Student {self.student_number} - Seat {self.seat_number} in {self.classroom.classroom_name}"


class InstructorSchedule(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.instructor.username} - {self.course.course_name} on {self.get_day_of_week_display()}"
