import pyttsx3
import PyPDF2
from tkinter import *

root = Tk()
root.title("Python Audiobooks")
root.geometry('400x400')

def pdf_to_sound_file():
	input_file_name = path_text.get(1.0, 'end-1c')
	output_file_name = input_file_name.replace('.pdf', '.mp3')

	# The Backend
	''' Read the pdf file
		Initialise the text-to-speech function
		Extract the text from each page
		Save the final text as an mp3 file
	'''
	with open(input_file_name, 'rb') as file:
		reader = PyPDF2.PdfFileReader(file)
		audio = pyttsx3.init()
		audio.setProperty('rate', 120)

		final_text = ''
		for page in range(reader.numPages):
			page = reader.getPage(page)
			text = page.extractText()

			final_text += text

		audio.save_to_file(final_text, output_file_name)
		audio.runAndWait()

# The GUI
path_label = Label(root, text='File Path or URL')
path_label.pack(pady=10)

path_text = Text(root, height=1, font=("Arial", 12))
path_text.pack(pady=5)

convert_btn = Button(root, text='Start Converting', padx=4, pady=2, command=pdf_to_sound_file)
convert_btn.pack(pady=8)

root.mainloop()