.. Agoraplex Annotations documentation master file, created by
   sphinx-quickstart2 on Fri Jan 11 10:39:10 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _index:

==============================================
 `anodi`: The `Agoraplex` Annotations Toolkit
==============================================

`anodi` [#etymology]_ is a decorater-based backport of :pep:`3107`,
function annotations, to Python 2.7, along with a limited set of
:mod:`~anodi.tools` based on those annotations (e.g.,
:func:`~anodi.tools.document`, which hoists annotations into the
docstring, for the `Sphinx`__ `autodoc`__ extension to find).

`anodi` is licensed under the BSD "3-clause" license. See
:doc:`LICENSE` for details.

.. __: http://sphinx-doc.org/
.. __: http://sphinx-doc.org/ext/autodoc.html


.. _motivation:

Motivation and applications
---------------------------

**TODO:** something goes here.


.. _html_api_documentation:

API Documentation
=================

Documentation for every :mod:`~anodi` API.

.. toctree::
   :maxdepth: 2

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Footnotes
=========

.. [#etymology]

   **Etymology:** The Welsh for `annotation` is `anodi` (according to
   `Google Translate`__). It won out over translations to other
   languages, because it's short, and phonetically (and, thus,
   mnemonically), related. It's also a tribute to my friend, `Allen
   Briggs`__, who passed away, unexpectedly, in March of 2012. Allen
   was an amateur student of Welsh, when he wasn't busy `maintaining
   the mac68k port of NetBSD`__, or, as a consequence of his \*BSD
   work, being `credited in iOS`__.

.. __: http://translate.google.com/#en/cy/annotation
.. __: http://www.legacy.com/obituaries/roanoke/obituary.aspx?n=allen-kenneth-briggs&pid=156377986
.. __: http://www.netbsd.org/ports/mac68k/history.html
.. __: http://blogs.roanoke.com/theburgs/news/2012/03/11/brigss-work-can-be-found-on-an-iphone/


.. add misc docs to a hidden toc to avoid warnings (a trick borrowed
   from Pyramid docs)

.. toctree::
   :hidden:

   LICENSE
   README
