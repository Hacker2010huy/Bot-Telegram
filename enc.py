import os,random,base64

def number_enc():
    return random.randint(1000, 1000000)
def ran_space():
    return " " * random.randint(25, 500)
def ran_text():
    kytu = list("~`|â€¢âˆšÏ€Ã·Ã—Â§âˆ†Â£â‚¬$Â¢^Â°={}\\%Â©Â®â„¢âœ“[]@#â‚«_&-+()/*:;!?ðŸ”´ðŸŸ ðŸŸ¡ðŸŸ¢ðŸ”µðŸŸ£ðŸŸ¤âš«âšª")
    return random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu) + random.choice(kytu)

def pyThon(code, namefile):
    encode = []
    code = code
    code = code.split("\n")
    for c in code:
        if c.replace(" ", "") != "":
            if c.strip().startswith("#"):
                continue
            if c.startswith(" "):
                c = "                                                            " + c
            c = c + f"{ran_space()}#{number_enc()}ENCODE BY PHAN QUOC HUY DEPTRY\n#{ran_space()}{ran_text()}"
            encode.append(c)
    encode = "\n".join(encode)
    encode = base64.b64encode("\n".join(encode).encode("utf-8"))
    with open(f"{namefile}", "w", encoding="utf-8") as fi:
        fi.write(f"import base64\nexec(base64.b64decode({encode}).decode('utf-8'))")
