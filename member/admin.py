from django.contrib import admin
from member.helper import form_helper
from member.models import Member, Country
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name']


@admin.register(Member)
class MemberAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = form_helper.MemberChangeForm
    add_form = form_helper.MemberCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'first_name', 'last_name', 'last_login']
    list_filter = ['country', 'is_active']

    fieldsets = (
        ['Authentication', {'fields': ['email', 'password']}],
        ['Personal info', {'fields': ['first_name', 'last_name', 'country']}],
        ['Permissions', {'fields': ['is_active', ]}],
        [None, {'fields': ['last_login']}]
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ['wide'],
            'fields': ['email', 'first_name', 'last_name', 'password1', 'password2'],
        }),
    )
    search_fields = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']
    filter_horizontal = ()


admin.site.unregister(Group)
