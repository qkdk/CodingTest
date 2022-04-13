def solution(new_id):
    
    new_id = new_id.lower()
    word =''
    
    del_char = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']
    for i in range(len(new_id)):
        if new_id[i] in del_char:
            pass
        else:
            word += new_id[i]
       
    new_id = word
    
    while '..' in new_id:
        new_id = new_id.replace('..','.')
        
    new_id = new_id.strip('.')
    
    if new_id == '':
        new_id = 'a'
        
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')

    while len(new_id)<3:
        new_id += new_id[-1]
    
    answer = new_id

    return answer