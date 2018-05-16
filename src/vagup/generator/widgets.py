from django.forms import widgets
from django.utils.safestring import mark_safe


class DefaultTextFieldWidget(widgets.TextInput):
    def render(self, name, value, attrs=None):
        return mark_safe(u'''<div class="col-6" style="border-radius: 25px;">%s</div>''' % (super(DefaultTextFieldWidget, self).render(name, value, attrs)))
