class Solution {
    public boolean validPalindrome(String s) {
        int startIndex = 0;
        int endIndex = s.length()-1;
        while(startIndex<endIndex){
            if(s.charAt(startIndex)!=s.charAt(endIndex)){
                return isPalindrome(s.substring(startIndex,endIndex))||isPalindrome(s.substring(startIndex+1,endIndex+1));
            }
            startIndex++;
            endIndex--;
        }
        
        return true;
    }
    public boolean isPalindrome(String s){
        int startIndex = 0;
        int endIndex = s.length()-1;
        while(startIndex<endIndex){
            if(s.charAt(startIndex)!=s.charAt(endIndex)){
                return false;
            }
            startIndex++;
            endIndex--;
        }
        return true;
    }
}