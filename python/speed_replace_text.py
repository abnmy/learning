import re
from itertools import product

ITERATION = 100
STMT_TMPL = "$f()"

TEXT_TO_REPLACE = "This is a sentence to delete."
PATTERN = re.compile(TEXT_TO_REPLACE)

TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque id suscipit lectus. Suspendisse ornare molestie nulla sit amet fringilla. Phasellus sit amet pharetra magna. Aenean lectus urna, feugiat at ex et, dignissim tempor justo. Curabitur accumsan convallis lectus, vitae tempus tellus euismod a. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed commodo tempus magna ac semper. Nulla tortor lacus, fermentum blandit velit ut, dignissim venenatis diam. Fusce in leo ante. Quisque at maximus magna. Integer ut placerat ipsum. Donec ultrices justo sem, at varius nibh porta nec. Proin bibendum tempor ante, vitae tincidunt nulla ornare eu.
Vestibulum ac pretium ipsum, eget mollis lorem. Integer sed nulla ullamcorper, placerat dui eu, viverra metus. Praesent eget odio a libero lobortis interdum. Nullam posuere quam et massa placerat scelerisque. Suspendisse luctus dolor in quam pellentesque dapibus. Vivamus id malesuada turpis, ullamcorper tempor magna. Vivamus nisi metus, molestie nec dignissim nec, finibus cursus urna. Sed sagittis venenatis sapien sed fermentum. Phasellus maximus dapibus nulla, ut maximus odio vehicula nec. Integer quis pharetra nunc, in feugiat metus. Proin non sagittis nisi. Sed odio ipsum, consequat vel volutpat eget, laoreet nec neque. Maecenas ullamcorper rhoncus vestibulum. Vivamus ultrices leo maximus, sollicitudin ipsum vitae, semper metus. Suspendisse vitae tortor ornare, commodo mi imperdiet, tincidunt nisl.
Vivamus id condimentum diam, et facilisis velit. Integer iaculis, lacus at consequat egestas, ipsum sapien fermentum velit, quis commodo turpis ante pharetra sapien. Pellentesque mollis vehicula venenatis. Vestibulum ligula ex, porta nec neque in, elementum suscipit lectus. Fusce auctor turpis scelerisque nulla tristique, eget commodo ligula tristique. Nulla facilisi. Sed lobortis, augue non semper pulvinar, lectus dolor accumsan ligula, at mattis sapien augue vel orci. Nunc consectetur fringilla nunc sed facilisis. Nam hendrerit, mauris id maximus cursus, diam nisl aliquet quam, et auctor dui felis eu est. Donec ut eros pulvinar, aliquet libero commodo, suscipit ante. Proin sapien augue, egestas at gravida ut, sollicitudin vitae leo. Praesent vel tortor porttitor turpis consectetur iaculis at efficitur metus. Sed aliquet aliquet justo a egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean ut nulla vitae magna dignissim tincidunt sit amet quis velit."""

RANDOM_TEXT = TEXT_TO_REPLACE+TEXT*1000

def f1():
    _ = RANDOM_TEXT.replace(TEXT_TO_REPLACE, "")
    
def f1b():
    _ = RANDOM_TEXT.replace(TEXT_TO_REPLACE, "", 1)

def f2():
    _ = re.sub(TEXT_TO_REPLACE, "", RANDOM_TEXT)

def f2b():
    _ = re.sub(TEXT_TO_REPLACE, "", RANDOM_TEXT, 1)

def f3():
    _ = PATTERN.sub("", RANDOM_TEXT)

def f3b():
    _ = PATTERN.sub("", RANDOM_TEXT, 1)
