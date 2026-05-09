#include <stdio.h>
#include <string.h>
struct pessoa{
    char primeiro_nome[30];
    int idade;
};
int main(){
    struct pessoa p[1000];
    int continuar = 0;
    int total = 0;
    FILE *arq;
    arq = fopen("dados.txt", "w");
    if (arq == NULL) {
        printf("Erro ao abrir o arquivo\n");
        return 1;
    }
        for(int i=0; i<1000; i++){
            printf("Digite o primeiro nome: ");
            scanf("%s", p[i].primeiro_nome);
            printf("Digite a idade: ");
            scanf("%d", &p[i].idade);
            printf("Digite 1 se quiser adicionar mais pessoas: ");
            scanf("%d", &continuar);
            total++;
            if(continuar!=1){
                break;
            }
        }
        for(int j = 0; j < total; j++){
            fprintf(arq, "nome = %s\nidade = %d\n\n", p[j].primeiro_nome, p[j].idade);
        }
    fclose(arq);
}