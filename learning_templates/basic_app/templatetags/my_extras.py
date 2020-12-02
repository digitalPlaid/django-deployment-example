# include the __init__.py file in the same folder so you can treat this like a module
from django import template

register = template.Library()

# you can create your own filters here
# use decorators to register, instead of using register.filter('what_you_want_to_call_your_filter, actual_filter_function_name)
@register.filter(name='cut')
def cut(value, arg):
    # value is from your context dictionary
    # arg is for additional arguments
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

    # remember to register it!
#register.filter('cut', cut) # the argument is what you want to call hte filter in the template tags
# you can also do it with decorators which is cleaner
