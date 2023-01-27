class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        1. 입력받은 문자열을 's' 라 하자.
        2. stack_list = []
        3. delete_index_list = []
        4. 입력받은 문자열을 한 글자씩, index와 함께 순회를 한다.
        5.1. 순회를 하는 문자열이 '(' 이면 stack_list에 저장한다.
        5.2.1 순회를 하는 문자열이 ')' 이면 stack_list에 담겨 있는 것이 있을 경우 stack_list에 가장 마지막에 들어간 것을 제거한다.
        5.2.2 순회를 하는 문자열이 ')' 이면 stack_list에 담겨 있는 것이 없을 경우 delete_index_list에 index를 추가한다.
        6. 순회가 끝나면 delete_index_list 에 있는 
        '''
        stack_list = []
        delete_index_list = []
        answer_list = []
        for i, ch in enumerate(s):
            if '(' == ch:
                #return (i, ch) # 왜 리스트 지? 튜플일 줄 알았는데
                stack_list.append((i,ch))
            elif stack_list and ')' == ch:
                stack_list.pop()
            elif not stack_list and ')' == ch:
                delete_index_list.append(i)
        # return stack_list
        # stack_list에 남아 있는 것이 있으면 -> 
        if stack_list:
            for i in stack_list:
                delete_index_list.append(i[0])
        for i, ch in enumerate(s):
            if not i in delete_index_list:
                answer_list.append(ch)
        return ''.join(answer_list)
        
                
            
                
        
                
        
        
        
        
                
                