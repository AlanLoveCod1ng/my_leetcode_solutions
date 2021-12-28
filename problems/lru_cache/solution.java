import java.util.*;
class LRUCache {
    private class DNode{
        int value;
        int key;
        DNode next;
        DNode prev;
        void moveToTop(){
            this.next = tail;
            this.prev = tail.prev;
            tail.prev = this;
            this.prev.next = this;
        }
        void deleteSelf(){
            DNode nextNode = this.next;
            DNode prevNode = this.prev;
            this.next = null;
            this.prev = null;
            nextNode.prev = prevNode;
            prevNode.next = nextNode;
        }
    }
    Hashtable <Integer, DNode> table = new Hashtable<>();
    DNode head = new DNode();
    DNode tail = new DNode();
    int capacity;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        DNode temp = table.getOrDefault(key, null);
        if(temp==null){
            return -1;
        }
        temp.deleteSelf();
        temp.moveToTop();
        return temp.value;
    }
    
    public void put(int key, int value) {

        if(table.containsKey(key)){
            DNode temp = table.get(key);
            temp.deleteSelf();
            temp.moveToTop();
            temp.value = value;
        }
        else{
            DNode temp = new DNode();
            temp.value = value;
            temp.moveToTop();
            if(table.size()==capacity){
                int deletedKey = head.next.key;
                head.next.deleteSelf();
                table.remove(deletedKey);
            }
            temp.key = key;
            temp.value = value;
            table.put(key,temp);
        }

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */