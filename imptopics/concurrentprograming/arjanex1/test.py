from iot.message import Message, MessageType

lst = []
a = Message('abc',MessageType.SWITCH_ON,'xyz')
b = Message('pqr',MessageType.SWITCH_ON,'xyz')
lst.append(a)
lst.append(b)


def print_list(lst) -> None:
    for item in lst:
        print(item)

print_list(lst)