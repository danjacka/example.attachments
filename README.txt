===========================================================
An example technique for modeling page attachments in Plone
===========================================================

This package demonstrates a simple way to have Files appear as
'attachments' to your Plone page.

The code and tests are not expected to be installed as is (though you
can if you like). More likely you'll incorporate them into your own
site policy if the technique works for you.

See http://www.treebrolly.com/blog/attachments-now-for-the-future for
more info.

What example.attachments does
-----------------------------

1. Adds a content type navigation portlet for Document types. The portlet
will be added to the right-hand column for every new Document.

2. Overrides the new portlet's renderer so that any 'exclude_from_nav'
settings on items in the portlet's context are ignored - items are
always shown.

How to create a Page with attachments
-------------------------------------

Steps to create an example Page:

1. Add a new Folder titled 'All about dinosaurs'. Publish it.
2. Inside that Folder, add a Page also titled 'All about
dinosaurs'. Publish it.
3. In the Folder's ``Display`` menu, set the Page as the default item
in that Folder.
4. Add a couple of Files to the Folder, e.g. tyrannosaurus.pdf and
stegosaurus.pdf. In their settings, exclude them from navigation so
that they don't show up in the left hand navigation.

Done!
