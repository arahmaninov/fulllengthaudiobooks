import os
import requests
from bs4 import BeautifulSoup
  
# Change this URL
url = "https://fulllengthaudiobooks.com/rick-riordan-the-lightning-thief-percy-jackson-and-the-olympians-book-1-audiobook/"

print("\nParsing https://fulllengthaudiobooks.com ...\n")
  
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')

book_title = soup.title.text
first_mp3 = requests.get(soup.find('audio').a.text)
list_mp3 = soup.find_all('audio')

print(f'\nPreparing downloading {book_title}\n')

if book_title not in os.listdir():
	os.mkdir(book_title)
	for number, audio in enumerate(list_mp3, 1):
		with open(os.path.join(book_title, f'{number}.mp3'), 'wb') as f:
			print(f'Downloading file {number} out of {len(list_mp3)}')
			audio = requests.get(audio.a.text)
			f.write(audio.content)
	print(f'\nDirectory \"{book_title}\" has been created. \nAudiofiles successfully downloaded.')
else:
	print(f'Directory \"{book_title}\" already exists. Delete this directory and try again')