LibGD 2.2.3 release
###################

:slug: release-2.2.3
:date: 2016-07-22
:author: Pierre Joye
:category: News

We welcome the 2.2.3 release around a month after 2.2.2 (we are getting consistent). Another important
milestone in the GD 2.2 series.

Security related fixes:
This flaw is caused by loading data from external sources (file, custom ctx, etc) and are hard to validate before calling libgd APIs:

 - fix php bug 72339, Integer Overflow in _gd2GetHeader (CVE-2016-5766)
 - bug #247, A read out-of-bands was found in the parsing of TGA files (CVE-2016-6132)
 - also bug #247, Buffer over-read issue when parsing crafted TGA file (CVE-2016-6214)
 - bug #248, fix Out-Of-Bounds Read in read_image_tga

Using application provided parameters, in these cases invalid data causes the issues:

 - Integer overflow error within _gdContributionsAlloc() (CVE-2016-6207)
 - fix php bug 72494, invalid color index not handled, can lead to crash (CVE-2016-6128)
 - improve color check for CropThreshold


Important update:

 - gdImageCopyResampled has been improved. Better handling of images with alpha channel, also brings libgd in sync with php's bundled gd.
 
This is a recommended update.

On a sidenote, we have now a gitter channel if you have any questions or like to discuss with us,
`gitter`_, in addition to our "#libgd" freenode channel.


You can download the 2.2.3 version of GD Graphics Library from
the `libgd project`_.

Check out the `full commits list`_ since the previous release.

.. _libgd project: https://github.com/libgd/libgd/releases/tag/gd-2.2.3
.. _full commits list: https://github.com/libgd/libgd/compare/gd-2.2.2...gd-2.2.3
.. _gitter: https://gitter.im/libgd/libgd
