import java.util.Scanner;
public class SeparandoPalavras {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] palavras = new String[10];
        String[] palavrasGrandes = new String[10];
        String[] palavrasPequenas = new String[10];
        for(int i = 0; i < palavras.length; i++){
            System.out.println("Digite um palavra: ");
            palavras[i] = sc.nextLine();
            if(palavras[i].length() > 7){
                palavrasGrandes[i] = palavras[i];
            } else {
                palavrasPequenas[i] = palavras[i];
            }
        }
        palavrasGrandes(palavrasGrandes);
        palavrasPequenas(palavrasPequenas);
        sc.close();
    } 
    public static void palavrasGrandes(String[] arr){
        int contador = 0;
        for(int i =0; i < arr.length; i++){
            if(arr[i] != null){
                System.out.printf("%s e seu tamanho é %d\n", arr[i], arr[i].length());
                contador++;
            }
        }
        System.out.printf("%d\n", contador);
        
    }
    public static void palavrasPequenas(String[] arr1){
        int contador1 = 0;
        for(int i =0; i < arr1.length; i++){
            if(arr1[i] != null){
                System.out.printf("%s e seu tamanho é %d\n", arr1[i], arr1[i].length());
                contador1++;
            }
        }
        System.out.printf("%d\n", contador1);
    }
}
