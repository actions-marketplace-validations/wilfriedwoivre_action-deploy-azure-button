import os
import io
import urllib.parse

def run():
  markdownPath = os.getenv("markdownPath")
  templatePath = os.getenv("templatePath")
  branchName = os.getenv("branchName")
  targetAzureUrl = os.getenv("targetAzureUrl")
  repositoryName = os.getenv("GITHUB_REPOSITORY")

  if (os.path.isfile(markdownPath)): 
    print(f"Markdown Path {markdownPath} exists")
  else:
    raise Exception(f"Markdown Path {markdownPath} not found")
  
  if (os.path.isfile(templatePath)): 
    print(f"Markdown Path {templatePath} exists")
  else:
    raise Exception(f"Markdown Path {templatePath} not found")

  matching = False
  lines = []
  with open(markdownPath, 'r') as file:
    lines = file.readlines()
    matching = [s for s in lines if "https://aka.ms/deploytoazurebutton" in s]

  if (len(matching) != 0): 
    print("Deploy to Azure button already exists")
    print(f"::set-output name=fileUpdated::false")
  else:
    publicFileUrl = f"https://raw.githubusercontent.com/{repositoryName}/{branchName}/{templatePath}"
    print(f"Add button for {publicFileUrl}")
    encodedPublicFileUrl = urllib.parse.quote(publicFileUrl, safe='')
    lineToWrite = f"[![Deploy to Azure](https://aka.ms/deploytoazurebutton)]({targetAzureUrl}{encodedPublicFileUrl})\n"

    with open(markdownPath, 'w') as file: 
      lines.insert(2, lineToWrite)
      lines = "".join(lines)
      file.writelines(lines)

    print(f"::set-output name=fileUpdated::true")
    
if __name__ == "__main__":
  run()