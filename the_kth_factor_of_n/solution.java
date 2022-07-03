class Solution {
    public int kthFactor(int n, int k) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 1; i<=n/2; i++){
            if(n%i==0){
                list.add(i);
            }
            if(list.size()==k){
                return list.get(k-1);
            }
        }
        list.add(n);
        return list.size()>=k?list.get(k-1):-1;
    }
}