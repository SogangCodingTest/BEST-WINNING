import java.util.*;
import java.io.*;


class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String input = bf.readLine();
        int index = 1;
        while(input.charAt(0) != '-'){
            sb.append(index);   sb.append(". ");
            int answer = 0;
            Deque<Integer> stack = new ArrayDeque<>();
            for(int i = 0; i<input.length(); i++){
                if(input.charAt(i) == '{'){
                    stack.push(0);
                }
                else{   // == '}'
                    if(!stack.isEmpty())      
                        stack.pop();
                    else{
                        answer++;
                        stack.push(0);
                    }
                }
            }
            answer += stack.size() / 2; 
            sb.append(answer);  sb.append("\n");
            //
            input = bf.readLine();
            index++;
        }
        System.out.println(sb);
    }
}
// {{{}

// { { } { { } } }
// { { } { } } } }

// { { { } } }
// { { } } } }

// } {