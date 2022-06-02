import java.util.*;
import java.io.*;


class Main{

    static int N = 0;
    static String exp = "";
    static double[] operand = null;
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        operand = new double[N];
        exp = bf.readLine();
        
        for(int i = 0; i<N; i++)    operand[i] = Integer.parseInt(bf.readLine());
        
        // END OF INPUT PROCESSING

        Deque<Double> stack = new ArrayDeque<>();
        for(int i = 0; i<exp.length(); i++){
            char c = exp.charAt(i);
            if('A' <= c && c <= 'Z'){   // in case of NUMBER
                stack.push(operand[c - 'A']);
            }
            else{   // in case of OPERATOR
                double b = stack.pop();
                double a = stack.pop();
                double ab = 0;
                switch(c){
                    case '+':
                        ab = a + b;
                        break;
                    case '-':
                        ab = a - b;
                        break;
                    case '*':
                        ab = a * b;
                        break;
                    case '/':
                        ab = a / b;
                        break;
                }
                stack.push(ab);
            }
        }
        System.out.printf("%.2f\n", stack.pop());
    }
}