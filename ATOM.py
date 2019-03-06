"""
Bhavik Dhandhalya
2018H1030118P
ME Computer Science student at BITS Pilani

Hi there, I am trying to make my own personal bot to make my normal things easier
"""

import os
import platform
import subprocess
import webbrowser

paths = '/Users/Bhavik/'
path2 = '/Hacker_data/'
dont_go = ['/Users/Bhavik/Applications/', '/Users/Bhavik/Library/', '/Users/Bhavik/Applications (Parallels)']
git_link = 'https://github.com/BhavikDhandhalya/'
linkedin_link = 'https://www.linkedin.com/in/bhavik-dhandhalya-b5a801108/'

mail_0 = 'https://mail.google.com/mail/u/0/?tab=rm#inbox'
mail_1 = 'https://mail.google.com/mail/u/1/#inbox'
mail_2 = 'https://mail.google.com/mail/u/3/'


files = []
folders = []

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

def open_link(X):
	webbrowser.open_new_tab(X)

def dfs(cur_path):
	if cur_path in dont_go: return

	new_DB = [f for f in os.listdir(cur_path) if f[0] != '.']

	# if directory then do DFS
	for x in new_DB:
		new_path = cur_path
		if '.' in x:
			new_path = new_path + str(x)
			files.append(new_path)
		else:
			new_path = new_path + str(x) + '/'
			if os.path.isdir(new_path):
				folders.append(new_path)
				dfs(new_path)

dfs(paths)
dfs(path2)

files.sort()
folders.sort()

print ('--------INPUT FORMATS------')
print ('fi xyz.txt for files')
print ('fo xyz for folders')
print ('git for opening github')
print ('li for opening linkedin')
print ('mail 0 for dhandhalyabhavik@gmail.com')
print ('mail 1 for bhavik.bitspilani@gmail.com')
print ('mail 2 for h2018...@pilani.bitspilani.ac.in')
print ('---------------------------')

while True:
	# take INPUT from user
	#A, B = map(str, raw_input('fi xyz.txt or fo xyz ? or exit 0  ').split())
	A = str(raw_input('\n'))

	if 'exit' in A: exit(0)

	elif 'git' in A:
		open_link(git_link)

	elif 'li' in A:
		open_link(linkedin_link)

	elif 'mail' in A:
		if '0' in A: open_link(mail_0)
		elif '1' in A: open_link(mail_1)
		elif '2' in A: open_link(mail_2)
		else: open_link(mail_0)

	elif 'fi' in A:
		B = A[3:]
		# open file
		print ('opening file :')

		good = False
		for x in files:
			if x.endswith(B):
				open_file(x)
				good = True
				break

		if not good:
			for x in files:
				if B in x:
					good = True
					open_file(x)
					break

		if not good: print ('file not found')

	elif 'fo' in A:
		B = A[3:]
		# open folder
		print ('opening folder :')

		good = False
		for x in folders:
			if x.endswith(B + '/'):
				open_file(x)
				good = True
				break
		if not good:
			for x in folders:
				if B in x:
					good = True
					open_file(x)
					break

		if not good: print ('folder not found')
	else: print ('Invalid input')