def main(list1):
    """
    A list of several elements is given. Return the last item.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    n=len(list1)
    return list1[n-1]
print(main(list1=[1,2,3,4,56,5]))