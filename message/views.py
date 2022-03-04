from django.views.generic import TemplateView


class MessageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        if 'message' in self.request.GET and 'name' in self.request.GET:
            message, name = self.request.GET['message'], self.request.GET['name']

            return {'message': message, 'name': name}


