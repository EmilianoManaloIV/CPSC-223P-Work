def reverse_line(inputFile, outputFile):
    lineList = inputFile.readlines()
    lineList.reverse()
    outputFile.writelines(lineList)

with open('INPUT', 'r') as fileInput, open('OUTPUT', 'w') as fileOutput:
    reverse_line(fileInput,fileOutput)
