import java.util.*;
class Solution {
    public boolean isValid(String s) {
        LinkedList<Character> stack = new LinkedList<>();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{'){
                stack.addLast(s.charAt(i));
                continue;
            }
            char a = s.charAt(i);
            if(stack.isEmpty()){
                return false;
            }
            if(a == ')'){
                char b = stack.removeLast();
                if(b != '(')return false;
            }
            else if(a == ']'){
                char b = stack.removeLast();
                if(b != '[')return false;
            }
            else if(a == '}'){
                char b = stack.removeLast();
                if(b != '{')return false;
            }
        }
        return stack.isEmpty();
    }
}