from django import template

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.is_superuser or user.groups.objects.filter(name=group_name).exists()