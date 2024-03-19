from rest_framework import permissions


class IsAuthenticated(permissions.IsAuthenticated):
    message = 'Invalid Auth token provided.'