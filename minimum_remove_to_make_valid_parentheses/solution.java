class Solution {
    public String minRemoveToMakeValid(String s) {
        LinkedList<Integer> queue = new LinkedList<>();
        HashSet<Integer> record = new HashSet<>();
        String newStr = "";
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i)=='('){
                queue.add(i);
            }
            else if(s.charAt(i)==')'){
                if(!queue.isEmpty()){
                    record.add(queue.pop());
                    record.add(i);
                }
            }
            else{
                record.add(i);
            }
        }
        for(int i = 0; i<s.length(); i++){
            if(record.contains(i)){
                newStr+=s.charAt(i);
            }
        }
        return newStr;
    }
}