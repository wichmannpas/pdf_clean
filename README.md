PDF clean
=========

clean
-----

clean.py removes all pages of a pdf document which are followed by a page containing the same text. This is especially useful for removing redundant slides from pdf presentations, i.e. those produced by LaTeX beamer.


Usage
-----

To clean a PDF document:

    ./clean.py example.pdf example_cleaned.pdf

To get all available parameters, use:

    ./clean.py --help
