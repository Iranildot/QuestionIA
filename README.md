# QuestionIA
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


### Temas do app

O aplicativo tem temas imbutidos para poder estilizar o aplicativo ao seu gosto. Confiram os modelos a seguir!

#### Darkly (default)
![estilo darkly](https://github.com/Iranildot/QuestionIA/assets/68133032/960bb8d4-e607-46bc-a234-20348057774d)

#### Superhero
![estilo superhero](https://github.com/Iranildot/QuestionIA/assets/68133032/333989c9-524f-4067-b90a-4c853f66bd06)

#### Solar
![estilo solar](https://github.com/Iranildot/QuestionIA/assets/68133032/b5955c88-64b4-49b1-82d0-18ef22ad6ab1)

#### Cyborg
![estilo cyborg](https://github.com/Iranildot/QuestionIA/assets/68133032/8ce4024f-31ab-4bec-b78e-d626e5e3bc13)

#### Vapor
![estilo vapor](https://github.com/Iranildot/QuestionIA/assets/68133032/2fc4d786-01fb-461c-8b54-a0d5826ab99b)

