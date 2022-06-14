from import_export import resources
from .models import Players

class PersonResource(resources.ModelResource):
    class Meta:
        model = Players