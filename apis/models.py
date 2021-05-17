from django.db import models


class Project(models.Model):
    # Project type

    DESIGN = 'design'
    WEBSITE = 'website'
    APP = 'app'

    PROJECT_TYPES = (
        (DESIGN, 'design'),
        (WEBSITE, 'website'),
        (APP, 'app')
    )

    # Fields
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default=WEBSITE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''



class Team(models.Model):
    # Project type

    CORE = 'core'
    BUSINESS = 'business'
    CONTRIBUTOR = 'contributor'

    TEAM_TYPES = (
        (CORE, 'core'),
        (BUSINESS, 'business'),
        (CONTRIBUTOR, 'contributor')
    )

    # Fields
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    portfolio = models.CharField(max_length=255, blank=True, null=True)
    github = models.CharField(max_length=255, blank=True, null=True)
    discord = models.CharField(max_length=255, blank=True, null=True)
    team_type = models.CharField(max_length=20, choices=TEAM_TYPES, default=CONTRIBUTOR)
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''