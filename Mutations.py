def mutate_string(string, position, character):
    list2=list(string)
    list2[position]=character      
    return ''.join(list2)
