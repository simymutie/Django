from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, FormView


class CompletedPage(TemplateView):
    template_name = "contact_form/contact_sent.html"


class ContactFormMixin(object):
    """
    Form view that sends email when form is valid. You'll need
    to define your own form_class and template_name.
    """
    def form_valid(self, form):
        form.send_email(self.request)
        return super(ContactFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse("completed")


class ContactFormView(ContactFormMixin, FormView):
    pass


class ContactModelFormView(ContactFormMixin, CreateView):
    pass
