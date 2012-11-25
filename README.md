impress-code-highlighter
========================

A simple tool to highlight source code blocks in LibreOffice Impress.

## How to test it
 1. Start libreoffice in server mode: `soffice "--accept=socket,host=localhost,port=2002;urp;" tests/teste1.odp`
 2. Create a textbox in your presentation and put the code you want to be highlighted inside. Create a custom style named `code` and apply it to your code box.
 3. Run `highlight.py`