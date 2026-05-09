#include <stdio.h>
#include <string.h>
struct pessoa{
    char primeiro_nome[30];
    int idade;
};
int main(){
    struct pessoa p[1000];
    FILE *arq;
    arq = fopen("dados.txt", "r");
    int j = 0;
    while(fscanf(arq, "nome = %s\nidade = %d\n\n", p[j].primeiro_nome, &p[j].idade) != EOF){
        if(p[j].idade > 18){
            printf("%s é maior que 18\n", p[j].primeiro_nome);
        }
        j++;
    }
}