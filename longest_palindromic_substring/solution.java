class Solution {
    public String longestPalindrome(String s) {
        boolean [][] matrix = new boolean[s.length()][s.length()];
        int start = 0;
        int end = 0;
        for(int i = 0; i < s.length();i++){
            matrix[i][i] = true;
            if(i<s.length()-1){
                matrix[i][i+1] = s.charAt(i) == s.charAt(i+1);
                if (matrix[i][i+1]){
                    start = i;
                    end = i+1;
                }   
            }
        }
        int maxLength = 2;
        while(maxLength<s.length()){
            for(int i = 0; i+maxLength<s.length(); i++){
                matrix[i][i+maxLength] = s.charAt(i)==s.charAt(i+maxLength)&&matrix[i+1][i+maxLength-1];
                if(matrix[i][i+maxLength]){
                    start = i;
                    end = i+maxLength;
                }
                
            }
            maxLength++;
        }
        return s.substring(start,end+1);
    }
}