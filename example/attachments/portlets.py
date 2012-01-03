from Acquisition import aq_inner
from zope.component import getMultiAdapter

from plone.memoize.instance import memoize
from plone.app.layout.navigation.interfaces import INavigationQueryBuilder
from plone.app.layout.navigation.navtree import buildFolderTree

from plone.app.portlets.portlets.navigation import NavtreeStrategy as NavigationNavtreeStrategy
from plone.app.portlets.portlets.navigation import Renderer as NavigationRenderer


class AttachmentsNavtreeStrategy(NavigationNavtreeStrategy):
    """The default navigation portlet navtree strategy, except any
    'exclude_from_nav' settings are ignored.
    """

    def nodeFilter(self, node):
        item = node['item']
        if getattr(item, 'getId', None) in self.excludedIds:
            return False
        #elif getattr(item, 'exclude_from_nav', False):
        #    return False
        else:
            return True


class AttachmentsRenderer(NavigationRenderer):
    """The default navigation portlet renderer, except always use a
    navtree strategy that ignores 'exclude_from_nav' settings.
    """

    @memoize
    def getNavTree(self, _marker=[]):
        context = aq_inner(self.context)
        queryBuilder = getMultiAdapter((context, self.data), INavigationQueryBuilder)
        strategy = AttachmentsNavtreeStrategy(context, self.data)

        return buildFolderTree(context, obj=context, query=queryBuilder(), strategy=strategy)
