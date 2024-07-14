# QuestionIA
## Summary
- [Program Explanation](https://github.com/Iranildot/QuestionIA/blob/master/README.md#program-explanation)
- [Getting to Know the Program](https://github.com/Iranildot/QuestionIA/blob/master/README.md#getting-to-know-the-program)
  - [Interface](https://github.com/Iranildot/QuestionIA/blob/master/README.md#interface)
     - [Question Settings](https://github.com/Iranildot/QuestionIA/blob/master/README.md#question-settings)
     - [Gemini Settings](https://github.com/Iranildot/QuestionIA/blob/master/README.md#gemini-settings)
     - [Output Window](https://github.com/Iranildot/QuestionIA/blob/master/README.md#output-window)
  - [App Themes](https://github.com/Iranildot/QuestionIA/blob/master/README.md#app-themes)
    - [Darkly (default)](https://github.com/Iranildot/QuestionIA/blob/master/README.md#darkly-default)
    - [Superhero](https://github.com/Iranildot/QuestionIA/blob/master/README.md#superhero)
    - [Solar](https://github.com/Iranildot/QuestionIA/blob/master/README.md#solar)
    - [Cyborg](https://github.com/Iranildot/QuestionIA/blob/master/README.md#cyborg)
    - [Vapor](https://github.com/Iranildot/QuestionIA/blob/master/README.md#vapor)
  - [App Fonts](https://github.com/Iranildot/QuestionIA/blob/master/README.md#app-fonts)
    - [Meera (default)](https://github.com/Iranildot/QuestionIA/blob/master/README.md#meera-default)
    - [Purisa](https://github.com/Iranildot/QuestionIA/blob/master/README.md#purisa)
    - [Chilanka](https://github.com/Iranildot/QuestionIA/blob/master/README.md#chilanka)
  - [Program Tests](https://github.com/Iranildot/QuestionIA/blob/master/README.md#program-tests)
    - [Test 1](https://github.com/Iranildot/QuestionIA/blob/master/README.md#test-1)
    - [Test 2](https://github.com/Iranildot/QuestionIA/blob/master/README.md#test-2)
    - [Test 3](https://github.com/Iranildot/QuestionIA/blob/master/README.md#test-3)
    - [Test 4](https://github.com/Iranildot/QuestionIA/blob/master/README.md#test-4)
    - [Test 5](https://github.com/Iranildot/QuestionIA/blob/master/README.md#test-5)
  - [Demonstration (video)](https://github.com/Iranildot/QuestionIA/blob/master/README.md#demonstration-video)

## Program Explanation

QuestionIA is a GUI program built in Python that uses the Tkinter library with Ttkbootstrap (providing a modern interface) and also makes use of the Gemini API. This program provides question templates for various subjects (Mathematics, Portuguese, Science, ...) depending on the school year selected (1st, 2nd, 3rd, ..., 9th grade of elementary school, 1st, 2nd, and 3rd year of high school). It aims to assist teachers in creating exercise lists.

## Getting to Know the Program
### Interface
#### Question Settings

This section of the program allows the user to configure the following options:
- **YEAR**: Refers to the students' school year (1st, 2nd, 3rd, ..., 9th grade of elementary school, 1st, 2nd, and 3rd year of high school)
- **SUBJECT**: The subjects from which the AI will generate questions (Portuguese, English, Spanish, ...)
- **TOPIC**: Refers to the topic of a given subject that will be used to generate content (e.g., subject=Mathematics, topic=fractions)
- **NUMBER OF QUESTIONS**: The number of questions the AI will generate (minimum limit = 1, maximum limit = 20)

  **NOTE**: The search buttons next to the subject and topic fields are used to assist in filling out the fields, with help provided by Gemini.


![estilo darkly](https://github.com/Iranildot/QuestionIA/assets/68133032/fc96d3dd-a784-4fe2-9d35-40ac8dda6633)

#### Gemini Settings

In the Gemini settings (in the GUI), only the place to enter the API KEY for communicating with Gemini has been added. The input widget is configured to display only "*", regardless of the input, to visually hide the API KEY.

![imagem do imput de API KEY](https://github.com/Iranildot/QuestionIA/assets/68133032/14881a6f-ac00-483b-b8e6-bad67e2e8219)

While the settings in the Backend are:

![Preparando o modelo](https://github.com/Iranildot/QuestionIA/assets/68133032/b7261e18-d0a3-4e4b-bbcd-5e68dc8352a0)

#### Output Window

The output window has a button to generate the content and display the output (Gemini's responses) in a text widget.

![página de output](https://github.com/Iranildot/QuestionIA/assets/68133032/f56e13d7-7a82-4a4b-b504-5fd4af9018bd)

## App Themes

The application has built-in themes to customize the app to your liking. Check out the following styles!

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

## App Fonts
The application offers fonts provided by the Tkinter library to customize the app to your liking. Check out the following styles!

### Meera (default)
![Questões sobre filosofia](https://github.com/Iranildot/QuestionIA/assets/68133032/98e77d00-1e34-42f1-8a18-0e5f1b832529)

### Purisa
![puriza font](https://github.com/Iranildot/QuestionIA/assets/68133032/3b9528e0-4de5-4ee6-b5b6-9919f8cb08de)

### Chilanka
![chilanka font](https://github.com/Iranildot/QuestionIA/assets/68133032/d2bf432f-f724-499e-bde0-5649bb008735)

## Program Tests

### Test 1

#### Input
For test 1, the following configurations were entered:
- **YEAR**: 6th grade of elementary school
- **SUBJECT**: Portuguese
- **TOPIC**: Grammar
- **NUMBER OF QUESTIONS**: 10

#### Output
![6 ano portugûes gramática](https://github.com/Iranildot/QuestionIA/assets/68133032/295e0664-2c75-4982-ab70-c9042859c295)

### Test 2

#### Input
For test 2, the following configurations were entered:
- **YEAR**: 3rd year of high school
- **SUBJECT**: Spanish
- **TOPIC**: Conjugation
- **NUMBER OF QUESTIONS**: 20

#### Output
![Espanol do 3 ano ensino médio](https://github.com/Iranildot/QuestionIA/assets/68133032/f687f365-4129-438a-86ab-7244a6de3a8e)

### Test 3

#### Input
For test 3, the following configurations were entered:
- **YEAR**: 2nd year of high school
- **SUBJECT**: Chemistry
- **TOPIC**: Periodic Table
- **NUMBER OF QUESTIONS**: 8

#### Output
![inglês gramática 1 ano ensino medio](https://github.com/Iranildot/QuestionIA/assets/68133032/59397f96-87a8-4eee-b93f-614bc92782ec)

### Test 4

#### Input
For test 4, the following configurations were entered:
- **YEAR**: 5th grade of elementary school
- **SUBJECT**: Mathematics
- **TOPIC**: Geometry
- **NUMBER OF QUESTIONS**: 12

#### Output
![matemática 3 ano ensino medio](https://github.com/Iranildot/QuestionIA/assets/68133032/67469b57-3eb8-4dba-9513-332530f6f410)

### Test 5

#### Input
For test 5, the following configurations were entered:
- **YEAR**: 9th grade of elementary school
- **SUBJECT**: History
- **TOPIC**: French Revolution
- **NUMBER OF QUESTIONS**: 15

#### Output
![Questões sobre filosofia](https://github.com/Iranildot/QuestionIA/assets/68133032/1f07415a-32c8-47bd-8e2f-b97fcba85406)

## Demonstration (video)

Here you can see how the program works in practice through the provided video.

https://github.com/Iranildot/QuestionIA/assets/68133032/4b66498f-fff4-4561-b5c9-48ffbebe8e10

**NOTE**: Don't worry, the key was deleted at the end of the video!
