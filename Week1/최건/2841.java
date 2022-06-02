import java.util.*;
import java.io.*;


class Main{

    static int string = 6;
    static int N, P;

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());   P = Integer.parseInt(st.nextToken());

        int answer = 0;

        Deque<Integer>[] stringStack = new ArrayDeque[7];
        for(int i = 0; i<7; i++)
            stringStack[i] = new ArrayDeque<>();
        for(int i = 0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            int s = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            
            Deque<Integer> aStack = stringStack[s];
            while(!aStack.isEmpty() && aStack.element() > p){
                aStack.pop();
                answer++;
            }
            if(aStack.isEmpty() || aStack.element() != p){
                aStack.push(p);
                answer++;
            }
        }
        System.out.println(answer);
    }
}
