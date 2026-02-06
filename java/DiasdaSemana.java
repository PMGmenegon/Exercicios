import java.util.Scanner;
public class DiasdaSemana {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int dia;
        System.out.println("Digite o número correspondente ao dia da semana ( 1 a 7 ): ");
        dia = sc.nextInt();
        switch(dia){
            case 1:
                System.out.println("Hoje é Domingo!");
                break;
            case 2:
                System.out.println("Hoje é Segunda-feira!");
                break;
            case 3:
                System.out.println("Hoje é Terça-feira!");
                break;
            case 4:
                System.out.println("Hoje é Quarta-feira!");
                break;
            case 5:
                System.out.println("Hoje é Quinta-feira!");
                break;
            case 6:
                System.out.println("Hoje é Sexta-feira!");
                break;
            case 7:
                System.out.println("Hoje é Sábado!");
                break;
            default:
                System.out.println("Número inválido!");
        }
        sc.close();

    }

    
}
