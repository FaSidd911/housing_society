from django import template

register = template.Library()

@register.filter(is_safe=True)
def label_with_classes(field, css):
    return field.label_tag(attrs={'class': css})

@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)