from django.db import models

# Create your models here.
class Projects:
    def __init__(self, title: str, description: str, draft: bool = True):
        self.title = title
        self.description = description
        self.draft = draft

    def is_draft(self):
        return self.draft
    
PROJECTS_DATA = [
    Projects("Proyecto mis animalitos", "Aplicacion para gestión de un zoológico.", False),
    Projects("Proyecto de reciclaje", "Aplicación para promover el reciclaje en la comunidad.", True),
    Projects("Proyecto de agricultura urbana", "Aplicación para la gestión de huertos urbanos.", False),
]