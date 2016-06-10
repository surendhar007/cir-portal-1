from django.contrib import admin
from registration.models import *

class UserAdmin(admin.ModelAdmin):
    pass
search_fields = ('first_name', 'last_name', 'email')
list_display = ('first_name', 'last_name', 'email')
admin.site.register(User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class TestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Test, TestAdmin)

class TechnicalTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(TechnicalTest, TechnicalTestAdmin)

class HRTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(HRTest, HRTestAdmin)

class QuantatitiveTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(QuantatitiveTest, QuantatitiveTestAdmin)

class VerbalTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(VerbalTest, VerbalTestAdmin)

class ReasoningTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(ReasoningTest, ReasoningTestAdmin)

class EligibilityTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(EligibilityTest,  EligibilityTestAdmin)

class AptitudeTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(AptitudeTest,  AptitudeTestAdmin)




