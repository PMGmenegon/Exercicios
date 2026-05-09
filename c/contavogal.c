//este código terá uma função a qual contará as vogais de uma string na main//
#include <stdio.h>
#include <ctype.h>
#include <string.h>
void contaVogal(char p[50]){
    int contador = 0;
    for(int i=0;i<50;i++){
        if (tolower(p[i])=='a' || tolower(p[i]) =='e'|| tolower(p[i]) == 'i' || tolower(p[i]) == 'u' || tolower(p[i]) == 'o'){
            contador++;
        }
    }
    printf("Total de vogais = %d", contador);
}
////////////MAIN/////////////
int main(){
    char frase[50];
    printf("Digite uma frase até 50 caracteres: ");
    fgets(frase,50,stdin);
    contaVogal(frase);
}