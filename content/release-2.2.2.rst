LibGD 2.2.2 release
###################

:slug: release-2.2.2
:date: 2016-06-25
:author: Pierre Joye
:category: News

Exactly a month after 2.2.1 we welcome the 2.2.2 release. An important
milestone in the GD 2.2 series.

Security related fixes:

 - Integer Overflow in gdImagePaletteToTrueColor() resulting in heap overflow (CVE-2016-5767)
 - #215 Stack overflow with gdImageFillToBorder (CVE-2015-8874, CVE-2016-9933)
 - NULL Pointer Dereference at _gdScaleVert

We also like to mention to consider the GD and GD2 image formats only for development or testing
purposes. We do plan to deprecate it in GD 2.3 and remove it in GD 3.0. Its existence is not justified
anymore as other formats provide lossless storage for both palette and truecolor images in a much more 
efficient way.

Numerous other fixes have been applied. The scale and rotation functions have been greatly improved as well.

This is a recommended update.

You can download the 2.2.2 version of GD Graphics Library from
the `libgd project`_.

Check out the `full commits list`_ since the previous release.

.. _libgd project: https://github.com/libgd/libgd/releases/tag/gd-2.2.2
.. _full commits list: https://github.com/libgd/libgd/compare/gd-2.2.1...gd-2.2.2
