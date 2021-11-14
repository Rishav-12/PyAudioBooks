import pyttsx3
import PyPDF2
import PySimpleGUI as sg

def pdf_to_sound_file(filename):
	input_file_name = filename
	output_file_name = input_file_name.replace('.pdf', '.mp3')

	# The Backend
	'''
	Read the pdf file
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

filename = sg.popup_get_file('Enter the file you wish to process')
if filename:
	pdf_to_sound_file(filename)
