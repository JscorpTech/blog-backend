from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FaqView, CategoryView, TagView, PostView, StackView, ExperienceView, EducationView, ProjectView, \
    StackCategoryView

router = DefaultRouter()
router.register("faq", FaqView, basename="faq")
router.register("category", CategoryView, basename="category")
router.register("tag", TagView, basename="tag")
router.register("post", PostView, basename="post")
router.register("stack", StackCategoryView, basename="stack")
router.register("experience", ExperienceView, basename="experience")
router.register("education", EducationView, basename="education")
router.register("project", ProjectView, basename="project")

urlpatterns = [
    path("", include(router.urls)),
]
