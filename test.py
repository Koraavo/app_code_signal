# inputString = "foo(bar)baz(blim)"
# inputString = "foo(bar)baz(blim)"
# inputString = "foo(bar(baz))blim"

import re
bracksearch = re.compile(r'\(\w*\(?\w*\)?\)?')
matches3 = bracksearch.finditer("foo(bar(baz))blim")
for matches in matches3:
    print(matches)
