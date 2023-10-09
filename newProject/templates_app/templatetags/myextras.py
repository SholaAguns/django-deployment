from django import template

register = template.Library()


def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    :param value:
    :param arg:
    :return:
    """

    return value.replace(arg, '')


# You can register filters using decorators
@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')


register.filter('cut', cut)

