from rest_framework import serializers

from .models import Project, Team

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "link",
            "project_type",
            "get_image",
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "title",
            "email",
            "linkedin",
            "portfolio",
            "github",
            "discord",
            "team_type",
            "get_image",
        )