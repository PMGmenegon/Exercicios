import java.util.Scanner;
public class ArredondandoNumeros {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float numero;
        boolean laço = true;
        while(laço){
            System.out.println("Digite um númer real:");
            numero = sc.nextFloat();
            if(numero < 0){
                laço = false;
            }else if(numero == (int)numero){
                System.out.println("Já está exato!");
            }
            else{
                System.out.printf("Número arredondado para cima: %f\n", Math.ceil(numero));
            }

        }
        sc.close();
    }
}   

