import java.util.Scanner;
public class VerificandoSenha {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String senha;
        boolean entrada;
        System.out.println("Digite a senha:");
        senha = sc.nextLine();
        entrada = verificarSenha(senha.toLowerCase());
        if(entrada){
            System.out.println("Acesso permitido!");
        }else{
            System.out.println("Acesso negado!");
        }
        sc.close();
    }

    public static boolean verificarSenha(String tentativa){
        if(tentativa.equals("java123")){
            return true;
        }else{
            return false;
        }
    }
}  
