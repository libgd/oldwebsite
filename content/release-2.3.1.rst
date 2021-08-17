LibGD 2.3.1 release
###################

:slug: release-2.3.1
:date: 2021-01-30
:author: Willson-chen
:category: News

The LibGD team is proud to announce the 2.3.1 release of libgd.

Fixes:

 - Fix potential integer overflow detected by oss-fuzz
 - Fix `#615`_ using libraqm
 - Fix `#303`_: gdlib.pc: use Requires instead of Libs
 - Using uninitialized variables. (CVE-2019-11038)
 - Heap-based buffer overflow. (CVE-2019-6977)
 - Double-free in gdImage*Ptr(). (CVE-2019-6978)

For full list of changes, see `CHANGELOG.md`_.
 
This is a recommended update.

You can download the 2.3.1 version of GD Graphics Library from
the `libgd 2.3.1 release`_.

Check out the `full commits list`_ since the previous release.

.. _CHANGELOG.md: https://github.com/libgd/libgd/blob/gd-2.3.1/CHANGELOG.md
.. _libgd 2.3.1 release: https://github.com/libgd/libgd/releases/tag/gd-2.3.1
.. _full commits list: https://github.com/libgd/libgd/compare/gd-2.3.0...gd-2.3.1
.. _gitter: https://gitter.im/libgd/libgd
.. _#615: https://github.com/libgd/libgd/issues/615
.. _#303: https://github.com/libgd/libgd/issues/303