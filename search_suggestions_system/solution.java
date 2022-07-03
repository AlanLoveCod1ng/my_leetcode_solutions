class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> result = new LinkedList<>();
        for(int i = 1; i <= searchWord.length(); i++){
            String temp = searchWord.substring(0, i);
            List<String> list = new LinkedList<>();
            for(String str: products){
                if(str.startsWith(temp)){
                    list.add(str);
                }
                if(list.size()==3){
                    break;
                }
            }
            result.add(list);
        }
        return result;
    }
}