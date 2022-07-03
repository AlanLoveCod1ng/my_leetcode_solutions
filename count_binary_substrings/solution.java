class Solution {
    public int countBinarySubstrings(String s) {
        if(s.length()==1){
            return 0;
        }
        int result = 0;
        LinkedList<Integer>turningStartIndex = new LinkedList<>();
        for(int i = 0; i < s.length()-1; i++){
            if(s.charAt(i)!=s.charAt(i+1)){
                turningStartIndex.add(i);
            }
        }
        for(int i: turningStartIndex){
            int start = i;
            int end = i+1;
            while(true){
                result++;
                start--;
                end++;
                if(start>=0&&end<s.length()){
                    if(s.charAt(start)!=s.charAt(start+1)||s.charAt(end)!=s.charAt(end-1)){
                        break;
                    }
                }else{
                    break;
                }
            }
        }
        return result;
    }
}