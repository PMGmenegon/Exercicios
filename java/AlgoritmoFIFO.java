import java.util.Scanner;
public class AlgoritmoFIFO {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String mensagem;
        boolean continuar = true;
        String[] historico = new String[5];
        while(continuar){
            System.out.println("Digite uma mensagem (ou 'sair' para enecerrar):");
            mensagem = sc.nextLine();
            if(mensagem.equals("sair")) {
                continuar = false;
            }else{
                for(int i = 0; i < historico.length - 1; i++){
                    historico[i] = historico[i + 1];
                }
                historico[historico.length - 1] = mensagem;
            }
            System.out.println("Histórico de mensagens:");
            for(int i = 0; i < historico.length; i++){
                if(historico[i] != null){
                    System.out.println(historico[i]);
                }
            }
        }
        sc.close();
    }
}
