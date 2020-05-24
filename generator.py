import os
import io
import urllib.parse

def run():
  markdownPath = os.getenv("markdownPath")
  templatePath = os.getenv("templatePath")
  branchName = os.getenv("branchName")
  repositoryName = os.getenv("GITHUB_REPOSITORY")

  if (os.path.isfile(markdownPath)): 
    print(f"Markdown Path {markdownPath} exists")
  else:
    raise Exception(f"Markdown Path {markdownPath} not found")
  
  if (os.path.isfile(templatePath)): 
    print(f"Markdown Path {templatePath} exists)")
  else:
    raise Exception(f"Markdown Path {templatePath} not found")

  buttonExists = False
  lines = []
  with open(markdownPath, 'r') as file:
    lines = file.readlines()
    buttonExists = lines.__contains__("https://aka.ms/deploytoazurebutton")

  if (buttonExists is True): 
    print("Deploy to Azure button already exists")
    print("::set-output name=fileUpdated::false")
  else:
    publicFileUrl = f"https://raw.githubusercontent.com/{repositoryName}/{branchName}/{templatePath}"
    print(f"Add button for {publicFileUrl}")
    encodedPublicFileUrl = urllib.parse.quote(publicFileUrl, safe='')
    lineToWrite = f"[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/{encodedPublicFileUrl})"

    with open(markdownPath, 'w') as file: 
      lines.insert(2, lineToWrite)
      lines = "".join(lines)
      file.writelines(lines)

    print("::set-output name=fileUpdated::true")

if __name__ == "__main__":
  run()