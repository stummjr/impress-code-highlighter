impress-code-highlighter
========================

A python macro for source code highlighting in LibreOffice Impress.

## How to test it
 1. Start libreoffice in server mode: `soffice "--accept=socket,host=localhost,port=2002;urp;" tests/teste1.odp`
 2. Run `highlight.py`


## How to use it
By now, are two ways to use the code highlighter:
 1. Start libreoffice in server mode
 2. Add `highlight.py` as a macro

In order to highlight the source code that you want to show in your impress presentation, you have to create a custom style named `code-<language name>` and apply it to all the text boxes you want to highlight. Then, you should run `highlight.py` either in a OS shell or as a macro. For example, to highlight some Python code, you have to apply a style named `code-python` to the code block and then run the macro.

## Dependencies
This script depends on the `pygments` module for Python 3.

## Disclaimer
This script is based on http://code.activestate.com/recipes/576796-python-syntax-highlighting-in-openoffice-impress/
