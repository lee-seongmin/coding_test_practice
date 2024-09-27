def solution(letter):
    answer=''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    lst = []
    ch = ''
    for i in letter:
        if i==' ':
            lst.append(ch)
            ch= ''
        else:
            ch+=i
    n = 1
    ch=''
    while True:
        if letter[-n] == ' ':
            lst.append(ch)
            break
        else:
            print(letter[-n])
            ch+=letter[-n]
            n+=1
    print(lst)
    for j in lst:
        answer+=morse[j]
            
    return answer
solution(".... . .-.. .-.. ---")