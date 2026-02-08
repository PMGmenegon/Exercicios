import java.util.Scanner;
public class TamanhoPalavra {
    public static void main(String[] args){
        Scanner sc = new Scanner (System.in);
        String [] palavras = new String[6];
        String [] palavrasMaiores = new String[6];
        for(int i = 0; i < palavras.length; i++){
            System.out.println("Digite uma palavra:");
            palavras[i] = sc.nextLine();
            if(palavras[i].length() > 5){
                palavrasMaiores[i] = palavras[i];
            }
        }
        System.out.println("Palavra com mais de 5 letras:");
        for(int i =0; i < palavrasMaiores.length; i++){
            if(palavrasMaiores[i] != null){
                System.out.println(palavrasMaiores[i]);
            }
        }
        sc.close();
    }
}
