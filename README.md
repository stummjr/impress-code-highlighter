impress-code-highlighter
========================

A python macro for source code highlighting in LibreOffice Impress.

## How to test it
 1. Start libreoffice in server mode: `soffice "--accept=socket,host=localhost,port=2002;urp;" tests/teste1.odp`
 2. Run `highlight.py`


## How to use it
By now, there are two ways to use the code highlighter:
 1. Starting libreoffice in server mode
 2. Adding `highlight.py` as a macro

In order to highlight your source code in your impress presentation, you should create a custom style named `code-<language name>` and apply it to all the text boxes you'd want to highlight. Then, you should run `highlight.py` either in an OS shell or as a macro inside Impress.

For example, to highlight some Python code blocks, you have to apply a style named `code-python` to the code block and then run the macro.


## Dependencies
This script depends on the `pygments` module for Python 3.

Debian-based OS users must install the package `libreoffice-script-provider-python` to be able to get LibreOffice working with Python macros.

## Disclaimer
This script is based on http://code.activestate.com/recipes/576796-python-syntax-highlighting-in-openoffice-impress/
