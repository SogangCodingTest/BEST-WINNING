import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken()); // num of space
        int M = Integer.parseInt(st.nextToken()); // about cars
        int[] parkingSpace = new int[N+1];
        int[] pricePerSpace = new int[N+1];
        int[] weightOfCars = new int[M+1];
        for(int i = 1; i<=N; i++)    pricePerSpace[i] = Integer.parseInt(bf.readLine());
        for(int i = 1; i<=M; i++)    weightOfCars[i] = Integer.parseInt(bf.readLine());
        //
        Queue<Integer> queueForWating = new LinkedList<>();
        int tot = 0;
        for(int i = 0; i<2*M; i++){
            int command = Integer.parseInt(bf.readLine());
            if(command > 0) queueForWating.offer(command);
            else{   // command < 0
                int j = 1;
                for(; j<=N; j++)    if(parkingSpace[j] == -command) break;
                tot += pricePerSpace[j] * weightOfCars[-command];
                parkingSpace[j] = 0;
            }
            // QUEUE PROCESSING
            while(!queueForWating.isEmpty()){
                int j = 1;
                for(; j<=N; j++)    if(parkingSpace[j] == 0)    break;
                if(j == N+1)    break;
                parkingSpace[j] = queueForWating.poll();
            }
        }
        System.out.println(tot);
    }
}