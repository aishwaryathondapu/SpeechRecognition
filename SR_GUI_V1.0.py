# Below are the images needed: The package is sys is used for system specific functions and parameters, re for handling the functions in regular
# expression, speech_recognition for handling the speech recognition, googletrans package for the translation and to work with GUI and related
# widgets use the tkinter.ttk and tkinter.
import sys
from tkinter.ttk import Combobox
import re
from tkinter import messagebox
import speech_recognition as sr
from tkinter import *
from googletrans import Translator as gt

# Global variables for error and dictionary to store the key and value of language code and country

speech_languages = {"af-ZA": "Afrikaans (South Africa)", "am-ET": "Amharic (Ethiopia)", "hy-AM": "Armenian (Armenia)",
                    "az-AZ": "Azerbaijani (Azerbaijan)",
                    "id-ID": "Indonesian (Indonesia)", "ms-MY": "Malay (Malaysia)", "bn-BD": "Bengali (Bangladesh)",
                    "bn-IN": "Bengali (India)",
                    "ca-ES": "Catalan (Spain)", "cs-CZ": "Czech (Czech Republic)", "da-DK": "Danish (Denmark)",
                    "de-DE": "German (Germany)",
                    "en-AU": "English (Australia)", "en-CA": "English (Canada)", "en-GH": "English (Ghana)",
                    "en-GB": "English (United Kingdom)",
                    "en-IN": "English (India)", "en-IE": "English (Ireland)", "en-KE": "English (Kenya)",
                    "en-NZ": "English (New Zealand)",
                    "en-NG": "English (Nigeria)", "en-PH": "English (Philippines)", "en-SG": "English (Singapore)",
                    "en-ZA": "English (South Africa)",
                    "en-TZ": "English (Tanzania)", "en-US": "English (United States)", "es-AR": "Spanish (Argentina)",
                    "es-BO": "Spanish (Bolivia)",
                    "es-CL": "Spanish (Chile)", "es-CO": "Spanish (Colombia)", "es-CR": "Spanish (Costa Rica)",
                    "es-EC": "Spanish (Ecuador)",
                    "es-SV": "Spanish (El Salvador)", "es-ES": "Spanish (Spain)", "es-US": "Spanish (United States)",
                    "es-GT": "Spanish (Guatemala)",
                    "es-HN": "Spanish (Honduras)", "es-MX": "Spanish (Mexico)", "es-NI": "Spanish (Nicaragua)",
                    "es-PA": "Spanish (Panama)",
                    "es-PY": "Spanish (Paraguay)", "es-PE": "Spanish (Peru)", "es-PR": "Spanish (Puerto Rico)",
                    "es-DO": "Spanish (Dominican Republic)",
                    "es-UY": "Spanish (Uruguay)", "es-VE": "Spanish (Venezuela)", "eu-ES": "Basque (Spain)",
                    "fil-PH": "Filipino (Philippines)",
                    "fr-CA": "French (Canada)", "fr-FR": "French (France)", "gl-ES": "Galician (Spain)",
                    "ka-GE": "Georgian (Georgia)",
                    "gu-IN": "Gujarati (India)", "hr-HR": "Croatian (Croatia)", "zu-ZA": "Zulu (South Africa)",
                    "is-IS": "Icelandic (Iceland)",
                    "it-IT": "Italian (Italy)", "jv-ID": "Javanese (Indonesia)", "kn-IN": "Kannada (India)",
                    "km-KH": "Khmer (Cambodia)",
                    "lo-LA": "Lao (Laos)", "lv-LV": "Latvian (Latvia)", "lt-LT": "Lithuanian (Lithuania)",
                    "hu-HU": "Hungarian (Hungary)",
                    "ml-IN": "Malayalam (India)", "mr-IN": "Marathi (India)", "nl-NL": "Dutch (Netherlands)",
                    "ne-NP": "Nepali (Nepal)",
                    "nb-NO": "Norwegian Bokmål (Norway)", "pl-PL": "Polish (Poland)", "pt-BR": "Portuguese (Brazil)",
                    "pt-PT": "Portuguese (Portugal)",
                    "ro-RO": "Romanian (Romania)", "si-LK": "Sinhala (Sri Lanka)", "sk-SK": "Slovak (Slovakia)",
                    "sl-SI": "Slovenian (Slovenia)",
                    "su-ID": "Sundanese (Indonesia)", "sw-TZ": "Swahili (Tanzania)", "sw-KE": "Swahili (Kenya)",
                    "fi-FI": "Finnish (Finland)",
                    "sv-SE": "Swedish (Sweden)", "ta-IN": "Tamil (India)", "ta-SG": "Tamil (Singapore)",
                    "ta-LK": "Tamil (Sri Lanka)",
                    "ta-MY": "Tamil (Malaysia)", "te-IN": "Telugu (India)", "vi-VN": "Vietnamese (Vietnam)",
                    "tr-TR": "Turkish (Turkey)",
                    "ur-PK": "Urdu (Pakistan)", "ur-IN": "Urdu (India)", "el-GR": "Greek (Greece)",
                    "bg-BG": "Bulgarian (Bulgaria)",
                    "ru-RU": "Russian (Russia)", "sr-RS": "Serbian (Serbia)", "uk-UA": "Ukrainian (Ukraine)",
                    "he-IL": "Hebrew (Israel)",
                    "ar-IL": "Arabic (Israel)", "ar-JO": "Arabic (Jordan)", "ar-AE": "Arabic (United Arab Emirates)",
                    "ar-BH": "Arabic (Bahrain)",
                    "ar-DZ": "Arabic (Algeria)", "ar-SA": "Arabic (Saudi Arabia)", "ar-IQ": "Arabic (Iraq)",
                    "ar-KW": "Arabic (Kuwait)",
                    "ar-MA": "Arabic (Morocco)", "ar-TN": "Arabic (Tunisia)", "ar-OM": "Arabic (Oman)",
                    "ar-PS": "Arabic (State of Palestine)",
                    "ar-QA": "Arabic (Qatar)", "ar-LB": "Arabic (Lebanon)", "ar-EG": "Arabic (Egypt)",
                    "fa-IR": "Persian (Iran)", "hi-IN": "Hindi (India)",
                    "th-TH": "Thai (Thailand)", "ko-KR": "Korean (South Korea)",
                    "zh-TW": "Chinese, Mandarin (Traditional, Taiwan)",
                    "yue-Hant-HK": "Chinese, Cantonese (Traditional, Hong Kong)", "ja-JP": "Japanese (Japan)",
                    "zh-HK": "Chinese, Mandarin (Simplified, Hong Kong)", "zh": "Chinese, Mandarin (Simplified, China)"}
