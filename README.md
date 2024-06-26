# QuestionIA
## Sumário
- [Explicação do programa](https://github.com/Iranildot/QuestionIA/blob/master/README.md#explica%C3%A7%C3%A3o-do-programa)
- [Conhecendo o programa](https://github.com/Iranildot/QuestionIA/blob/master/README.md#conhecendo-o-programa)
  - [Interface](https://github.com/Iranildot/QuestionIA/blob/master/README.md#interface)
     - [Configurações de perguntas](https://github.com/Iranildot/QuestionIA/blob/master/README.md#interface)
     - [Configurações do Gemini](https://github.com/Iranildot/QuestionIA/blob/master/README.md#configura%C3%A7%C3%B5es-do-gemini)
     - [Janela de saída](https://github.com/Iranildot/QuestionIA/blob/master/README.md#janela-de-sa%C3%ADda)
  - [Temas do app](https://github.com/Iranildot/QuestionIA/blob/master/README.md#temas-do-app)
    - [Darkly (default)](https://github.com/Iranildot/QuestionIA/blob/master/README.md#darkly-default)
    - [Superhero](https://github.com/Iranildot/QuestionIA/blob/master/README.md#superhero)
    - [Solar](https://github.com/Iranildot/QuestionIA/blob/master/README.md#solar)
    - [Cyborg](https://github.com/Iranildot/QuestionIA/blob/master/README.md#cyborg)
    - [Vapor](https://github.com/Iranildot/QuestionIA/blob/master/README.md#vapor)
  - [Fontes do app](https://github.com/Iranildot/QuestionIA/blob/master/README.md#fontes-do-app)
    - [Meera (default)](https://github.com/Iranildot/QuestionIA/blob/master/README.md#meera-default)
    - [Purisa](https://github.com/Iranildot/QuestionIA/blob/master/README.md#purisa)
    - [Chilanka](https://github.com/Iranildot/QuestionIA/blob/master/README.md#chilanka)
  - [Testes do programa](https://github.com/Iranildot/QuestionIA/blob/master/README.md#testes-do-programa)
    - [Teste 1](https://github.com/Iranildot/QuestionIA/blob/master/README.md#teste-1)
    - [Teste 2](https://github.com/Iranildot/QuestionIA/blob/master/README.md#teste-2)
    - [Teste 3](https://github.com/Iranildot/QuestionIA/blob/master/README.md#teste-3)
    - [Teste 4](https://github.com/Iranildot/QuestionIA/blob/master/README.md#teste-4)
    - [Teste 5](https://github.com/Iranildot/QuestionIA/blob/master/README.md#teste-5)
  - [Mostrando na prática (vídeo)](https://github.com/Iranildot/QuestionIA/blob/master/README.md#mostrando-na-pr%C3%A1tica-v%C3%ADdeo)

## Explicação do programa

QuestionIA é programa GUI contruido em Python que usa a biblioteca Tkinter com a biblioteca Ttkbootstrap (Fornece interface moderna) e também faz uso da API do Gemini. Esse programa serve para fornecer modelos de questões para as mais diversas disciplinas (Matemática, Português, Ciências, ...) a depender do ano escolar informado (1º, 2º, 3º, ..., 9º ano do ensino fundamental, 1º, 2º e 3º ano do ensino médio). Com o objetivo de auxiliar os professores na hora da criação das listas de exercícios.

## Conhecendo o programa
### Interface
#### Configurações de perguntas

Esta página do programa permite ao usuário configurar as opções: 
- **ANO:** Se refere ao ano escolar dos estudates (1º, 2º, 3º, ..., 9º ano do ensino fundamental, 1º, 2º e 3º ano do ensino médio)
- **MATÉRIA:** São as disciplinas das quais a IA gerará as questões (Português, Inglês, Espanhol, ...)
- **ASSUNTO:** Se refere aos assunto de uma dada disciplina que será utilizado para gerar o conteúdo (por exemplo: matéria=matemática, assunto=frações)
- **QUANTIDADE DE QUESTÕES:** É a quantidade de questões que a LLM vai gerar (limite mínimo = 1, limite máximo = 20)

  **OBS:** Os botões de buscar que há próximos aos campos de matéria e assunto servem pra auxiliar no preencimento dos campos e a ajuda é fornecida pelo Gemini.

![estilo darkly](https://github.com/Iranildot/QuestionIA/assets/68133032/fc96d3dd-a784-4fe2-9d35-40ac8dda6633)

#### Configurações do Gemini

Nas configurações do Gemini (no GUI) foi adicionado apenas o local para inserir API KEY para realizar a comunicação com o Gemini. O widget de entrada está configurado para mostrar apenas "*" não importando a entrada, para poder manter API KEY visualmente escondida.

![imagem do imput de API KEY](https://github.com/Iranildot/QuestionIA/assets/68133032/14881a6f-ac00-483b-b8e6-bad67e2e8219)

Enquanto que as configurações no Backend são:

![Preparando o modelo](https://github.com/Iranildot/QuestionIA/assets/68133032/b7261e18-d0a3-4e4b-bbcd-5e68dc8352a0)

#### Janela de saída

A janela de saída tem um botão para gerar os conteúdos e mostrar a saída (as respostas do Gemini) em um widget de texto.

![página de output](https://github.com/Iranildot/QuestionIA/assets/68133032/f56e13d7-7a82-4a4b-b504-5fd4af9018bd)


## Temas do app

O aplicativo tem temas imbutidos para poder estilizar o aplicativo ao seu gosto. Confiram os modelos a seguir!

### Darkly (default)
![estilo darkly](https://github.com/Iranildot/QuestionIA/assets/68133032/960bb8d4-e607-46bc-a234-20348057774d)

### Superhero
![estilo superhero](https://github.com/Iranildot/QuestionIA/assets/68133032/333989c9-524f-4067-b90a-4c853f66bd06)

### Solar
![estilo solar](https://github.com/Iranildot/QuestionIA/assets/68133032/b5955c88-64b4-49b1-82d0-18ef22ad6ab1)

### Cyborg
![estilo cyborg](https://github.com/Iranildot/QuestionIA/assets/68133032/8ce4024f-31ab-4bec-b78e-d626e5e3bc13)

### Vapor
![estilo vapor](https://github.com/Iranildot/QuestionIA/assets/68133032/2fc4d786-01fb-461c-8b54-a0d5826ab99b)


## Fontes do app
O aplicativo tem fontes disponibilizadas pela biblioteca Tkinter para poder estilizar o aplicativo ao seu gosto. Confiram os modelos a seguir!

### Meera (default)
![Questões sobre filosofia](https://github.com/Iranildot/QuestionIA/assets/68133032/98e77d00-1e34-42f1-8a18-0e5f1b832529)

### Purisa
![puriza font](https://github.com/Iranildot/QuestionIA/assets/68133032/3b9528e0-4de5-4ee6-b5b6-9919f8cb08de)

### Chilanka
![chilanka font](https://github.com/Iranildot/QuestionIA/assets/68133032/d2bf432f-f724-499e-bde0-5649bb008735)

## Testes do programa

### Teste 1

#### Input
Para o teste 1 foram inseridas as seguintes configurações
- **ANO:** 6º ano do ensino fundamental
- **MATÉRIA:** Português
- **ASSUNTO:** Gramática
- **QUANTIDADE DE QUESTÕES:** 10

#### Output
![6 ano portugûes gramática](https://github.com/Iranildot/QuestionIA/assets/68133032/295e0664-2c75-4982-ab70-c9042859c295)

### Teste 2

#### Input
Para o teste 2 foram inseridas as seguintes configurações
- **ANO:** 3º do ensino médio
- **MATÉRIA:** Espanol
- **ASSUNTO:** Completar a conjugação correta dos verbos
- **QUANTIDADE DE QUESTÕES:** 20

#### Output
![Espanol do 3 ano ensino médio](https://github.com/Iranildot/QuestionIA/assets/68133032/f687f365-4129-438a-86ab-7244a6de3a8e)

### Teste 3

#### Input
Para o teste 3 foram inseridas as seguintes configurações
- **ANO:** 1º do ensino médio
- **MATÉRIA:** Inglês
- **ASSUNTO:** Gramática
- **QUANTIDADE DE QUESTÕES:** 10

#### Output
![inglês gramática 1 ano ensino medio](https://github.com/Iranildot/QuestionIA/assets/68133032/59397f96-87a8-4eee-b93f-614bc92782ec)

### Teste 4

#### Input
Para o teste 4 foram inseridas as seguintes configurações
- **ANO:** 3º do ensino médio
- **MATÉRIA:** Matemática
- **ASSUNTO:** Álgebra
- **QUANTIDADE DE QUESTÕES:** 10

#### Output
![matemática 3 ano ensino medio](https://github.com/Iranildot/QuestionIA/assets/68133032/67469b57-3eb8-4dba-9513-332530f6f410)

### Teste 5

#### Input
Para o teste 5 foram inseridas as seguintes configurações
- **ANO:** 3º do ensino médio
- **MATÉRIA:** Filosofia
- **ASSUNTO:** Filosofia da ciência
- **QUANTIDADE DE QUESTÕES:** 10

#### Output
![Questões sobre filosofia](https://github.com/Iranildot/QuestionIA/assets/68133032/1f07415a-32c8-47bd-8e2f-b97fcba85406)

## Mostrando na prática (vídeo)


https://github.com/Iranildot/QuestionIA/assets/68133032/4b66498f-fff4-4561-b5c9-48ffbebe8e10


**OBS:** Não se preocupem, a chave foi deletada ao final do vídeo!
