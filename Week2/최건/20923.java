import java.util.*;
import java.io.*;


class Main{


    public static void main(String[] args) throws IOException {
        
        BufferedReader bf = new BufferedReader(new InputStreamReader((System.in)));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());   int M = Integer.parseInt(st.nextToken());
        Deque<Integer> doQueue = new ArrayDeque<>();
        Deque<Integer> suQueue = new ArrayDeque<>();
        for(int i = 0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            int doCard = Integer.parseInt(st.nextToken());
            int suCard = Integer.parseInt(st.nextToken());
            //
            doQueue.offerFirst(doCard);
            suQueue.offerFirst(suCard);
        }
        // END OF INIT
        Deque<Integer> doGround = new ArrayDeque<>(); 
        Deque<Integer> suGround = new ArrayDeque<>(); 
        int gameCount = 0;
        int turnFlag = 0;   // 0-->do's turn | 1-->su's turn
        while(gameCount < M && !doQueue.isEmpty() && !suQueue.isEmpty()){
            if(turnFlag == 0)
                doGround.offer(doQueue.poll());
            if(turnFlag == 1)
                suGround.offer(suQueue.poll());
            if(doQueue.isEmpty() || suQueue.isEmpty())
                break;
            turnFlag = (turnFlag + 1) % 2;
            gameCount += 1;
            //
            Integer doTop = doGround.peekLast();
            Integer suTop = suGround.peekLast();
            if(doTop != null && suTop !=null && doTop + suTop == 5){             //su win
                suQueue.addAll(doGround);
                suQueue.addAll(suGround);
                doGround = new ArrayDeque<>();
                suGround = new ArrayDeque<>();
            }
            else if((doTop != null && doTop == 5) || (suTop != null && suTop == 5)){  //do win
                doQueue.addAll(suGround);
                doQueue.addAll(doGround);
                doGround = new ArrayDeque<>();
                suGround = new ArrayDeque<>();
            }
        }

        // 0 --> draw
        // 1 --> su wins
        // 2 --> do wins
        if(doQueue.size() < suQueue.size())
            System.out.println("su");
        else if(suQueue.size() < doQueue.size())
            System.out.println("do");
        else 
            System.out.println("dosu");
    }
}