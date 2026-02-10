import java.util.Scanner;
public class Preços {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double[] preços = new double[10];
        double[] preçosp = new double[10];
        double[] preçosg = new double[10];
        for(int i = 0; i < preços.length;i++){
            System.out.println("Digite os preços de 10 produtos:");
            preços[i] = sc.nextDouble();
            if(preços[i] > 100){
                preçosg[i] = preços[i]; 
            }else{
                preçosp[i] = preços[i];
            }
        }
        System.out.println("Analisando os produtos caros:");
        produtosCaros(preçosg);
        System.out.println("Analisando os produtos baratos:");
        produtosBaratos(preçosp);
        sc.close();
    }
    public static void produtosCaros(double[] precos){
        for(int i = 0; i < precos.length; i++){
            if(precos[i] != 0){
                System.out.printf("Preço: R$ %.2f\n", precos[i]);
                if(precos[i] >= 300){
                    System.out.println("Produto Premium");
                }else{
                    System.out.println("Produto Intermediário");
                }
            }
        }
    }
    public static void produtosBaratos(double[] precos1){
        int contador = 0;
        double soma = 0;
        for(int i = 0; i < precos1.length; i++){
            if(precos1[i] != 0){
                System.out.printf("Preço: R$ %.2f\n", precos1[i]);
                soma += precos1[i];
                contador++;
                if(precos1[i] < 50){
                    System.out.println("Preço Popular");
                }else{
                    System.out.println("Preço Acessível");}
           } 
        }
        double média = soma / contador;
        System.out.printf("Número de produtos baratos: %d\n", contador);
        System.out.printf("Média dos preços baratos: R$ %.2f\n", média);
    }
}
