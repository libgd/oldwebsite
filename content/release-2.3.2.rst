LibGD 2.3.2 release AVIF & HEIF support
#######################################

:slug: release-2.3.2
:date: 2021-03-07
:author: Mike Frysinger
:category: News

The LibGD team is proud to announce the 2.3.2 release of libgd.

Fixes:

 - gif: allow decodin when both Global and Local Colormaps (`#494`_)

Added:

- avif: Support for AVIF images via libavif (`#494`_)
- heif: Support for HEIF/AVIF images via libheif (`#395`_) (`#557`_)
- webp: Drop ../deps/ search when building with cmake
- Windows: Remove unused snprintf fallback

For full list of changes, see `CHANGELOG.md`_.
 
This is a recommended update.

You can download the 2.3.1 version of GD Graphics Library from
the `libgd 2.3.1 release`_.

Check out the `full commits list`_ since the previous release.

.. _CHANGELOG.md: https://github.com/libgd/libgd/blob/gd-2.3.1/CHANGELOG.md
.. _libgd 2.3.1 release: https://github.com/libgd/libgd/releases/tag/gd-2.3.1
.. _full commits list: https://github.com/libgd/libgd/compare/gd-2.3.0...gd-2.3.1
.. _gitter: https://gitter.im/libgd/libgd
.. _#494: https://github.com/libgd/libgd/issues/494
.. _#395: https://github.com/libgd/libgd/issues/395
.. _#557: https://github.com/libgd/libgd/issues/557