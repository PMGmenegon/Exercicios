public class Gastos{
    public static void main(String[] args){
        int g1,g2,g3,m, t;
        g1 = 15000;
        g2 = 23000;
        g3 = 17000;
        m = (g1 + g2 + g3) / 3;
        t = g1 + g2 + g3;
        System.out.printf("Gasto total: %d\nGasto médio: %d", t, m);
    }
}