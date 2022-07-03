class Solution {
    Integer [][] memo;
    public boolean isValidPalindrome(String s, int k) {
        memo = new Integer[s.length()][s.length()];
        return k>=validPalindrome(s,0,s.length()-1);
    }
    public int validPalindrome(String s, int i, int j){
        if(i == j){
            return 0;
        }
        if(i == j-1){
            return s.charAt(i)!=s.charAt(j)? 1:0;
        }
        if(memo[i][j]!=null){
            return memo[i][j];
        }
        if(s.charAt(i)==s.charAt(j)){
            return memo[i][j] = validPalindrome(s,i+1,j-1);
        }
        return memo[i][j] = 1+Math.min(validPalindrome(s,i+1,j),validPalindrome(s,i,j-1));
    }
}