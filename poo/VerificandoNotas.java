import java.util.Scanner;
public class VerificandoNotas {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float nota;
        System.out.println("Digite sua nota: ");
        nota = sc.nextFloat();
        if( nota<0 || nota>10){
            System.out.println("Nota inválida!");
        }
        else if(nota == (int)nota){
            int notaInteira = (int)nota;
            switch(notaInteira){
                case 0:
                case 1:
                case 2:
                case 3:
                case 4:
                    System.out.println("Reprovado!");
                    break;
                case 5:
                case 6:
                    System.out.println("Recuperação!");
                    break;
                case 7:
                case 8:
                case 9:
                case 10:
                    System.out.println("Aprovado!");
                    break;
            }
        }else{
            if(nota>=8.5){
                System.out.println("Aprovado com mérito!");
            }else if(nota<7 && nota>4){
                System.out.println("Recuperação!");
            }else if(nota<=4){
                System.out.println("Reprovado!");
            }else{
                System.out.println("Aprovado!");
            }
        sc.close();
        }
    }
}
