import os
import io
from github import Github

def run():
  markdownPath = os.getenv("markdownPath")
  templatePath = os.getenv("templatePath")
  repositoryName = os.getenv("repositoryName")

  if (os.path.isfile(markdownPath)): 
    print(f"Markdown Path {markdownPath} exists")
  else:
    raise Exception(f"Markdown Path {markdownPath} not found")
  
  if (os.path.isfile(templatePath)): 
    print(f"Markdown Path {templatePath} exists)")
  else:
    raise Exception(f"Markdown Path {templatePath} not found")

  print(repositoryName)

  buttonExists = False
  with open(markdownPath, 'r') as file:
    data = file.readlines()
    buttonExists = data.__contains__("https://aka.ms/deploytoazurebutton")

  if (buttonExists is True): 
    print("Deploy to Azure button already exists")



if __name__ == "__main__":
  run()