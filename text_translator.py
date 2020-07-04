from tkinter import *
from tkinter.ttk import Combobox
from textblob import TextBlob
from tkinter import messagebox
root=Tk()
lan_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'} 
def submit_function(event=None):
	try:
		UserWord=TextBlob(TextLabelEntry.get())
		UserInputLang=UserWord.detect_language()	   #Its not detecting the lang properly..i mean error!!!!!
		lan_todict=languages.get()
		UserOutputLang=lan_dict[lan_todict]
		UserWord=UserWord.translate(from_lang=UserInputLang,to=UserOutputLang)			#It required the internet connection to check or dteect
		TranslatedTextAns.grid()
		TranslatedTextAns.configure(text=UserWord)
		TranslatedLabelEntry.set(UserWord)
	except:
		TranslatedLabelEntry.set('Try Diffrenet Word !!')
def exit_function():
	NotificationMessage=messagebox.askyesnocancel('Notification Bar','Do you want to exit ?',parent=root)
	if(NotificationMessage==True):
		root.destroy()
def on_enterUserInputEntry(e):
	UserInputEntry['bg']='pink'

def on_enterUserOutputEntry(e):
	UserOutputEntry['bg']='pink'

def on_enterSubmitButton(e):
	SubmitButton['bg']='springgreen'

def on_enterExitButton(e):
	ExitButton['bg']='springgreen'
#def on_enterfont_box(e):
	#font_box['bg']='springgreen'

def on_leaveUserInputEntry(e):
	UserInputEntry['bg']='white'

def on_leaveUserOutputEntry(e):
	UserOutputEntry['bg']='white'

def on_leaveSubmitButton(e):
	SubmitButton['bg']='yellow'

def on_leaveExitButton(e):
	ExitButton['bg']='yellow'
#def on_leavefont_box(e):
	#font_box['bg']='springgreen'
#Label
TextLabel=Label(root,text='Enter Word :-',bg='skyblue',font=('time',15,'italic bold'))
TextLabel.grid(row=1,column=0,padx=20,pady=20)

TranslatedText=Label(root,text='Translated Word :-',bg='skyblue',font=('time',15,'italic bold'))
TranslatedText.grid(row=2,column=0,padx=20,pady=20)

TranslatedTextAns=Label(root,text=' ',bg='cyan',font=('time',15,'italic bold'))
TranslatedTextAns.grid(row=3,column=0,padx=20,pady=20)
TranslatedTextAns.grid_remove()
 #Entry box
TextLabelEntry=StringVar()
UserInputEntry=Entry(root,textvariable=TextLabelEntry,width=30,font=('time',15,'italic bold'))
UserInputEntry.grid(row=1,column=1,padx=20,pady=20)

TranslatedLabelEntry=StringVar()
UserOutputEntry=Entry(root,textvariable=TranslatedLabelEntry,width=30,font=('time',15,'italic bold'))
UserOutputEntry.grid(row=2,column=1,padx=20,pady=20)

#Buttons
SubmitButton=Button(root,text='Submit',bd=10,bg='yellow',activebackground='purple4',width=10,font=('time',15,'italic bold'),command=submit_function)
SubmitButton.grid(row=4,column=0,padx=20,pady=20)

ExitButton=Button(root,text='Exit',bd=10,bg='yellow',activebackground='red',width=10,font=('time',15,'italic bold'),command=exit_function)
ExitButton.grid(row=4,column=1,padx=20,pady=20)
root.bind('<Return>',submit_function)
#Button Hover
UserInputEntry.bind('<Enter>',on_enterUserInputEntry)
UserInputEntry.bind('<Leave>',on_leaveUserInputEntry)

UserOutputEntry.bind('<Enter>',on_enterUserOutputEntry)
UserOutputEntry.bind('<Leave>',on_leaveUserOutputEntry)

SubmitButton.bind('<Enter>',on_enterSubmitButton)
SubmitButton.bind('<Leave>',on_leaveSubmitButton)

ExitButton.bind('<Enter>',on_enterExitButton)
ExitButton.bind('<Leave>',on_leaveExitButton)


#Combo Box
languages=StringVar()
font_box=Combobox(root,width=25,textvariable=languages,state='normal')
font_box.grid(row=1,column=3,padx=20,pady=20)
font_box['values']=[e for e in lan_dict.keys()]
font_box.current(21)

#font_box.bind('<Enter>',on_enterfont_box)
#font_box.bind('<Leave>',on_leavefont_box)
#Container for app
root.geometry('800x400+100+100')
root.title('Text Translator App')
root.resizable(False,False) 
root.configure(bg='skyblue')
root.iconbitmap('kingbondl.ico')
StringText='App Developer - KingbondL / MS'
count=0
text=''
SliderLabel=Label(root,text=StringText,bg='lightskyblue',font=('arial',15,'italic bold'))
SliderLabel.grid(row=5,padx=20,pady=20,columnspan=3)

def StringTextSliderShow():
	global count,text
	if(count>=len(StringText)):
		count=-1
		text=''
		SliderLabel.configure(text=text)
	else:
		text=text+StringText[count]
		SliderLabel.configure(text=text)
	count+=1
	SliderLabel.after(200,StringTextSliderShow)
StringTextSliderShow()
root.mainloop() 
