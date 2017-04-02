from django import template

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.is_superuser or user.groups.filter(name=group_name).exists()

@register.filter(name='full_or_username')
def full_or_username(user):
    return user.first_name + ' ' + user.last_name if user.first_name != '' and user.last_name != '' else user.username