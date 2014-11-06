from django.contrib import admin
from polls.models import Choice, Question, Mirdb, FruitflyPredictionMiranda, HumanPredictionMiranda, MousePredictionMiranda, NematodePredictionMiranda, RatPredictionMiranda, TarbaseV5 

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Mirdb)
admin.site.register(FruitflyPredictionMiranda)
admin.site.register(HumanPredictionMiranda)
admin.site.register(MousePredictionMiranda)
admin.site.register(NematodePredictionMiranda)
admin.site.register(TarbaseV5)

# Register your models here.
