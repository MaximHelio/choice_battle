from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    red = models.TextField()
    blue = models.TextField()
    red_img = models.ImageField(upload_to="either", null=True, blank=True)
    red_img = models.ImageField(upload_to="either", null=True)
    slug = models.SlugField(max_length=100, null=True)
    poster_path = models.CharField(max_length=500)
    
    def __str__(self):
        return f'{self.title}: {self.red} vs {self.blue}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Choice(models.Model):
    RED = 'RED'
    BLUE = 'BLUE'
    movie_choices = [
        (RED, 'RED'),
        (BLUE, 'BLUE'),
    ]
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,)
    choice = models.CharField(max_length=2, choices=movie_choices)
    
    def __str__(self):
        return f'{self.movie.title}: {self.choice}'