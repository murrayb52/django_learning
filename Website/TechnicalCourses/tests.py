from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Allcourses, details


# Create your tests here.
class AllcoursesModelTest(TestCase):
    # This method returns False for all courses to be published in the future
    def test_was_published_recently_with_future_course(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Allcourses(startedfrom=time)
        # assertIs will check our output with the intended output, False
        self.assertIs(future_question.was_published_recently(), False)

    # This method returns False for all courses whose published day is older than 1 day
    def test_was_published_recently_with_old_course(self):
        time=timezone.now()-datetime.timedelta(days=1, seconds=1)
        old_course=Allcourses(startedfrom=time)
        self.assertIs(old_course.was_published_recently(),False)

    # This method retunrs True for all courses that have been published within 1 day
    def test_was_published_recently_with_recent_course(self):
        time=timezone.now()-datetime.timedelta(hours=23, minutes=59, seconds=59)
        old_course=Allcourses(startedfrom=time)
        self.assertIs(old_course.was_published_recently(),True)