def slownie(kwota):
    k=[i for i in str(kwota)]
    jedn={'1':'jeden','2':'dwa','3':'trzy','4':'cztery','5':'pięć','6':'sześć','7':'siedem','8':'osiem','9':'dziewięć'}
    nas={'1':'jedenaście','2':'dwanaście','3':'trzynaście','4':'cztarenaście','5':'piętnaście','6':'szesnaście','7':'siedemnaście','8':'osiemnaście','9':'dzewiętnaście','0':'dziesięć'}
    dzie={'2':'dwadzieścia','3':'trzydzieści','4':'czterdzieści','5':'pięćdziesiąt','6':'sześćdziesiąt','7':'siedemdziesiąt','8':'osiemdziesiąt','9':'dziewięćdziesiąt'}
    set={'1':'sto','2':'dwieście','3':'trzysta','4':'czterysta','5':'pięćset','6':'sześćset','7':'siedemset','8':'osiemset','9':'dziewięćset'}
    tys={'1':'tysiąc','2':'dwa tysiące','3':'trzy tysiące','4':'cztery tysiące','5':'pięć tysięcy','6':'sześć tysięcy','7':'siedem tysięcy','8':'osiem tysięcy','9':'dziewięć tysięcy'}

    if len (k)>1 and k[-2]=='1':
        if k[-1] in nas:
            k[-1]=nas[k[-1]]
            k[-2]='x'
    else:
        if k[-1] in jedn:
            k[-1]=jedn[k[-1]]
        if k[-2] in dzie:
            k[-2]=dzie[k[-2]]
    if len(k)>2:
        if k[-3] in set:
            k[-3]=set[k[-3]]
    #==================tysiące====================================================
    if len (k)>4 and k[-5]=='1':
        if k[-4] in nas:
            k[-4]=nas[k[-4]]+' tysięcy'
            k[-5]='x'
    else:

        if len (k)>4 and k[-5] in dzie:
            k[-5]=dzie[k[-5]]

    if len(k)>3:
        if k[-4] in tys:
            k[-4]=tys[k[-4]]
    #==================dziesiątki tysięcy========================================
    if len(k)>4:
        if k[-5] in dzie:
            k[-5]=dzie[k[-5]]
        if k[-4]=='tysiąc':
            k[-4]='jeden tysięcy'
    #==============setki tysięcy=================================================
    if len(k)>5:
        if k[-6] in set:
            k[-6]=set[k[-6]]






    r=[]
    for i in range(len(k)):
        if k[i]!='x' and k[i]!='0':
            r.append(k[i])
    l=''
    if k[len(k)-1]=='dwa' or k[len(k)-1]=='trzy':
        l=' złote'
    else:
        l=' złotych'

    print(k)
    r=' '.join(r)
    return r + l


print(slownie(78963))
