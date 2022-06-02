import java.util.*;
import java.io.*;

class Main{

    static String input = null;
    static int[] posInfo = null;
    static TreeSet<String> answers = new TreeSet<>();
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        input = bf.readLine();
        posInfo = new int[input.length()];
        Arrays.fill(posInfo, -1);
        {
            Deque<Integer> stack = new ArrayDeque<>();
            for(int i = 0; i<input.length(); i++){
                if(input.charAt(i) == '(')
                    stack.push(i);
                else if(input.charAt(i) == ')'){
                    int headIndex = stack.pop();
                    posInfo[headIndex] = i;
                    posInfo[i] = headIndex;
                }
            }
        }
        // END OF INPUT PROCESSING

        boolean[] selected = new boolean[input.length()];
        dfs(0, selected);
        answers.remove(input);
        StringBuilder sb = new StringBuilder();
        for(Iterator<String> itr = answers.iterator(); itr.hasNext(); ){
            sb.append(itr.next());
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    public static void dfs(int index, boolean[] selected){
        if(index == input.length()){
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i<input.length(); i++)
                if(selected[i]) sb.append(input.charAt(i));
            answers.add(sb.toString());
            return;
        }
        // =================================
        if(input.charAt(index) == '('){
            selected[index] = true;
            selected[posInfo[index]] = true;
            dfs(index+1, selected);            
            selected[index] = false;
            selected[posInfo[index]] = false;
            // ------------------------------
            dfs(index+1, selected);
        }
        else if(input.charAt(index) == ')'){
            dfs(index+1, selected);
        }
        else{
            selected[index] = true;
            dfs(index+1, selected);
            selected[index] = false;
        }
    }
}