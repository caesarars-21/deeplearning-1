

def read_log(log):
  """takes log parameter as a file that will read by open(log,'r') as f:"""
 error = []
 with open(log, "r") as f:
  lines = f.readlines()
  for i in lines :
   result = re.findall("ERROR ([\w+\._]*)", i).groups()
   find = result[1]
   error.append(find)
 return error
