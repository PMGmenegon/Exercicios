//Nesse código faremos uma matriz trabalhando pela primeira vez com a função malloc//
#include <stdio.h>
#include <stdlib.h>
void criaMatriz(){
    int **p, l, c;
    printf("Digite o número de linhas da sua matriz: ");
    scanf("%d", &l);
    printf("Digite o número de colunas da sua matriz: ");
    scanf("%d", &c);
    p = (int**)malloc(c* sizeof(int*));
    if (p!=NULL){
        printf("Memória alocada");
    }
    else{
        printf("Armazenamento esgotado");
    }
    for (int i=0; i < c; i++){
        p[i] = (int*)malloc(l* sizeof(int));
        if(p[i]!=NULL){
            printf("Memória alocada");
        }
        else{
            printf("Armazenamento esgotado");
        }
    }
    for(int i=0;i<l;i++){
        for(int j = 0;j<c;j++){
            printf("Digite um número: ");
            scanf("%d", &p[j][i]);
        }
    }
    printf("Matriz:\n");
    for(int i=0;i<l;i++){
        for(int j = 0;j<c;j++){
            printf("%d ", p[j][i]);
        }
        printf("\n");
    }
    for(int i = i-1;i>=0;i--){
        free(p[i]);
    }
    free(p);
}
///////////MAIN////////////
int main(){
    criaMatriz();
}