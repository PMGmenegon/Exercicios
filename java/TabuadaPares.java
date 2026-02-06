import java.util.Scanner;
public class TabuadaPares {
    public static void main(String[] args){
        int numero, i;
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um número o qual você quer sua tabuada:");
        numero = sc.nextInt();
        for(i=1; i<=10; i++){
            if((numero*i) % 2 ==0){
                System.out.printf("%d\n", numero * i);
            }
        }
        if(i == 10){
            sc.close();
        }

    }
    
}
