import java.util.Random;
public class BrincandoComMatrizes {
    public static void main(String[] args){
        int[][] matrizB = {
            {2, -3, 5},
            {-1, 4, 0},
            {7, 8, -6},
            {9, -2, 1},
        }; 
        int[][] matrizA = new int[4][3];
        int[][] matrizS = new int[4][3];
        int[][] matrizD = new int[4][3];
        int[][] matrizM = new int[4][3];
        Random numeros = new Random();
        for(int i = 0; i < matrizA.length; i++){
            for(int j = 0; j < matrizA[i].length; j++){
                matrizA[i][j] = numeros.nextInt(201) - 100;
                matrizS[i][j] = matrizA[i][j] + matrizB[i][j];
                matrizD[j][i] = matrizA[i][j] - matrizB[i][j];
                matrizM[j][i] = matrizA[i][j] * matrizB[i][j];
            }
        
        }
        System.out.println("Matriz A:");
        for(int i = 0; i < matrizA.length; i++){
            for(int j = 0; j < matrizA[i].length; j++){
                System.out.print(matrizA[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Matriz B:");
        for(int i = 0; i < matrizB.length; i++){
            for(int j = 0; j < matrizB[i].length; j++){
                System.out.print(matrizB[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Matriz Soma:");
        for(int i = 0; i < matrizS.length; i++){
            for(int j = 0; j < matrizS[i].length; j++){
                System.out.print(matrizS[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Matriz Diferença:");
        for(int i = 0; i < matrizD.length; i++){
            for(int j = 0; j < matrizD[i].length; j++){
                System.out.print(matrizD[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Matriz Multiplicação:");
        for(int i = 0; i < matrizM.length; i++){
            for(int j = 0; j < matrizM[i].length; j++){
                System.out.print(matrizM[i][j] + " ");
            }
            System.out.println();
        }
    }
}
