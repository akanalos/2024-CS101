myword=list(input().split())
pm=1
num1=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
num2=['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
s1=0
ans=0
for ele in myword:
    if ele=='negative':
        pm=-1
    elif ele in num1:
        s1+=num1.index(ele)
    elif ele in num2:
        s1+=(num2.index(ele)+2)*10
    elif ele in ['hundred', 'thousand', 'million']:
        if ele=='hundred':
            s1*=100
        elif ele=='thousand':
            s1 *= 1000
            ans+=s1
            s1=0
        elif ele=='million':
            s1 *= 1000000
            ans += s1
            s1 = 0
ans+=s1
ans=ans*pm
print(ans)