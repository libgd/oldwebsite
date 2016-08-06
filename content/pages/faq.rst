Frequently Asked Questions
##########################

:date: 2013-04-09
:title: Frequently Asked Questions
:slug: faq
:author: Ondřej Surý

What does "gd" stand for?
=========================

In gd 1.0, it stood for "gif draw." After the Unisys patent on the LZW
compression used in GIF came to light and GIF support was dropped, it
did not officially stand for anything, but let's just say "graphics
draw" and leave it at that. (GIF support is back, thanks to the
expiration of the patent, but gd can draw much more than GIFs.)


Does gd support GIF images?
===========================

Yes. Support for GIF was restored in gd 2.0.28 on July 21st,
2004. Support for creating GIF animations is also available. Note that
gdlib-config --features can be used to list the image formats
supported by gd. Versions of gdlib-config prior to recent updates do
not support the --features option, which can be understood to mean
that GIF is not available.


How do I install gd on Linux?
=============================

Well, what do you really want?

If you want gd for a PHP application, just do (for Fedora):

.. code-block:: shell

    yum install php-gd

Or, for Red Hat Enterprise Linux or CentOS:

.. code-block:: shell

    up2date php-gd

Then do:

.. code-block:: shell

    service httpd restart

If your system is Debian based (Debian/Ubuntu/...) then you need to install `php5-gd` package:

.. code-block:: shell

    apt-get install php5-gd

Other Linux distributions may have gd already compiled into PHP, or
they may have a similar php-gd package that brings in PHP's gd
module. PHP includes its own distribution of gd, you do not need mine.

If you really want gd for C programming or some other language that
has an extension built on top of my distribution of gd, do:

.. code-block:: shell

    yum install gd-devel

or on Debian based systems do:

.. code-block:: shell

    apt-get install libgd2-xpm-dev

Or the equivalent for your Linux distribution.

Note: this might not install the latest, most-cutting edge version of
gd, depending on the Linux distribution you are running and how
current their gd packages are at the moment.

How do I load an image file from a buffer in memory?
====================================================

The following C code shows how to load an entire image file into a
buffer in memory, then ask gd to read the image from that
buffer. Please note that since you are responsible for allocating the
buffer, You are also responsible for freeing the buffer with your
normal memory management functions.

Of course, there is a gdImageCreateFromJpegPtr function available as
well.  This particular example loads a PNG image.

.. code-block:: C

    #include <sys/types.h>
    #include <sys/stat.h>
    #include <stdlib.h>
    
    gdImagePtr myLoadPng(char *filename)
    {
      FILE *in;
      struct stat stat_buf;
      gdImagePtr im;
      in = fopen("myimage.png", "rb");
      if (!in) {
        /* Error */
      }
      if (fstat(fileno(in), &stat_buf) != 0) {
        /* Error */
      }
      /* Read the entire thing into a buffer 
        that we allocate */
      char *buffer = malloc(stat_buf.st_size);
      if (!buffer) {
        /* Error */
      }
      if (fread(buffer, 1, stat_buf.st_size, in) 
        != stat_buf.st_size) 
      {
        /* Error */
      }
      im = gdImageCreateFromPngPtr(
        stat_buf.st_size, buffer);
      /* WE allocated the memory, WE free 
        it with our normal free function */
      free(buffer);
      fclose(in);
      return im;
    } 


How do I save an image to a buffer in memory?
=============================================

The following C code shows how to save a gd image to a memory buffer,
and then write that buffer to a file on disk. You could also write it
directly to stdout, preceded by a Content-type: image/png header and
two CR/LF sequences, to directly return an image from a CGI program.

For your convenience, gd allocates the buffer for you; when you are
done with it, you must call gdFree to release it.

Of course, there is a gdImageJpegPtr function available as well.  This
particular example saves a PNG image.

.. code-block:: C

    #include <sys/types.h>
    #include <sys/stat.h>
    #include <stdlib.h>
    
    void mySavePng(char *filename, 
      gdImagePtr im)
    {
      FILE *out;
      int size;
      char *data;
      out = fopen("filename, "wb");
      if (!out) {
        /* Error */
      }
      data = (char *) gdImagePngPtr(im, &size);
      if (!data) {
        /* Error */
      }
      if (fwrite(data, 1, size, out) != size) {
        /* Error */
      }
      if (fclose(out) != 0) {
        /* Error */
      }
      gdFree(data);  
    }

Why doesn't my gd 1.x program work well with gd 2.x?
====================================================

There are two common reasons:

1. You were using an ancient version of gd 1.x with GIF support, and now you are using a not-quite-new-enough version of gd 2.x without GIF support. Solution: get the latest gd 2.x which again supports GIF.

2. You are trying to make thumbnails, or otherwise copy photographic-quality images like JPEG files. But you are creating the new image with gdImageCreate, which makes a palette-color image not suitable for photographs. Solution: use gdImageCreateTrueColor (new in gd 2.x), which creates a true-color image. This sort of "worked" in gd 1.x because gd 1.x did a quick and nasty job of converting JPEGs to palette color when reading them. But you will get much better results doing it the right way in gd 2.x. If you really want to, you can reduce to palette color after the copy using gdImageTrueColorToPalette.

Why does gd cause my PHP script to run out of memory?
=====================================================

Most often, the problem is that the memory_limit parameter in php.ini
is set to something very conservative, like 8M (eight
megabytes). Increase that setting and restart the web server.  Of
course, opening truly huge images can cause real memory problems, if
several are open at once. 8,000 pixels times 8,000 pixels times four
bytes for truecolor equals a walloping 256 megabytes.

How can I determine the image dimensions without loading the entire image into memory (and possibly running out)?
=================================================================================================================

Very large images can cause gd to run out of memory (see the previous
question). And sometimes the image file itself isn't terribly large—
consider a JPEG of a completely blank field, 8,000 pixels on a side:
the file compresses well but representing it in memory as a bitmap is
impractical.  If you are coding in PHP, you can check for this
situation with the getimagesize function, which determines the image
dimensions without using gd. This is possible because the popular
image formats all store the image dimensions near the beginning of the
file where they are easily accessible. Perl programmers can use the
similar Image::Size CPAN module. If you are not using PHP or Perl and
your language of choice does not offer a similar feature, you can
implement the technique yourself. See the GIF specification, the JPEG
specification, and the PNG specification.
