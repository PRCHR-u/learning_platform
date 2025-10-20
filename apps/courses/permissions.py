from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'teacher'


class IsMaterialCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.course.owner == request.user
