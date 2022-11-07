# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestPlannerViews(TestCase):
    """
    A class for testing planner view
    """
    def test_get_planner_page(self):
        """
        This test checks if the planner page is displayed
        """
        response = self.client.get('/planner/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plannerapp/planner.html')

    def test_choose_date(self):
        """
        This test checks the display of the date picker page
        """
        response = self.client.get('/planner/choose_date/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plannerapp/choose_date.html')
