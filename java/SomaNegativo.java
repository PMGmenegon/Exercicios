import java.util.Scanner;
public class SomaNegativo {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float numero, soma = 0;
        boolean lopp = true;
        while(lopp){
            System.out.println("Digite um número:");
            numero = sc.nextFloat();
            if(numero>=0){
                soma+=numero;
            }else{
                System.out.printf("A soma dos números positivos é: %.2f", soma);
                lopp = false;
            }
        }
        sc.close();

    }
    
}
