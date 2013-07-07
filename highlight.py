# Author: stummjr - <stummjr at gmail>
# License: MIT
from pygments import styles
from pygments.lexers import (get_lexer_by_name)


def highlight_source_code():
    ctx = XSCRIPTCONTEXT
    doc = ctx.getDocument()
    highlight_all(doc)


def rgb(r, g, b):
    return (r & 255) << 16 | (g & 255) << 8 | (b & 255)


def to_rgbint(hex_str):
    if hex_str:
        r = int(hex_str[:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:], 16)
        return rgb(r, g, b)
    return rgb(0, 0, 0)


def highlight_code(styleName, codebox):
    lang = styleName.replace("code-", "")
    lexer = get_lexer_by_name(lang)
    cursor = codebox.createTextCursor()
    style = styles.get_style_by_name('default')
    cursor.gotoStart(False)
    for tok_type, tok_value in lexer.get_tokens(codebox.String):
        cursor.goRight(len(tok_value), True)  # selects the token's text
        cursor.CharColor = to_rgbint(style.style_for_token(tok_type)['color'])
        cursor.goRight(0, False)  # deselects the selected text


def highlight_all(doc):
    styles = doc.StyleFamilies.getByName(u'graphics')
    code = styles.getByName(u'code')
    pages = doc.DrawPages
    for idx in xrange(pages.getCount()):
        page = pages.getByIndex(idx)
        for item_idx in xrange(page.getCount()):
            box = page.getByIndex(item_idx)
            if 'com.sun.star.drawing.TextShape' in box.SupportedServiceNames:
                if box.Style.getName().find("code-") == 0:
                    highlight_code(box.Style.getName(), box)


def remote_get_doc():
    import uno
    localContext = uno.getComponentContext()
    resolver = localContext.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", localContext)
    ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    doc = desktop.getCurrentComponent()
    return doc


g_exportedScripts = (highlight_source_code,)
if __name__ == "__main__":
    doc = remote_get_doc()
    highlight_all(doc)
