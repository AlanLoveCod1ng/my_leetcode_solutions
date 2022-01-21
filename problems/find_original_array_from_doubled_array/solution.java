import java.util.HashMap;
class Solution {
    public int[] findOriginalArray(int[] changed) {
        Arrays.sort(changed);
        if(changed.length%2!=0){
            return new int[0];
        }
        int [] result = new int [changed.length/2];
        int current = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = changed.length-1; i>=0; i--){
            if(map.containsKey(changed[i])&&changed[i]!=0){
                map.put(changed[i],map.get(changed[i])+1);
                continue;
            }
            if(!map.containsKey(changed[i]*2)){
                map.put(changed[i],1);
                continue;
            }
            if(map.containsKey(changed[i]*2)){
                if(map.get(changed[i]*2)>0){
                    map.put(changed[i]*2,map.get(changed[i]*2)-1);
                    result[current] = changed[i];
                    current++;
                }else{
                    map.put(changed[i],1);
                }
                continue;
            }
            map.put(changed[i],-1);
        }

        if(current==result.length){
            return result;
        }
        return new int[0];
    }
}