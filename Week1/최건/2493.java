import java.util.*;
import java.io.*;


class Main {

    static int N = 0;
    static TreeSet<Pair> set = new TreeSet<>();
    
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i<=N; i++){
            int tempHeight = Integer.parseInt(st.nextToken());
            Pair tempPair = new Pair(i, tempHeight);
            if(!set.isEmpty() && set.ceiling(tempPair) != null)
                sb.append(set.ceiling(tempPair).key);
            else
                sb.append(0);
            sb.append(" ");
            set.add(tempPair);
        }
        System.out.println(sb.toString());
    }

}

// key : coord, value : height
class Pair implements Comparable<Pair>{
    int key, value;

    Pair(int key, int value){
        this.key = key;
        this.value = value;
    }

    @Override
    public int compareTo(Pair o) {
        return this.value - o.value;
    }
}
