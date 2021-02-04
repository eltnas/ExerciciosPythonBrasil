num = 500
primeiro=1
segundo=1

if (num==1) or (num==2):
    print("1")
else:
    for c in range(2,num):
        termo = primeiro + segundo
        segundo = primeiro
        primeiro = termo
        c += 1
    print(termo)
