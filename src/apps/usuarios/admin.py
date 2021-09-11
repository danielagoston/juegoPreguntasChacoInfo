from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioChangeForm

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['email', 'username', 'edad', 'is_staff', ] 
    fieldsets = UserAdmin.fieldsets + ( 
    (None, {'fields': ('edad',)}),
)


admin.site.register(Usuario, UsuarioAdmin)

add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields': ('edad',)}),
)
