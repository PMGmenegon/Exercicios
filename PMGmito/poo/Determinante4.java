import java.util.Random;

public class Determinante4 {

    public static void main (String[] args){

        int[][] matriz = new int[4][4];
        Random numeros = new Random();
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                matriz[i][j] = numeros.nextInt(10);
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println(); 
        }

        int determinante = determinante(matriz);

        System.out.println("\nDeterminante = " + determinante);
    }
    public static int determinante(int[][] m){

        int n = m.length;

        if(n == 2){
            return m[0][0]*m[1][1] - m[0][1]*m[1][0];
        }

        int det = 0;
        for(int j = 0; j < n; j++){

            int[][] menor = submatriz(m, 0, j);

            int sinal = (j % 2 == 0) ? 1 : -1;

            det += sinal * m[0][j] * determinante(menor);
        }

        return det;
    }
    public static int[][] submatriz(int[][] m, int linhaRem, int colRem){

        int n = m.length;
        int[][] sub = new int[n-1][n-1];

        int r = 0;

        for(int i = 0; i < n; i++){

            if(i == linhaRem) continue;

            int c = 0;

            for(int j = 0; j < n; j++){

                if(j == colRem) continue;

                sub[r][c] = m[i][j];
                c++;
            }

            r++;
        }

        return sub;
    }
}

