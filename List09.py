def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    s=0
    n=len(list1)
    while i<n:
        if list1[0]==list1[i]:
            s=s+1
    
        
        i=i+1
    if s==n:
        s=True
    else:
        s=False
    return s
list1=[0,0,0,0,0]
print(main(list1))