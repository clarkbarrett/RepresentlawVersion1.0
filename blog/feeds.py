from django.contrib.syndication.views import Feed
# from django.urls import reverse
from django.core.urlresolvers import reverse
from .models import Post
from django.utils.feedgenerator import Atom1Feed


class RSSSiteNewsFeed(Feed):
    title = "Represent News Feed"
    link = "https://representlaw.com/blog/rss/"
    description = "Latest Represent posts and news."
    # description_template = 'blog/feed_template.html'

    def items(self):
        # return Post.objects.order_by('-published')[:100]
        return Post.objects.all().order_by('-published')[:100]

    def item_title(self, obj):
        return obj.title

    def item_description(self, obj):
        return obj.seo_description

    def item_link(self, obj):
        return "https://www.representlaw.com/blog/rss/%s" % obj.slug

    # item_link is only needed if NewsItem has no get_absolute_url method.
    """def item_link(self, item):
        return reverse('news-item', args=[item.pk])"""

    def get_context_data(self, **kwargs):
        context = super(RSSSiteNewsFeed, self).get_context_data(**kwargs)
        context['post'] = 'posts'
        return context


class AtomSiteNewsFeed(RSSSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RSSSiteNewsFeed.description
