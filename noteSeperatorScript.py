"""
Liam Duncan
24/01/17, last changed 24/01/17
Course notes compiler
-takes sporatic notes with a given course identifier and writes them
into a new file from the complete 'notes' file
"""

#user cmdline input: new filename and paragraph identifier 
newFileName = input('Enter desired filename: ')
textMarker = input('Enter identifier of beginning of desired notes: ')

#open ref semester notes file, create filtered file
readableFile = open( 'notes.txt', 'r')
writableFile = open( newFileName, 'a')#only append permission

#turns file contents into list of paragraphs
notesContentsString = readableFile.read()
notesContentsList = notesContentsString.split( '\n\n')# split on blank line
filteredContents = []# declaration

#find desired paragraphs from contents
for paragraph in notesContentsList:
    if paragraph[:len(textMarker)] == textMarker:# uses string slicing
        filteredContents.append(paragraph)

#writes filtered content with restored paragraph seperators
for paragraph in filteredContents:
    writableFile.write(paragraph)
    writableFile.write('\n\n')

#close files
readableFile.close()
writableFile.close()
