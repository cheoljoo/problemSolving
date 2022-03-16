impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut poppedIndex = 0;
        let mut stack = Vec::<i32>::new();  // let mut v = Vec::new();
        for v in pushed {
            if stack.len() == 0 {
                stack.push(v);
            } 
            else if v != popped[poppedIndex] {
                stack.push(v);
            }
            else {
                poppedIndex += 1;
            }
            while poppedIndex != popped.len() && stack.len() > 0 {
                if stack[stack.len()-1] == popped[poppedIndex] {
                    stack.pop();
                    poppedIndex += 1;
                } else {
                    break;
                }
            }
        }    
        if stack.len() == 0 && poppedIndex == popped.len() {
            return true
        } else {
            return false
        }
    }
}

// class Solution:
//     def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
//         poppedIndex = 0
//         stack = []
//         for v in pushed:
//             if len(stack) == 0:
//                 stack.append(v)
//             elif v != popped[poppedIndex]:
//                 stack.append(v)
//             else :  # v == popped[poppedIndex]:
//                 poppedIndex += 1
//             while poppedIndex != len(popped) and len(stack) > 0:
//                 if stack[-1] == popped[poppedIndex] :
//                     stack.pop()
//                     poppedIndex += 1
//                 else :
//                     break
//         if len(stack) == 0 and poppedIndex == len(popped):
//             return True
//         else :
//             return False