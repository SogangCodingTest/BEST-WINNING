import java.util.*;
import java.io.*;


class Main{


    static int n, w, L;
    static int[] weightOfTrucks = null;

    public static void main(String[] args) throws IOException {


        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        //
        n = Integer.parseInt(st.nextToken());   // The number of trucks
        w = Integer.parseInt(st.nextToken());   // The length of bridge
        L = Integer.parseInt(st.nextToken());   // The maximum weight of bridge
        //
        weightOfTrucks = new int[n];
        Queue<Integer> bridgeQueue = new LinkedList<>();
        Queue<Integer> truckQueue = new LinkedList<>();
        for(int i = 0; i<w; i++)    bridgeQueue.offer(0);
        st = new StringTokenizer(bf.readLine());
        for(int i = 0; i<n; i++)    truckQueue.offer(Integer.parseInt(st.nextToken()));
        //
        int count = 0;
        while(true){    // Per a unit time
            // Step 1
            bridgeQueue.poll();
            // Step 2
            int totBridgeWeight = 0;
            for(Iterator<Integer> itr = bridgeQueue.iterator(); itr.hasNext(); )    
                totBridgeWeight += itr.next();
            if(!truckQueue.isEmpty() && totBridgeWeight + truckQueue.element() <= L)
                bridgeQueue.offer(truckQueue.poll());
            else
                bridgeQueue.offer(0);
            count += 1;
            
            totBridgeWeight = 0;
            for(Iterator<Integer> itr = bridgeQueue.iterator(); itr.hasNext(); )    
                totBridgeWeight += itr.next();
            if(truckQueue.isEmpty() && totBridgeWeight == 0){
                break;
            }
        }
        System.out.println(count);
    }
}