error = "Didn't listened properly."
languages = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
             'az': 'azerbaijani', 'eu': 'basque',
             'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano',
             'ny': 'chichewa',
             'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
             'cs': 'czech',
             'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino',
             'fi': 'finnish', 'fr': 'french',
             'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati',
             'ht': 'haitian creole',
             'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian',
             'is': 'icelandic', 'ig': 'igbo',
             'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada',
             'kk': 'kazakh', 'km': 'khmer',
             'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
             'lt': 'lithuanian',
             'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam',
             'mt': 'maltese', 'mi': 'maori',
             'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian',
             'ps': 'pashto', 'fa': 'persian',
             'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan',
             'gd': 'scots gaelic',
             'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak',
             'sl': 'slovenian',
             'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik',
             'ta': 'tamil', 'te': 'telugu',
             'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese',
             'cy': 'welsh', 'xh': 'xhosa',
             'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}


class SR_GUI(Frame):
    # Printing the Python Version
    print("Python Version:" + sys.version)

    # The below is the constructor method. In this method we are setting the title of the frame and and configuring the backgroung color.
    # The argument self in the __init__ method points to the current object
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.master = master
        self.master.config(bg="teal")
        self.master.title("Speech Recognition")
        self.add_widgets()

    # In add_widgets() we are creating the widgets
    def add_widgets(self):
        self.combo_speech_var = StringVar()
        # Use can use grid(),place() or pack() to place the widget in the frame or window.
        # Label widget creation
        # Retrieving all the languages dictionary values and converting to list as we are passing as input to the combobox
        self.speech_lang_values = list(speech_languages.values())
        # Retrieving all the languages dictionary keys as we want to pass to the destination field during the translation
        self.speech_lang_keys = list(speech_languages.keys())
        label_speech_language = Label(self.master, text="Talking in:", bg="Teal")
        label_speech_language.place(x=0, y=20)
        #self.combo_speech = Combobox(self.master, values=self.speech_lang_values, textvariable=self.combo_speech_var)
        self.combo_speech = Combobox(self.master, values=sorted(self.speech_lang_values), textvariable=self.combo_speech_var)
        self.combo_speech.bind("<<ComboboxSelected>>", self.speech_Callbackfunc)
        self.combo_speech.bind("<KeyRelease>", self.testPrint)
        self.combo_speech.set("English (United States)")
        print("2****************")
        self.combo_speech.focus_set()
        self.combo_speech.place(x=100, y=20)
        self.combo_var = StringVar()

        #print("Selected Speech Language" + ":" + self.selected_speech_value)
        label_yousaid = Label(self.master, text="You Said:", bg="teal", bd=3)
        label_yousaid.place(x=0, y=70)
        # Textarea creation. Non editable as set state to DISABLED
        text_area = Text(self.master, width=50, height=5, state=DISABLED)
        text_area.place(x=100, y=50)
        # Referenced the text_area to self.ta as it has to be used in other functions
        self.ta = text_area
        # Button Creation. On Button click it'll call the method self.add_text and set the text_area to "Listening...."
        button1 = Button(text="Click here to listen", command=self.add_text)
        button1.place(x=190, y=150)
        # To trace the tkinker variables we create the wrapper variable
        var = IntVar()
        # The labelframe_widget creation. Created to hold the radio_buttons, frame , label and combobox
        self.labelframe_widget = LabelFrame(self.master, text="Translation", width=490, height=170, bg="Teal")
        self.labelframe_widget.place(x=5, y=180)
        # Label creation
        label1 = Label(self.labelframe_widget, text="Select the radiobutton if you want to translate the text",
                       bg="Teal")
        label1.place(x=5, y=20)
        # Radio Button creation and set the state to DISABLED as don't want to enable for error messages. When loaded they are in DISABLED state
        self.yes_radiobutton = Radiobutton(self.labelframe_widget, text="Yes", variable=var, value=1, bg="Teal",
                                           state=DISABLED)
        self.yes_radiobutton.place(x=5, y=60)
        self.no_radiobutton = Radiobutton(self.labelframe_widget, text="No", variable=var, value=2, bg="Teal",
                                          state=DISABLED)
        self.no_radiobutton.place(x=5, y=90)
        print("self_ta value:" + self.ta.get(1.0, END))
        self.var_radio = var;
        print("The value of the radio button:" + str(self.var_radio.get()))
        label_translate = Label(self.master, text="Translated Text:", bg="teal")
        label_translate.place(x=5, y=410)
        self.text_area_translate = Text(self.master, width=50, height=5, state=DISABLED)
        self.text_area_translate.place(x=120, y=380)
        self.translate_button=Button(self.master,text="Click Here to Translate", bg="Teal",state=DISABLED)
        self.translate_button.place(x=200, y=490)
        cancel_button=Button(self.master, text="Reset", bg="Teal",command=self.on_Cancel,width=10)
        cancel_button.place(x=150,y=540)
        quit_button=Button(self.master,text="Quit",bg="Teal",command=self.master.destroy,width=10)
        quit_button.place(x=300,y=540)
        self.label_combo = Label(self.labelframe_widget, text="Select Language:", bg="Teal")
        self.combo_widget = Combobox(self.labelframe_widget, height=6, textvariable=self.combo_var)

    def testPrint(self,event):
        s_temp=""
        s_temp=self.combo_speech.get()
        print("testPrint:"+s_temp)


    def on_Cancel(self):
        self.combo_speech.set("English (United States)")
        self.ta.configure(state=NORMAL)
        self.ta.delete(1.0, END)
        self.ta.configure(state=DISABLED)
        self.yes_radiobutton.configure(state=DISABLED)
        self.no_radiobutton.configure(state=DISABLED)
        self.var_radio.set(0)
        self.text_area_translate.configure(state=NORMAL)
        self.text_area_translate.delete(1.0, END)
        self.text_area_translate.configure(state=DISABLED)
        self.label_combo.place_forget()
        self.combo_widget.place_forget()
        self.translate_button.configure(state=DISABLED)

    # Event for the language combo box where user selects the desired language to speak
    def speech_Callbackfunc(self, event):
        self.selected_speech_value = self.combo_speech_var.get()
        print("Callback:"+self.selected_speech_value)

    # In this method we are setting the radio button state to 0 and setting the textarea to "Listening...." and calling the speech_recog() method.
    # This method is called whenever the button click takes place
    def add_text(self):
        if self.combo_speech_var.get() == "English (United States)":
            self.selected_speech_keys = [key for (key, value) in speech_languages.items() if
                                         value == "English (United States)"]
            print(self.selected_speech_keys)
        else:
            self.selected_speech_keys = [key for (key, value) in speech_languages.items() if
                                         value == self.selected_speech_value]
        self.final_sk = re.sub('[^-a-z-A-Z]', '', str(self.selected_speech_keys))
        self.var_radio.set(0)
        self.ta.configure(state=NORMAL)
        self.ta.delete(1.0, END)
        print("****")
        self.ta.insert(END, "Listening....")
        self.text_area_translate.configure(state=NORMAL)
        self.text_area_translate.delete(1.0, END)
        self.text_area_translate.configure(state=DISABLED)
        self.label_combo.place_forget()
        self.combo_widget.place_forget()
        self.ta.update()
        self.speech_recog()

    # In this method we are creating object for speechrecognition and selecting the engine we want to use.
    def speech_recog(self):
        # Printing the Speech Recognition Version
        print("Speech Recognition:" + sr.__version__)
        # Creating the object for speech recognition as r
        r = sr.Recognizer()
        # Print the object r
        print("The object of speech recognition:" + str(r))
        # As we want to listen to the voice from the microphone use the Microphone() from speech_recognition
        micro_phone = sr.Microphone()
        # To list all the available microphones use the list_microphone_names
        list_of_microphone_devices = micro_phone.list_microphone_names()
        print("List of available devices:")
        for i in range(0, len(list_of_microphone_devices)):
            print(list_of_microphone_devices[i] + " ")
        print("Total number of devices:" + str(len(list_of_microphone_devices)))
        with micro_phone as source:
            # As we are using the microphone as source we use the listen(). If we are using source as some audio files we use the record()
            audio = r.listen(source)
        try:
            self.a_text = r.recognize_google(audio, language=self.final_sk)
            print("you said: " + self.a_text)
            # As we want to clear the text everytime we speak, we delete the already present text in the textarea insert new text and diable the
            # textarea. Before inserting the text to the textarea set the state to NORMAL or else if wont insert the text
            self.ta.delete(1.0, END)
            self.ta.insert(END, self.a_text)
            self.ta.configure(state=DISABLED)
            # By default textarea contains the newline. Check if its "\n. And set the radiobuttons to the enable state and call the combo_box method
            if self.ta.get(1.0, END) != "\n":
                print("Inside speech_recog function if")
                self.yes_radiobutton.configure(state=NORMAL, command=self.combo_box)
                self.no_radiobutton.configure(state=NORMAL, command=self.combo_box)
            # In the exception we disabling the radio buttons and inserting the error message inside the textarea
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.ta.delete("1.0", END)
            self.ta.insert(END, "Click the button to try again")
            self.ta.configure(state=DISABLED)
            messagebox.showwarning("Warning", (error + "\n" + "Try Again....!"))
            self.yes_radiobutton.configure(state=DISABLED)
            self.no_radiobutton.configure(state=DISABLED)

    # Inside this method we are creating the label and the combobox widget and loading the combobox with the values of the language dictionary
    def combo_box(self):
        print("In Combo box")
        # If the radiobutton selected is Yes then it'll display the widget combobox and label
        if self.var_radio.get() == 1:
            self.label_combo.place(x=130, y=50)
            self.combo_widget.place(x=250, y=50)
            # Retrieving all the languages dictionary values and converting to list as we are passing as input to the combobox
            self.lang_values = list(languages.values())
            # Retrieving all the languages dictionary keys as we want to pass to the destination field during the translation
            self.lang_keys = list(languages.keys())
            # As the list values are in lower, capitalizing the list
            self.lang_values_Capitalize = [self.lang_value.capitalize() for self.lang_value in self.lang_values]
            print(self.lang_values_Capitalize)
            # Passing the values to the combobox using widget.configure
            self.combo_widget.configure(values=self.lang_values_Capitalize)
            # Setting the default value of the combobox to "Select" instead of empty
            self.combo_widget.set("Select")
            self.combo_widget.bind("<<ComboboxSelected>>", self.callbackFunc)
            print("Button Click combo box:" + self.combo_var.get())
            # self.update()
            self.translate_button.configure(state=NORMAL,command=self.translate_text)

        else:
            # Messagebox creation which will display the  if there is no translation when "No" radiobutton is selected and all the widgets
            # in the frame will be destroyed
            # messagebox.showinfo("Translation", "No translation is available for this text")
            #self.remove_widgets()
            self.combo_widget.place_forget()
            self.label_combo.place_forget()
            # Call the insert_translation_text() where we are setting the translated text in the textbox or delete the translation if there is no
            # translation available
            self.insert_translation_text()
            self.translate_button.configure(state=DISABLED)

    # This method is called from the bind() in combo_box(). Finally we are converting the selected item to lower and calling the translate_text()
    # where are retreiving the key for the value selected
    def callbackFunc(self, event):
        self.selected_value = self.combo_var.get().lower()
        print("Selected Language" + ":" + self.selected_value)
        #self.translate_text()

    # This method will retreive the key pass to the destination field in translator.translate()
    def translate_text(self):
        self.selected_keys = [key for (key, value) in languages.items() if value == self.selected_value]
        # Here we are extracting only the alphabets. As the keys we get in enclosed in the square brakets and single quotes
        reg_key = re.sub('[^-a-zA-Z]', '', str(self.selected_keys))
        print("Type of reg_key:")
        print("reg_key:" + reg_key)
        # Creating the object for translator
        translator = gt()
        self.text_after_translation = translator.translate(self.a_text, dest=reg_key)
        print(self.text_after_translation)
        self.insert_translation_text()

    # This method will insert the translated text to the text_area_translate and delete the content in the text_area_translate if there is no
    # translation available
    def insert_translation_text(self):
        if self.var_radio.get() == 1:
            print("In translate_text")
            self.text_area_translate.configure(state=NORMAL)
            self.text_area_translate.delete(1.0, END)
            self.text_area_translate.insert(1.0, self.text_after_translation.text)
        else:
            self.text_area_translate.configure(state=NORMAL)
            self.text_area_translate.delete(1.0, END)
            self.update()
            #messagebox.showinfo("Info", "Translation is not available for the text")
        self.text_area_translate.configure(state=DISABLED)
root = Tk()
# Set the dimensions of the window using geometry
root.geometry("500x600")
# Disable maximise
root.resizable(width=0, height=0)
my_sr = SR_GUI(root)
root.mainloop()
