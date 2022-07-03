class Solution {
    public String gcdOfStrings(String str1, String str2) {
        String publicPart = "";
        for(int i = 0; i<str1.length()&&i<str2.length(); i++){
            if(str1.charAt(i)==str2.charAt(i)){
                publicPart = str1.substring(0,i+1);
            }
        }
        for(int i = publicPart.length(); i>=0; i--){
            String unit = publicPart.substring(0,i);
            if(isDivider(unit,str1)&&isDivider(unit,str2)){
                return unit;
            }
        }
        return "";
    }
    boolean isDivider(String unit, String tested){
        if(unit.length()==0){
            return true;
        }
        if(tested.length()%unit.length()!=0){
            return false;
        }
        String temp = "";
        for(int i = 0; i<tested.length(); i+=unit.length()){
            temp+=unit;
            if(!tested.contains(temp)){
                return false;
            }
        }
        return true;
    }
}