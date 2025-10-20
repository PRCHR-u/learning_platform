from django.views.generic import TemplateView


class TeacherDashboardView(TemplateView):
    template_name = "teacher_dashboard.html"
