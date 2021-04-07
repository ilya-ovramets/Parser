from arekt import parser, prefir, html_lib
import requests

n = 10

i = 1

while i <= n:
    try:
        img = html_lib()
        r = requests.get(img)
        with open(f"{i}.png", "wb") as code:
            code.write(r.content)
        i += 1
    except AttributeError:
        print("УПС")
        continue


# p = requests.get(html_lib())
# out = open("...\skrin", "png")
# out.write(p.content)
# out.close()