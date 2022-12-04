
letter = ".... . .-.. .-.. ---"

morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}


def solution(letter):
    res = ''
    arr = list(letter.split())

    for i in arr:
        res += morse[i]
                
    return res

print(solution(letter))
