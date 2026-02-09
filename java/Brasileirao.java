import java.util.Scanner;
public class Brasileirao{
    public static void main (String[] args){
        Scanner sc;
        int pontos1, pontos2, diferença, vitorias;
        sc = new Scanner (System.in);
        System.out.println("Digite os pontos do líder: ");
        pontos1 = sc.nextInt();
        System.out.println("Digite os pontos do lanterna: ");
        pontos2 = sc.nextInt();
        diferença = pontos1 - pontos2;
        if (diferença % 3 == 0){
            vitorias = diferença / 3;
        }else{
            vitorias = (diferença / 3) + 1;
        }
        System.out.printf("O lanterna precisa de %d vitórias para alcançar o líder.", vitorias);
    }
}