class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. stack = []
        2. mapping_table = {
                '}': '{',
                ']': '[',
                ')': '(',
        }
        3. 입력받은 문자열을 i라고 하자.
        4. 입력받은 문자열이 mapping_table key와 다를 경우 stack에 넣자.
        5. 입력받은 문자열이 mapping_table key와 같을 경우 다음의 조건식을 수행
        6. mapping_table[i] ==  stack[-1]이 같으면 stack에서 가장 마지막에 생긴 원소를 제거한다.(pop)
        7. 만약 다르면 false를 return 한다.
        '''
        stack = []
        mapping_table = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for char in s:
            if not char in mapping_table:
                stack.append(char)
                continue
            else:
                if len(stack) == 0:
                    return False
                elif mapping_table[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        
            
        

        