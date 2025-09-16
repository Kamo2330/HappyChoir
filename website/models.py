from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(TimestampedModel):
    title = models.CharField(max_length=200)
    date = models.DateField()
    venue = models.CharField(max_length=200, blank=True)
    ticket_url = models.URLField(blank=True)
    is_upcoming = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.date})"


class News(TimestampedModel):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_at = models.DateTimeField()

    class Meta:
        ordering = ['-published_at']

    def __str__(self) -> str:
        return self.title


class Member(TimestampedModel):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to='members/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Testimonial(TimestampedModel):
    quote = models.TextField()
    author = models.CharField(max_length=120, blank=True)
    source = models.CharField(max_length=120, blank=True)

    def __str__(self) -> str:
        return f"{self.author}: {self.quote[:30]}..."

# Create your models here.
