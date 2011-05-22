from django.core.urlresolvers import reverse
from django import template


register = template.Library()


@register.simple_tag
def edit_link(obj=''):
    try:
        url = reverse('admin:%s_%s_change' %
        (obj._meta.app_label, obj._meta.module_name),  args=[obj.id])
        return u'<a href="%s">Edit (%s)</a>' % (url,
                                              obj.__unicode__())
    except:
        return ''
