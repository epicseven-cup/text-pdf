import os
from pypdf import PdfReader

input_d = "./input/"
output_d = "./output/"



def main():
	for filename in os.listdir(input_d):
		path = input_d + filename 
		reader = PdfReader(path)
		number_of_pages = len(reader.pages)
		print("===============================")
		print(f"Starting to extract text from {path} with {number_of_pages} pages")
		with open(output_d + filename[:-4] + ".txt", "w") as file:
			for page in range(number_of_pages): 
				text = reader.pages[page].extract_text()
				print(f"Text: {text}")
				file.write("\n")
				file.write(f"========PAGE{page}========")
		file.close()
		print("Finish extracting text from pdf")
		print("===============================")
if __name__ == "__main__":
	main()
