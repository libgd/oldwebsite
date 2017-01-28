LibGD 2.2.4 release
###################

:slug: release-2.2.4
:date: 2017-01-18
:author: Ondřej Surý
:category: News

LibGD team is proud to announce the 2.2.4 release of libgd.

Security related fixes:
This flaw is caused by loading data from external sources (file, custom ctx, etc) and are hard to validate before calling libgd APIs:

 - gdImageCreate() doesn't check for oversized images and as such is
   prone to DoS vulnerabilities. (CVE-2016-9317)
 - double-free in gdImageWebPtr() (CVE-2016-6912)
 - potential unsigned underflow in gd_interpolation.c (CVE-2016-10166)
 - DOS vulnerability in gdImageCreateFromGd2Ctx() (CVE-2016-10167)
 - Signed Integer Overflow gd_io.c (CVE-2016-10168)

For full list of changes, see `CHANGELOG.md`_.
 
This is a recommended update.

You can download the 2.2.4 version of GD Graphics Library from
the `libgd project`_.

Check out the `full commits list`_ since the previous release.

.. _CHANGELOG.md: https://github.com/libgd/libgd/blob/gd-2.2.4/CHANGELOG.md
.. _libgd project: https://github.com/libgd/libgd/releases/tag/gd-2.2.4
.. _full commits list: https://github.com/libgd/libgd/compare/gd-2.2.3...gd-2.2.4
.. _gitter: https://gitter.im/libgd/libgd
