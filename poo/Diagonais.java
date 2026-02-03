import java.util.Scanner;
import java.util.Random;

public class Diagonais {
    public static void main (String[] args){

        Scanner sc = new Scanner(System.in);
        int n, soma1 = 0, soma2 = 0;
        System.out.println("Digite o índice da matriz: ");
        n = sc.nextInt();
        int[][] matriz = new int[n][n];
        Random numeros = new Random();
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++){
                matriz[i][j] = numeros.nextInt(20);
                if(j > i){
                    soma1 += matriz[i][j];
                } 
                else if(i > j){
                    soma2 += matriz[i][j];
                }
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
        System.out.printf("Soma dos acima da diagonal: %d", soma1);
        System.out.printf("\nSoma dos abaixo da diagonal: %d", soma2);
        if (soma1 > soma2){
            System.out.println("\nA soma acima da diagonal é maior.");
        } else if (soma2 > soma1){
            System.out.println("\nA soma abaixo da diagonal é maior.");
        } else {
            System.out.println("\nAs somas são iguais.");
        }
        sc.close();
    }
}
