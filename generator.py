import os
from github import Github

def run():
  markdownPath = os.getenv("markdownPath")
  templatePath = os.getenv("templatePath")

  if (os.path.exists(markdownPath)): 
    print(f"Markdown Path {markdownPath} exists")
  else:
    raise Exception(f"Markdown Path {markdownPath} not found")
  
  if (os.path.exists(templatePath)): 
    print(f"Markdown Path {templatePath} exists)")
  else:
    raise Exception(f"Markdown Path {templatePath} not found")

if __name__ == "__main__":
  run()