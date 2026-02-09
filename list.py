print("Operations on list")
lst = ['cherry', 'watermelon', 'tangerines', 'apple', 'pear']

print("Length of list:", len(lst))
print("Print watermelon:", lst[1])

lst.append('passionfruit')
print("List after new fruit:", lst)
lst.remove('apple')
print("List after removing a fruit:", lst)
lst.pop(3)
print("List after popping a fruit", lst)