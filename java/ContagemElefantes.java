import java.util.Scanner;

public class ContagemElefantes {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um número inteiro:");
        int n = sc.nextInt();
        for(int i = n; i >= 1; i--) {
            System.out.print(" ");
            for(int j = 0; j < i; j++) {
                if(i == 1) {
                    System.out.print("elefante ");
                } else {
                    System.out.print("elefantes ");
                }
            }
            if(i == 1) {
                System.out.println("incomoda");
            } else {
                System.out.println("incomodam");
            }
        }
        sc.close();
    }
}
