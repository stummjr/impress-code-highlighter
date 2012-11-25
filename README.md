impress-code-highlighter
========================

A simple tool for source code blocks highlighting in LibreOffice Impress.

## How to test it
 1. Start libreoffice in server mode: `soffice "--accept=socket,host=localhost,port=2002;urp;" tests/teste1.odp`
 2. Run `highlight.py`


## How to use it
By now, are two ways to use the code highlighter:
 1. Start libreoffice in server mode
 2. Add `highlight.py` as a macro

In order to highlight the source code that you want to show in your impress presentation, you have to create a custom style named `code` and apply it to all the text boxes you want to highlight. Then, you should run `highlight.py` either in a OS shell or as a macro.


## Disclaimer
This script been has started as a "fork" from http://code.activestate.com/recipes/576796-python-syntax-highlighting-in-openoffice-impress/