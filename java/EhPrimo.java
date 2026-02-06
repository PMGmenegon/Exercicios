import java.util.Scanner;
public class EhPrimo {
    public static void main(String[] args){
        Scanner sc = new Scanner (System.in);
        int  limite, contador = 0;
        System.out.println("Digite um número maior que 2: ");
        limite = sc.nextInt();
        if(limite > 2){
            for(int i=2; i<=limite; i++){
                boolean primo = true;
                for(int j=2; j<i; j++){
                    if(i%j == 0){
                        primo = false;
                        break;
                    }
                }
                if(primo){
                    System.out.println(i);
                    contador++;
                }
            }
        }
        System.out.println("Quantidade de números primos: " + contador);

    }
    
}
