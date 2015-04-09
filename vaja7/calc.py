x = float(raw_input("Vstavi prvo stevilko"))
y = float(raw_input("Vstavi drugo stevilko"))
znak = float(raw_input("za sestevanje vpisi 1, za odstevanje vpisi 2, za mnozenje vpisi 3, za deljenje vpisi 4"))


if znak == 1:
    print (x + y)
elif znak == 2:
    print (x - y)
elif znak == 3:
    print (x * y)
elif znak == 4:
    print (x / y)
else:
    print("Napaka")


