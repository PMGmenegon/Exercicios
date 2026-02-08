import java.util.Scanner;
import java.util.Random;
public class BubbleSort {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int numero;
        System.out.println("Digite a quantidade de elementos do vetor (máx = 50): ");
        numero = sc.nextInt();
        int[] lista = new int[numero];
        Random aleatorio = new Random();
        for(int i = 0; i < numero; i++){
            lista[i] = aleatorio.nextInt(100);
        }
        System.out.println("Vetor antes da ordenação:");
        for(int i = 0; i < numero; i++){
            System.out.printf("%d ", lista[i]);
        }
        bubbleSort(lista, numero);
        System.out.println("\nVetor após ordenação:");
        for(int i = 0; i < numero; i++){
            System.out.printf("%d ", lista[i]);
        }
        sc.close();
    }
    public static void bubbleSort(int[] vetor, int n){
        int aux;
        for(int i = 0; i < n - 1; i++){
            for(int j = 0; j < n - i - 1; j++){
                if(vetor[j] > vetor[j + 1]){
                    aux = vetor[j];
                    vetor[j] = vetor[j + 1];
                    vetor[j + 1] = aux;
                }
            }
        }
    }
}
