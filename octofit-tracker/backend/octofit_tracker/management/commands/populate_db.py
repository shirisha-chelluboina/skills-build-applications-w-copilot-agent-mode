
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, UserProfile, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Delete all data, ignore errors if collections are empty
        for model in [Activity, Workout, Leaderboard, UserProfile, Team]:
            try:
                model.objects.all().delete()
            except Exception:
                pass

        # Teams
        marvel = Team.objects.create(name="Team Marvel", description="Superheroes from Marvel")
        dc = Team.objects.create(name="Team DC", description="Superheroes from DC")

        # Users
        ironman = UserProfile.objects.create(name="Iron Man", email="ironman@marvel.com", team=marvel)
        cap = UserProfile.objects.create(name="Captain America", email="cap@marvel.com", team=marvel)
        spiderman = UserProfile.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=marvel)
        batman = UserProfile.objects.create(name="Batman", email="batman@dc.com", team=dc)
        superman = UserProfile.objects.create(name="Superman", email="superman@dc.com", team=dc)
        wonderwoman = UserProfile.objects.create(name="Wonder Woman", email="wonderwoman@dc.com", team=dc)

        # Activities
        Activity.objects.create(user=ironman, activity="Running", duration=30)
        Activity.objects.create(user=batman, activity="Cycling", duration=45)
        Activity.objects.create(user=wonderwoman, activity="Swimming", duration=60)

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=250)
        Leaderboard.objects.create(team=dc, points=300)

        # Workouts
        Workout.objects.create(user=spiderman, workout="Push-ups", reps=100)
        Workout.objects.create(user=superman, workout="Squats", reps=150)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data using Django ORM.'))
