// https://codeforces.com/problemset/problem/1791/A

import java.util.Scanner;

public class CodeForcesChecking {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int inputNumber = scanner.nextInt();
        scanner.nextLine();
        char[] input = new char[inputNumber];

        for (int i = 0; i < input.length; i++) {
            input[i] = scanner.next().charAt(0);
            scanner.nextLine();
        }

        String txt = "codeforces";

        for (int i = 0; i < input.length; i++) { 
            boolean isThere = false;
            for (int j = 0; j < txt.length(); j++) {
                if (input[i] == txt.charAt(j)) {
                    isThere = true;
                }

                if (isThere) {
                    System.out.println("YES");
                    break;
                } 
            }

            if (!isThere) {
                System.out.println("NO");
            }
        }

        scanner.close();
    }
}
