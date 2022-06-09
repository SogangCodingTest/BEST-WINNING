import java.util.*;
import java.io.*;


class Main{

    static int N = 0;   // size of map
    static int K = 0;   // the number of apples
    static int L = 0;   // the number of changing directions

    static List<Point> apples = new ArrayList<>();
    static Deque<Turn> turns = new ArrayDeque<>();
    static Deque<Point> snake = new ArrayDeque<>();

    //                          <-L .  D->
    static int[] x_ = new int[]{1,0,-1,0};
    static int[] y_ = new int[]{0,1,0,-1};
    static int curDirection = 0;
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        K = Integer.parseInt(st.nextToken());
        for(int i = 0; i<K; i++){
            st = new StringTokenizer(bf.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            apples.add(new Point(x, y));
        }
        //
        st = new StringTokenizer(bf.readLine());
        L = Integer.parseInt(st.nextToken());
        for(int i = 0; i<L; i++){
            st = new StringTokenizer(bf.readLine());
            int time = Integer.parseInt(st.nextToken());
            String turn = st.nextToken();
            turns.offer(new Turn(time, turn));
        }
        snake.offer(new Point(1, 1));
        // END OF INIT. START!
        int time = 0;
        while(true){
            time++;
            Point headPoint = snake.peekLast(); 
            // step1
            snake.offer(new Point(headPoint.x + x_[curDirection], headPoint.y + y_[curDirection]));
            if(alive() == false){
                break;
            }
            // step2
            headPoint = snake.peekLast();
            int flag = 0;
            for(Iterator<Point> itr = apples.iterator(); itr.hasNext(); ){
                Point tempApple = itr.next();
                if(headPoint.equals(tempApple)){
                    apples.remove(tempApple);
                    flag = 1;
                    break;
                }
            }
            if(flag == 0)   snake.poll();

            // change direction
            if(!turns.isEmpty() && time == turns.peek().x){
                curDirection += turns.peek().y;
                if(curDirection == -1)  curDirection = 3;
                if(curDirection == 4)   curDirection = 0;
                turns.poll();
            }
        }
        System.out.println(time);
    }

    static boolean alive(){
        Point headPoint = snake.peekLast();
        // case 1 : Bang! with wall
        if(headPoint.x < 1 || N < headPoint.x || headPoint.y < 1 || N < headPoint.y){
            return false;
        }
        // case 2 : self-Bang!
        for(Iterator<Point> itr = snake.iterator(); itr.hasNext(); ){
            Point partOfSnake = itr.next();
            if(partOfSnake.equals(headPoint) && partOfSnake != headPoint)
                return false;
        }
        return true;
    }
}

class Turn extends Point{
    Turn(int time, String turn){
        super(time, (turn.equals("D") ? 1 : -1)); // D(right) : 1, L(left) : -1
    }
}

class Point{
    int x, y;
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
        return (this.x == ((Point)obj).x && this.y == ((Point)obj).y);
    }

    @Override
    public String toString(){
        return "x: "+x+", y: "+y;
    }
}