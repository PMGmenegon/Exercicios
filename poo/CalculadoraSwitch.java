import java.util.Scanner;
public class CalculadoraSwitch {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int operação;
        float n1, n2, resultado;
        System.out.println("Digite a operação que você deseja!\n 1-ADIÇÃO\n 2-SUBTRAÇÃO\n 3-MULTIPLICAÇÃO\n 4-DIVISÃO");
        operação = sc.nextInt();
        System.out.println("Digite o primeiro número: ");
        n1 = sc.nextFloat();
        System.out.println("Digite o segundo número: ");
        n2 = sc.nextFloat();
        switch(operação){
            case 1:
                resultado = n1 + n2;
                System.out.printf("%f", resultado);
                break;
            case 2:
                resultado = n1 - n2;
                System.out.printf("%f", resultado);
                break;
            case 3:
                resultado = n1 * n2;
                System.out.printf("%f", resultado);
                break;
            case 4:
                if(n2 != 0){
                    resultado = n1 / n2;
                    System.out.printf("%f", resultado);
                } else {
                    System.out.println("Erro: Divisão por zero não é permitida.");
                    break;
                }
            sc.close();
        }
    }
        
}
