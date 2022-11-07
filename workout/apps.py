# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PlannerappConfig(AppConfig):
    """
    A class for configuring the planner app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plannerapp'
