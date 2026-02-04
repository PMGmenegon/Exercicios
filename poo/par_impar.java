import java.util.Scanner;
public class par_impar {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int contador_par, contador_impar, numero, i;
        contador_par = 0;
        contador_impar = 0;
        for(i=0; i<10; i++){
            System.out.println("Digite um número inteiro: ");
            numero = sc.nextInt();
            if(numero % 2 == 0){
                contador_par++;
            } else {
                contador_impar++;
            }
        if(i == 9){
            System.out.printf("Quantidade de pares: %d\nQuantidade de ímpares: %d\n", contador_par, contador_impar);
            sc.close();
        }
        }
    }
    
}
