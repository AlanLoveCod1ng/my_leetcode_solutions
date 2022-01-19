import java.util.*;
class SnapshotArray {
    int currentSnapId = 0;
    ArrayList<Hashtable<Integer, Integer>> list;
    public SnapshotArray(int length) {
        list = new ArrayList<>(length);
        for(int i = 0; i < length; i++){
            Hashtable<Integer, Integer> table = new Hashtable<>();
            table.put(0,0);
            list.add(table);
        }
    }
    
    public void set(int index, int val) {
        Hashtable<Integer,Integer> table = list.get(index);
        table.put(currentSnapId, val);
    }
    
    public int snap() {
        currentSnapId++;
        return currentSnapId-1;
    }
    
    public int get(int index, int snap_id) {
        Hashtable<Integer,Integer> table = list.get(index);
        if(!table.containsKey(snap_id)){
            while(!table.containsKey(snap_id)){
                snap_id--;
            }
        }
        return table.get(snap_id);
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */