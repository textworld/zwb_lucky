from datetime import datetime

from django.template.loader import render_to_string
from django.test import TestCase


# Create your tests here.
class EmailTestCase(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        lucky_str = "01,02,03,04,05,06,07"
        nums = lucky_str.split(",")
        report = render_to_string("email_template.html", context={
            "send_time": datetime.now().strftime("%Y年%m月%d日 %H:%M:%S"),
            "lucky_str": lucky_str,
            "red_nums": ' '.join(nums[:6]),
            "blue_num": nums[6]
        })
        self.assertTrue(report is not None)
