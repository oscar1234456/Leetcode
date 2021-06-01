class MyCircularQueue {
public:
    int front = 0;
    int rear = 0;
    int capacity = 0;
    int *queue;
    bool lastOp = false; //true: push, false:pop
    MyCircularQueue(int k) {
        capacity = k;
        queue = new int[capacity];
    }
    
    bool enQueue(int value) {
        if(isFull()) return false;
        rear = (rear+1)%capacity;
        queue[rear] = value;
        lastOp = true;
        return true;
    }
    
    bool deQueue() {
        if(isEmpty()) return false;
        front = (front+1)%capacity;
         lastOp = false;
        return true;
    }
    
    int Front() {
        if(!isEmpty()) return queue[(front+1)%capacity];
        else return -1;
    }
    
    int Rear() {
        if(!isEmpty()) return queue[rear%capacity];
        else return -1;
    }
    
    bool isEmpty() {
        if (!lastOp && front == rear) return true;
        else return false;
    }
    
    bool isFull() {
        if (lastOp && front == rear) return true;
        else return false;
    }
    
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */