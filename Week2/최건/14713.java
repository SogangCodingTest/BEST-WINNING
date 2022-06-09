import java.util.*;
import java.io.*;


class Main{

    static int N = 0;
    static Queue[] inputs = null;
    static List<String> target = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        inputs = new LinkedList[N];

        for(int i = 0; i<N; i++){
            inputs[i] = new LinkedList();
            st = new StringTokenizer(bf.readLine());
            while(st.hasMoreTokens()){
                String word = st.nextToken();
                inputs[i].offer(word);
            }
        }
        
        st = new StringTokenizer(bf.readLine());
        while(st.hasMoreTokens()){
            String word = st.nextToken();
            target.add(word);
        }
        // END OF INIT
        int flag = 0;
        for(Iterator<String> itr = target.iterator(); itr.hasNext(); ){
            String word = itr.next();
            flag = 0;
            for(int i = 0; i<N; i++){
                if(!inputs[i].isEmpty() && word.equals(inputs[i].peek())){
                    inputs[i].poll();
                    flag = 1;
                    break;
                }
            }
            if(flag == 0)   break;
        }
        for(int i = 0; i<N; i++){
            if(!inputs[i].isEmpty())
                flag = 0;
        }
        if(flag == 0)
            System.out.println("Impossible");
        else
            System.out.println("Possible");
    }
}