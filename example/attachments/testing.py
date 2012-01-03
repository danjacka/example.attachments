from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class ExampleAttachments(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import example.attachments
        xmlconfig.file('configure.zcml',
                       example.attachments,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.attachments:default')

EXAMPLE_ATTACHMENTS_FIXTURE = ExampleAttachments()
EXAMPLE_ATTACHMENTS_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(EXAMPLE_ATTACHMENTS_FIXTURE, ),
                       name="ExampleAttachments:Integration")
