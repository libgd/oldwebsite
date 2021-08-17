LibGD 2.3.0 release
###################

:slug: release-2.3.0
:date: 2020-03-22
:author: Willson-chen
:category: News

The LibGD team is proud to announce the 2.3.0 release of libgd.

Security related fixes:

 - Double-free vulnerability in gdImageBmpPtr. (CVE-2018-1000222)
 - Null pointer reference at gdImageClone. (CVE-2018-14553)
 - Integer signedness error. (CVE-2018-5711)
 - Using uninitialized variables. (CVE-2019-11038)
 - Heap-based buffer overflow. (CVE-2019-6977)
 - Double-free in gdImage*Ptr(). (CVE-2019-6978)

For full list of changes, see `CHANGELOG.md`_.
 
This is a recommended update.

You can download the 2.3.0 version of GD Graphics Library from
the `libgd 2.3.0 release`_.

Check out the `full commits list`_ since the previous release.

.. _CHANGELOG.md: https://github.com/libgd/libgd/blob/gd-2.3.0/CHANGELOG.md
.. _libgd 2.3.0 release: https://github.com/libgd/libgd/releases/tag/gd-2.3.0
.. _full commits list: https://github.com/libgd/libgd/compare/gd-2.2.5...gd-2.3.0
.. _gitter: https://gitter.im/libgd/libgd
