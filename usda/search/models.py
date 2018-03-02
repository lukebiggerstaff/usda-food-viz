from django.db import models

# Create your models here.


class Food(models.Model):
    """food and accompanying nutritional information"""

    ndb_no = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=69)
    water = models.FloatField(null=True, blank=True)
    kcal = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    carbohydrates = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    sugar = models.FloatField(null=True, blank=True)
    calcium = models.FloatField(null=True, blank=True)
    iron =   models.FloatField(null=True, blank=True)
    magnesium = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    zinc = models.FloatField(null=True, blank=True)
    folate = models.FloatField(null=True, blank=True)
    vitamin_b12 = models.FloatField(null=True, blank=True)
    vitamin_a = models.FloatField(null=True, blank=True)
    vitamin_c = models.FloatField(null=True, blank=True)
    vitamin_d = models.FloatField(null=True, blank=True)

    def find_string_index(self, string):
        return self.description.lower().find(string.lower())

    def __repr__(self):
        return self.description.split(',')[0]
