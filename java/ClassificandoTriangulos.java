import java.util.Scanner;
public class ClassificandoTriangulos {
    public static void main(String[] args){
        Scanner sc = new Scanner (System.in);
        int lado1, lado2, lado3;
        boolean permissao;
        System.out.println("Digite o valor do primeiro lado do triângulo:");
        lado1 = sc.nextInt();
        System.out.println("Digite o valor do segundo lado do triângulo:");
        lado2 = sc.nextInt();
        System.out.println("Digite o valor do terceiro lado do triângulo:");
        lado3 = sc.nextInt();
        permissao = EhTriangulo(lado1, lado2, lado3);
        if(permissao == true){
            String tipo = TipoTriangulo(lado1, lado2, lado3);
            System.out.printf("O triângulo é: %s", tipo);
        }else{
            System.out.println("Não é possível formar um triângulo!");
        }
        sc.close();

    }

    public static boolean EhTriangulo(int a, int b, int c){
        if(a < b + c && b < a + c && c < a + b){
            return true;
        }else{
            return false;
        }
    }
    public static String TipoTriangulo( int a, int b, int c){
        if( a == b && b == c){
            return "Equilátero";
        } else if( a == b || b == c || a == c){
            return "Isósceles";
        } else {
            return "Escaleno";
        }
    }
}
    

