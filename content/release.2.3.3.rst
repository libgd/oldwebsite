LibGD 2.3.3 Bugs fixes, improved MacOs, Windows builds support
##############################################################

:slug: release-2.3.3
:date: 2021-09-12
:author: Pierre Joye
:category: News

The LibGD team is proud to announce the 2.3.3 release of libgd. This release brings a few fixes 
as well as improved compilations and builds on all platforms. On Windows, vcpkg to install libGd
dependencies is now well supported.

In the process, we also added CI using github actions for Linux (x64, arm64/neon, gcc and clan), Windows 
(x64, arm64, vc and mingw). We are looking for more supported platforms to add to our CI (BSD, all 
architures, PowerPC, RiscV etc). If you have such systems and willing to let us run  run the github actions 
CI on it, please let us know, it will be much appreciated.

Fixes:

- `#759`_ update cmake to generate config.h in the build dir
- `#756`_ 2.3.3 release
- `#750`_ gdPutBuf return value check
- `#729`_ HEIF builds fail with latest distros
- `#678`_ segfault in heif tests due to missing label.heic
- `#677`_ Test failure avif/compare_avif_to_png with libavif-0.8.2
- `#661`_ imagecopyresampled() produce artifacts on transparent PNG
- `#611`_ Fixes to build v2.3.0 on Windows with MinGW-w64
- `#415`_ optimize option in gif animation causes segfault
- `#331`_ _gdContributionsCalc() always uses DEFAULT_BOX_RADIUS (gdImageScale internal sub method)
- `#320`_ gdImageRotateInterpolated() converts the source image to truecolor
- `#249`_ CMake and Makefiles build broken on Windows
- `#93`_ gdImageScaleTwoPass() looses top row and left column


For full list of changes, see `CHANGELOG.md`_.
 
This is a recommended update.

You can download the 2.3.3 version of GD Graphics Library from
the `libgd 2.3.3 release`_.

Check out the `full commits list`_ since the previous release.

.. _CHANGELOG.md: https://github.com/libgd/libgd/blob/gd-2.3.3/CHANGELOG.md
.. _libgd 2.3.3 release: https://github.com/libgd/libgd/releases/tag/gd-2.3.3
.. _full commits list: https://github.com/libgd/libgd/compare/gd-2.3.2...gd-2.3.3
.. _gitter: https://gitter.im/libgd/libgd
.. _#759: https://github.com/libgd/libgd/issues/759  update cmake to generate config.h in the build dir
.. _#756: https://github.com/libgd/libgd/issues/756  2.3.3 release
.. _#750: https://github.com/libgd/libgd/issues/750  gdPutBuf return value check
.. _#729: https://github.com/libgd/libgd/issues/729  HEIF builds fail with latest distros
.. _#678: https://github.com/libgd/libgd/issues/678  segfault in heif tests due to missing label.heic
.. _#677: https://github.com/libgd/libgd/issues/677  Test failure avif/compare_avif_to_png with libavif-0.8.2
.. _#661: https://github.com/libgd/libgd/issues/661  imagecopyresampled() produce artifacts on transparent PNG
.. _#611: https://github.com/libgd/libgd/issues/611  Fixes to build v2.3.0 on Windows with MinGW-w64
.. _#415: https://github.com/libgd/libgd/issues/415  optimize option in gif animation causes segfault
.. _#331: https://github.com/libgd/libgd/issues/331  _gdContributionsCalc() always uses DEFAULT_BOX_RADIUS
.. _#320: https://github.com/libgd/libgd/issues/320  gdImageRotateInterpolated() converts the source image to truecolor
.. _#249: https://github.com/libgd/libgd/issues/249  CMake and Makefiles build broken on Windows
.. _#93: https://github.com/libgd/libgd/issues/93   gdImageScaleTwoPass() looses top row and left column