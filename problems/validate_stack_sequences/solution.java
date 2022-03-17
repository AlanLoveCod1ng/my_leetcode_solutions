class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int pushIndex = 0;
        int popIndex = 0;
        while(pushIndex<=pushed.length&&popIndex<=popped.length){
            if(popIndex>=popped.length){
                return true;
            }
            if(stack.isEmpty()){
                if(pushIndex>=pushed.length){
                    return false;
                }
                stack.push(pushed[pushIndex]);
                pushIndex++;
                continue;
            }
            if(stack.peek()==popped[popIndex]){
                stack.pop();
                popIndex++;
                continue;
            }else{
                if(pushIndex>=pushed.length){
                    return false;
                }
                stack.push(pushed[pushIndex]);
                pushIndex++;
                continue;
            }
        }
        return true;
    }
    
}