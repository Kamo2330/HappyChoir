from django.contrib import admin
from .models import Event, News, Member, Testimonial


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "venue", "is_upcoming")
    list_filter = ("is_upcoming", "date")
    search_fields = ("title", "venue")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at")
    search_fields = ("title", "body")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ("name", "role")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author",)
    search_fields = ("author", "quote", "source")

# Register your models here.
