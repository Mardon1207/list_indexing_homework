def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    n=len(list1)
    if list1[0]>list1[n-1]:
        s=list1[0]
    else:
        s=list1[n-1]
    return s
list1=[5,32,1,4,3]
print(main(list1))