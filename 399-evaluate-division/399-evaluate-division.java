import java.util.*;
class Currency{
    String name;
    Hashtable<Currency, Double> currencyMap;
    Currency(String name, Hashtable<Currency,Double> currencyMap){
        this.name = name;
        this.currencyMap = currencyMap;
    }
}
class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Hashtable<String,Currency> cur_table = new Hashtable<>();
        for(int i = 0; i < equations.size(); i++){
            String cur1name = equations.get(i).get(0);
            String cur2name = equations.get(i).get(1);
            double cur1_cur2 = values[i];
            Currency cur1 = cur_table.getOrDefault(cur1name, new Currency(cur1name, new Hashtable<>()));
            Currency cur2 = cur_table.getOrDefault(cur2name, new Currency(cur2name, new Hashtable<>()));
            cur1.currencyMap.put(cur2, cur1_cur2);
            cur2.currencyMap.put(cur1, 1/cur1_cur2);
            cur_table.put(cur1name,cur1);
            cur_table.put(cur2name,cur2);
        }
        double [] result = new double[queries.size()];
        for(int i = 0; i < queries.size(); i++){
            result[i] = bfs(cur_table,queries.get(i).get(0),queries.get(i).get(1));
        }
        return result;
    }
    public double bfs(Hashtable<String, Currency> cur_table, String startName, String targetName){
        Currency start = cur_table.getOrDefault(startName, null);
        Currency target = cur_table.getOrDefault(targetName, null);
        if(start == null || target == null){
            return -1;
        }
        HashSet<Currency> visited = new HashSet<>();
        LinkedList<Currency> cur_list = new LinkedList<>();
        LinkedList<Double> weight_list = new LinkedList<>();
        cur_list.addLast(start);
        weight_list.addLast(1.0);
        while(!cur_list.isEmpty()){
            Currency current = cur_list.removeFirst();
            double weight = weight_list.removeFirst();
            if(current == target){
                return weight;
            }
            for(Currency name: current.currencyMap.keySet()){
                if(visited.contains(name)){
                    continue;
                }
                cur_list.addLast(cur_table.get(name.name));
                weight_list.addLast(current.currencyMap.get(name)*weight);
                visited.add(name);
            }
        }
        return -1;
    }
}