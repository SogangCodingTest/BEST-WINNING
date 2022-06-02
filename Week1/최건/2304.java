import java.util.*;
import java.io.*;


class Main{
    public static void main(String[] args) throws IOException{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        
        MyStack<Node> stack = new MyStack<>();
        List<Node> inputs = new LinkedList<>();
        for(int i = 0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            int x_ = Integer.parseInt(st.nextToken());
            int y_ = Integer.parseInt(st.nextToken());
            Node input = new Node(x_, y_);
            inputs.add(input);
        }
        Collections.sort(inputs); 

        int cur_y = 0;
        for(int i = 0; i<N; i++){
            Node target = inputs.get(i);
            int x_ = target.x; int y_ = target.y;

            if(cur_y <= y_){
                while(!stack.isEmpty() && stack.get().y < cur_y)
                    stack.pop();
                stack.push(target);                
                cur_y = y_;
            }
            else{ // in case cur_y > y_
                while(!stack.isEmpty() && stack.get().y <= y_)
                    stack.pop();
                stack.push(target);
            }
        }

        int answer = 0;
        if(!stack.isEmpty()){
            Node target1 = stack.pop();
            while(!stack.isEmpty()){
                Node target2 = stack.pop();
                answer += getRectagleSize(target1, target2);
                target1 = target2;
            }
        }

        System.out.println(answer + cur_y);
    }

    public static int getRectagleSize(Node node1, Node node2){
        
        int width = (node1.x < node2.x) ? (node2.x - node1.x) : (node1.x - node2.x);
        int height = (node1.y < node2.y) ? node1.y : node2.y;
        return width * height;
    }
}

class MyStack<E> extends ArrayDeque<E>{
    public E pop(){
        return this.removeFirst();
    }

    public E get(){
        return this.getFirst();
    }

    public void push(E item){
        this.addFirst(item);
    }
}

class Node implements Comparable<Node>{
    int x, y;
    Node(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int compareTo(Node o){
        return this.x - o.x;
    }

    @Override
    public String toString(){
        return ""+this.x + " " + this.y;
    }
}