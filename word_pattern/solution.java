import java.util.Hashtable;
class Solution {
    Hashtable<String, String> table1 = new Hashtable<>();
    Hashtable<String, String> table2 = new Hashtable<>();
    public boolean wordPattern(String pattern, String s) {
        String [] strs = s.split(" ");
        if(strs.length!=pattern.length()){
            return false;
        }
        for(int i = 0; i<pattern.length(); i++){
            String currentPattern = pattern.charAt(i)+"";
            if(!table1.containsKey(currentPattern)){
                table1.put(currentPattern,strs[i]);
            }
            else{
                if(!table1.get(currentPattern).equals(strs[i])){
                    return false;
                }
            }
            if(!table2.containsKey(strs[i])){
                table2.put(strs[i],currentPattern);
            }
            else{
                if(!table2.get(strs[i]).equals(currentPattern)){
                    return false;
                }
            }
        }
        return true;
    }
}