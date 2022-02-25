from pypi_scrapped import pypi_search
project = input ("Type something ")
result = pypi_search (project)
if not result:
  print ("nothing found on pypi")
else:
  print (result)
