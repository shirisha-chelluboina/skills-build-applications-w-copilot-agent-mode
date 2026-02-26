from django.test import TestCase
from .models import Team, UserProfile, Activity, Leaderboard, Workout

class ModelTestCase(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name="Team Marvel", description="Marvel heroes")
        dc = Team.objects.create(name="Team DC", description="DC heroes")
        ironman = UserProfile.objects.create(name="Iron Man", email="ironman@marvel.com", team=marvel)
        batman = UserProfile.objects.create(name="Batman", email="batman@dc.com", team=dc)
        Activity.objects.create(user=ironman, activity="Running", duration=30)
        Leaderboard.objects.create(team=marvel, points=100)
        Workout.objects.create(user=batman, workout="Push-ups", reps=50)

    def test_team_count(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_userprofile_count(self):
        self.assertEqual(UserProfile.objects.count(), 2)

    def test_activity_count(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_leaderboard_count(self):
        self.assertEqual(Leaderboard.objects.count(), 1)

    def test_workout_count(self):
        self.assertEqual(Workout.objects.count(), 1)
