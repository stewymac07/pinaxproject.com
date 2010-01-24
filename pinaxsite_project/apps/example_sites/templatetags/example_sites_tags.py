from django import template

from example_sites.models import Site

from pinaxsite_project.utils import AsNode



register = template.Library()



class FeaturedSiteNode(AsNode):
    
    def render(self, context):
        try:
            site = Site.objects.filter(approved=True).get(featured=True)
        except Site.DoesNotExist:
            site = None
        context[self.context_var] = site
        return u""


@register.tag
def featured_site(parser, token):
    return FeaturedSiteNode.handle_token(parser, token)
