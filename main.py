class Stack:

    def __init__(self, elements):
        self.elements = elements

    def is_empty(self):
        return not bool(self.elements)

    def push(self, new_element):
        self.elements.append(new_element)

    def pop(self):
        self.elements.pop()
        return self.peek()

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]

    def size(self):
        return len(self.elements)


def is_balanced(brackets):
    st = Stack(list(brackets))
    if st.size() % 2 != 0:
        return 'Небалансированно'
    elif st.peek() not in (')', '}', ']'):
        return 'Небалансированно'
    else:
        st2 = Stack([])
        while not st.is_empty():
            last_el = st.peek()
            if last_el in (')', '}', ']'):
                st2.push(last_el)
            elif last_el == '(':
                if st2.peek() == ')':
                    st2.pop()
            elif last_el == '{':
                if st2.peek() == '}':
                    st2.pop()
            elif last_el == '[':
                if st2.peek() == ']':
                    st2.pop()
            st.pop()
        if st2.size() == 0:
            return 'Сбалансированно'
        else:
            return 'Небалансированно'


if __name__ == '__main__':
    print(is_balanced('([)[]]'))

