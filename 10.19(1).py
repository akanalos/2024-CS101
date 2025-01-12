x=int(input())
calendar1={'pop':1,'no':2,'zip':3,'zotz':4,'tzec':5,'xul':6,'yoxkin':7,'mol':8,'chen':9,'yax':10,
     'zac':11,'ceh':12,'mac':13,'kankin':14,'muan':15,'pax':16,'koyab':17, 'cumhu':18,'uayet':19}
calender2=['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok',
           'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
days=list('imix,ik,akbal,kan,chicchan,cimi,manik,lamat,muluk,ok,chuen,eb,ben,ix,mem,cib,caban,eznab,canac,ahau'.split(','))
print(x)
for i in range(x):
    d,m,y=input().split()
    d=int(d[0:-1])
    y=int(y)
    tot=365*y+(calendar1[m]-1)*20+d+1
    newy=(tot-1)//260
    tot=tot%260
    num=(tot-1)%13+1
    newm=(tot-1)//20
    newd=(tot-1)%20+1
    print(num,days[newd-1],newy)