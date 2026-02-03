import java.util.Scanner;
public class IMCcom_scanner {
    public static void main (String[] args){
        Scanner sc;
        double peso, altura,imc;
        sc = new Scanner(System.in);
        System.out.println("Digite seu peso em kg: ");
        peso = sc.nextDouble();
        System.out.println("Digite sua altura em metros: ");
        altura = sc.nextDouble();
        imc = peso / (altura * altura);
        System.out.printf("Seu IMC é: %f", imc);
        sc.close();
    }
}
