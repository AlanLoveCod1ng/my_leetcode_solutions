//solution 1
// class Solution {
//     public int[] dailyTemperatures(int[] temperatures) {
//         int currentMaxIndex = temperatures.length-1;
//         int currentMax = temperatures[currentMaxIndex];
//         int[] results = new int [temperatures.length];
//         for(int i = results.length-2; i >=0; i--){
//             if(temperatures[i]>=currentMax){
//                 currentMaxIndex = i;
//                 currentMax = temperatures[i];
//                 continue;
//             }
//             for(int j = i+1; j<temperatures.length; j++){
//                 if(temperatures[j]>temperatures[i]){
//                     results[i] = j-i;
//                     break;
//                 }
//             }
//         }
//         return results;
//     }
// }
//solution 2
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int [] result = new int[temperatures.length];
        LinkedList<Integer> indexList = new LinkedList<>();
        LinkedList<Integer> valueList = new LinkedList<>();
        for(int i = 0; i < temperatures.length; i++){
            while(!valueList.isEmpty()&&valueList.getLast()<temperatures[i]){
                int index = indexList.removeLast();
                result[index] = i-index;
                valueList.removeLast();
            }
            indexList.add(i);
            valueList.add(temperatures[i]);
        }
        return result;
    }
}