import requests
from bs4 import BeautifulSoup as bs

def remove_white_spaces_from(a_string):
  return a_string.replace(" ", "")

def pypi_search (project):
  url = "https://pypi.org/project/{}".format(project)
  if url == "https://pypi.org/project/ ":
    return False
  try:
    source = requests.get(url).text
    s = bs(source, "html.parser")
    name = remove_white_spaces_from (s.find(class_ = "package-header__name").text)
    description = s.find(property = "og:description")["content"]
    release_date = remove_white_spaces_from(s.find("time").text)
    pip_command = s.find(id = "pip-command").text
    fetched_details = f"""
    name: {name}
    description: {description}
    released on: {release_date}
    installing command: {pip_command}
    """
    return fetched_details
  except Exception:
  	return False
