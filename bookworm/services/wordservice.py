import PyICU
# $x is variable x
# @x is attribute x

def word_tokenize(txt):
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(txt)
    lastPos = bd.first()
    words = []
    while (lastPos < len(txt)):
        currentPos = bd.next()
        words.append(txt[lastPos:currentPos])
        print txt[lastPos:currentPos]
        lastPos = currentPos
    return words


def get_word_type(txts=[]):
    base = ['$n', '$v', '$a-n', '$a-v', '$cj', '$uk']
