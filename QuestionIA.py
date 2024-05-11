from tkinter import *
from tkinter import font
import ttkbootstrap as ttkb
from ttkbootstrap.toast import ToastNotification
import google.generativeai as genai

class App():
    def __init__(self) -> None:

        # CREATING A WINDOW WIDGET
        self.root = ttkb.Window(title="QuestionIA")

        # DEFINING A VARIABLES
        self.font_family = "Meera"

        # SETTING APP STYLE (THEME AND FONT)
        self.style = ttkb.Style(theme="darkly")
        self.style.configure('TLabelframe.Label', font=(self.font_family, 18, "bold"))
        self.style.configure('TNotebook.Tab', font=(self.font_family, 15, "bold"))
        self.style.configure('TButton', font=(self.font_family, 15, "bold"))

        # EDITTING WINDOW SETTINGS
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # CALLING THE INTERFACE METHOD
        self.interface()
        
        self.root.mainloop()

    # CREATING THE APP INTERFACE
    def interface(self):
        # CREATING A MAIN FRAME
        self.main_frame = ttkb.Frame(self.root, style="success", padding=15)
        self.main_frame.grid(sticky="NSEW")
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        # CREATING A SECOND FRAME
        self.second_frame = ttkb.Frame(self.main_frame)
        self.second_frame.grid(sticky="NSEW")
        self.second_frame.rowconfigure(0, weight=1)
        self.second_frame.columnconfigure(1, weight=1)

        # CREATING A DRAWER
        self.left_drawer = ttkb.Frame(self.second_frame)
        self.left_drawer.grid(row=0, column=0, sticky=NS)
        self.left_drawer.rowconfigure(0, weight=1)

        # SHOWING THE APP NAME
        self.app_title = ttkb.Label(self.left_drawer, text="QuestionIA", font=("purisa", 30), padding=(30, 50, 30, 10))
        self.app_title.grid(row=0, column=0, sticky=N)

        # ADDING A LABELFRAME TO THE THEME CHOOSER
        self.theme_chooser_labelframe = ttkb.LabelFrame(self.left_drawer, text="Theme", border=8)
        self.theme_chooser_labelframe.grid(pady=(0, 30))

        # CREATING A COMBOBOX (THE THEME CHOOSER)
        self.theme_chooser = ttkb.Combobox(self.theme_chooser_labelframe, values=["darkly", 
                                                                         "superhero", 
                                                                         "solar", 
                                                                         "cyborg", 
                                                                         "vapor"], 
                                                                         style="success")
        self.theme_chooser.insert(0, "darkly")
        self.theme_chooser["state"] = "readonly"

        # BINDING A VIRTUAL EVENT TO THE COMBOBOX
        self.theme_chooser.bind("<<ComboboxSelected>>", self.set_theme)
        self.theme_chooser.grid(row=0, column=0, sticky=S)

        # ADDING A LABELFRAME TO THE THEME CHOOSER
        self.font_chooser_labelframe = ttkb.LabelFrame(self.left_drawer, text="Font", border=8)
        self.font_chooser_labelframe.grid(pady=(0, 30))

        # CREATING A COMBOBOX (THE THEME CHOOSER)
        self.font_chooser = ttkb.Combobox(self.font_chooser_labelframe, values=font.families(),
                                                                         style="success")
        self.font_chooser.insert(0, self.font_family)
        self.font_chooser["state"] = "readonly"

        # BINDING A VIRTUAL EVENT TO THE COMBOBOX
        self.font_chooser.bind("<<ComboboxSelected>>", self.set_font)
        self.font_chooser.grid(row=0, column=0, sticky=S)

        # CREATING THE DASHBOARD FRAME
        self.dashboard_frame = ttkb.Frame(self.second_frame, padding=30, style="dark")
        self.dashboard_frame.grid(row=0, column=1, sticky=NSEW)
        self.dashboard_frame.rowconfigure(0, weight=1)
        self.dashboard_frame.columnconfigure(0, weight=1)
        
        # CREATING A NOTEBOOK
        self.notebook = ttkb.Notebook(self.dashboard_frame, bootstyle="success")

        self.questions_settings_elements()
        self.gemini_settings_elements()
        self.output_elements()

        self.notebook.grid(sticky=NSEW)
    
    def questions_settings_elements(self):
        # QUESTIONS SETTINGS FRAME
        self.questions_settings_frame = ttkb.Frame(self.notebook, padding=(0, 20))
        self.questions_settings_frame.rowconfigure(0, weight=1)
        self.questions_settings_frame.columnconfigure(0, weight=1)

        # ADDING TAB TO THE NOTEBOOK
        self.notebook.add(self.questions_settings_frame, sticky=NSEW, text="QUESTION SETTINGS")

        self.questions_settings_second_frame = ttkb.Frame(self.questions_settings_frame, padding=(0, 20))
        self.questions_settings_second_frame.grid()

        # FIRST TAB (QUESTION SETTINGS)
        self.grade_labelframe = ttkb.LabelFrame(self.questions_settings_second_frame, text="Ano", border=8)
        self.grade_labelframe.grid(pady=(0, 30))
        self.grade_combobox = ttkb.Combobox(self.grade_labelframe, 
                                            width=50, 
                                            values=[str(ano + 1) + "º ano do ensino fundamental" for ano in range(9)] + [str(ano + 1) + "º ano do ensino médio" for ano in range(3)], 
                                            state="readonly",
                                            style="success")
        self.grade_combobox.grid()

        # SUBJECT
        self.subject_labelframe = ttkb.LabelFrame(self.questions_settings_second_frame, text="Matéria", border=8)
        self.subject_labelframe.grid(pady=(0, 30))
        self.subject_combobox = ttkb.Combobox(self.subject_labelframe, 
                                              width=50, 
                                              state="readonly",
                                              style="success")
        self.subject_combobox.grid()

        ttkb.Button(self.subject_labelframe, text="Buscar", style="success", command=self.get_subject_options).grid(row=0, padx=(10, 0), column=1)

        # TOPICS
        self.topics_labelframe = ttkb.LabelFrame(self.questions_settings_second_frame, text="Assunto", border=8)
        self.topics_labelframe.grid(pady=(0, 30))
        self.topics_combobox = ttkb.Combobox(self.topics_labelframe, 
                                              width=50, 
                                              state="readonly",
                                              style="success")
        self.topics_combobox.grid()

        ttkb.Button(self.topics_labelframe, text="Buscar", style="success", command=self.get_topics_options).grid(row=0, padx=(10, 0), column=1)

        # AMOUNT OF QUESTIONS
        self.amount_questions_labelframe = ttkb.LabelFrame(self.questions_settings_second_frame, text="Número de questões", border=8)
        self.amount_questions_labelframe.grid(pady=(0, 30))
        self.amount_questions_combobox = ttkb.Combobox(self.amount_questions_labelframe, 
                                                       width=50, 
                                                       values=[(amount + 1) for amount in range(20)], 
                                                       state="readonly",
                                                       style="success")
        self.amount_questions_combobox.grid()

        self.grade_combobox["state"] = DISABLED
        self.topics_combobox["state"] = DISABLED
        self.subject_combobox["state"] = DISABLED
        self.amount_questions_combobox["state"] = DISABLED

    def get_subject_options(self):
        subject_options = self.get_response_from_gemini(f"Liste todas as disciplinas do {self.grade_combobox.get()}. Siga o exemplo:\n\n'1º ano do ensino fundamental'\nPortugês\nMatemática\n...").split("\n")
        subject_options = [options.replace("*", "").strip() for options in subject_options]
        
        try:
            subject_options.remove("")
            subject_options.remove(" ")
        except:
            pass

        aux = []
        for i in range(len(subject_options)):
            if len(subject_options[i]) <= 15:
                aux.append(subject_options[i])
        
        self.subject_combobox["values"] = aux
        

    def get_topics_options(self):
        topics_options = self.get_response_from_gemini(f"Liste os conteúdos da disciplina {self.subject_combobox.get()} do {self.grade_combobox.get()}. Siga o exemplo:\n\n'Matemática do 6º do ensino fundamental'\n\nFrações\nÁgebra\n(continuação)").split("\n")
        topics_options = [options.replace("*", "").strip() for options in topics_options]
        
        self.topics_combobox["values"] = topics_options

    def gemini_settings_elements(self):
        # GEMINI SETTINGS FRAME
        self.gemini_settings_frame = ttkb.Frame(self.notebook)
        self.gemini_settings_frame.rowconfigure(0, weight=1)
        self.gemini_settings_frame.columnconfigure(0, weight=1)

        # ADDING TAB TO THE NOTEBOOK
        self.notebook.add(self.gemini_settings_frame, sticky=NSEW, text="GEMINI SETTINGS")

        # SUBJECT
        self.api_key_labelframe = ttkb.LabelFrame(self.gemini_settings_frame, text="API KEY", border=8)
        self.api_key_labelframe.grid(pady=(0, 50))
        self.api_key_entry = ttkb.Entry(self.api_key_labelframe, 
                                        width=50, 
                                        show="*",
                                        style="success")
        self.api_key_entry.grid()

        ttkb.Button(self.api_key_labelframe, text="Conectar", style="success", command=self.active_questions_settings_comboboxes).grid(row=0, padx=(10, 0), column=1)
    
    def active_questions_settings_comboboxes(self):
        try:
            self.start_gemini(self.api_key_entry.get())

            # IT GIVE USER PERMISION TO USE OPTIONS 
            self.grade_combobox["state"] = "readonly"
            self.topics_combobox["state"] = NORMAL
            self.subject_combobox["state"] = NORMAL
            self.amount_questions_combobox["state"] = "readonly"

            # POP UP A MESSAGE SAYING THAT EVERYTHING IS OK
            toast = ToastNotification(
                title="GEMINI",
                message="Conexão com o Gemini realizada com sucesso.",
                duration=5000,
                position=(0, 50, "s")
            )
            toast.show_toast()

        except:
            # IT DON'T GIVE USER PERMISION TO USE OPTIONS 
            self.grade_combobox["state"] = DISABLED
            self.topics_combobox["state"] = DISABLED
            self.subject_combobox["state"] = DISABLED
            self.amount_questions_combobox["state"] = DISABLED
            
            # POP UP A MESSAGE SAYING THAT OUCCURS AN ERROR
            toast = ToastNotification(
                title="GEMINI",
                message="Falha ao tentar se conectar ao Gemini.",
                duration=5000,
                position=(0, 50, "s")
            )
            toast.show_toast()

    def output_elements(self):
        # OUTPUT FRAME
        self.output_frame = ttkb.Frame(self.notebook)
        self.output_frame.rowconfigure(0, weight=1)
        self.output_frame.columnconfigure(0, weight=1)

        # ADDING TAB TO THE NOTEBOOK
        self.notebook.add(self.output_frame, sticky=NSEW, text="OUTPUT")

        # CREATING A TEXT BOX TO SHOW THE QUESTIONS AND ANSWERS
        self.text = ttkb.Text(self.output_frame, font=(self.font_family, 18))
        self.text.grid(row=0, column=0, sticky=NSEW)

        self.buttons_frame = ttkb.Frame(self.output_frame, padding=(0, 2))
        self.buttons_frame.grid(sticky=EW)

        self.generate_questions_button = ttkb.Button(self.buttons_frame, text="Gerar questões", bootstyle="success", command=self.generate_questions).grid()
    
    def generate_questions(self):
        self.text.delete(1.0, END)

        response = self.get_response_from_gemini(f"Crie {self.amount_questions_combobox.get()} questões de {self.subject_combobox.get()} com o assunto {self.topics_combobox.get()} do {self.grade_combobox.get()}. Não forneça o gabarito. Não estilize o texto. Gere questões complexas e bem diferentes das anteriores.")
        
        self.text.insert(1.0, response + "\n\n")

    # EVENT TO SET THE APP THEME
    def set_theme(self, event):
        self.style = ttkb.Style(theme=self.theme_chooser.get())
        self.style.configure('TLabelframe.Label', font=(self.font_family, 18, "bold"))
        self.style.configure('TNotebook.Tab', font=(self.font_family, 15, "bold"))
        self.style.configure('TButton', font=(self.font_family, 15, "bold"))
        self.text["font"] = (self.font_family, 18, "bold")

    
    # EVENT TO SET THE APP FONT
    def set_font(self, event):
        self.font_family = self.font_chooser.get()
        self.style = ttkb.Style(theme=self.theme_chooser.get())
        self.style.configure('TLabelframe.Label', font=(self.font_family, 18, "bold"))
        self.style.configure('TNotebook.Tab', font=(self.font_family, 15, "bold"))
        self.style.configure('TButton', font=(self.font_family, 15, "bold"))
        self.text["font"] = (self.font_family, 18, "bold")

    # TO INITIALIZE GEMINI
    def start_gemini(self, api_key):
        genai.configure(api_key=api_key)

        # Set up the model
        self.generation_config = {
            "temperature": 1,
            "top_p": 1,
            "top_k": 0,
            "max_output_tokens": 2048,
        }

        self.safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        ]

        self.model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                           generation_config=self.generation_config,
                                           safety_settings=self.safety_settings)

        self.chat = self.model.start_chat(history=[])
        self.chat.send_message("Isso é só um teste")

    # GET RESPONSES FROM GEMINI
    def get_response_from_gemini(self, input):
        self.chat.send_message(input)
        return self.chat.last.text

if __name__ == "__main__":
    App()
