import unittest2 as unittest

from zope.component import getUtility, getMultiAdapter

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from plone.portlets.constants import CONTENT_TYPE_CATEGORY
from plone.app.portlets.utils import assignment_mapping_from_key

from example.attachments.testing import\
    EXAMPLE_ATTACHMENTS_INTEGRATION_TESTING

class TestAttachmentsPortlet(unittest.TestCase):

    layer = EXAMPLE_ATTACHMENTS_INTEGRATION_TESTING

    def test_portlet_installed(self):
        portal = self.layer['portal']

        mapping = assignment_mapping_from_key(portal,
            manager_name=u"plone.rightcolumn", category=CONTENT_TYPE_CATEGORY, key="Document")

        self.assertEquals(1, len(mapping))

    def test_portlet_displays_attachments(self):
        portal = self.layer['portal']

        mapping = assignment_mapping_from_key(portal,
            manager_name=u"plone.rightcolumn", category=CONTENT_TYPE_CATEGORY, key="Document")

        setRoles(portal, TEST_USER_ID, ('Manager',))
        portal.invokeFactory('Folder', 'dinosaurs', title=u"All about dinosaurs")
        folder = portal['dinosaurs']
        folder.invokeFactory('Document', 'dinosaurs', title=u"All about dinosaurs")
        folder.invokeFactory('File', 'tyrannosaurus.pdf', title=u"Tyrannosaurus Full Report")
        folder.invokeFactory('File', 'stegosaurus.pdf', title=u"Stegosaurus Information Pack")
        document = folder['dinosaurs']
        folder.setDefaultPage('dinosaurs')
        file1 = folder['tyrannosaurus.pdf']
        file2 = folder['stegosaurus.pdf']
        file1.setExcludeFromNav(True)
        file1.reindexObject()
        file2.setExcludeFromNav(True)
        file2.reindexObject()
        setRoles(portal, TEST_USER_ID, ('Member',))

        context = document
        request = document.REQUEST
        view = document.restrictedTraverse('@@plone')
        manager = getUtility(IPortletManager, name='plone.rightcolumn', context=portal)
        assignment = mapping[u'attachments']
        renderer = getMultiAdapter((context, request, view, manager, assignment), IPortletRenderer)

        html = renderer.render()
        self.failIf('All about dinosaurs' in html)
        self.failUnless('Tyrannosaurus Full Report' in html)
        self.failUnless('Stegosaurus Information Pack' in html)
