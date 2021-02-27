
def read_log(log):
 error = []
 with open(log, "r") as f:
  lines = f.readlines()
  for i in lines :
   result = re.findall("ERROR ([\w+\._]*)", i).groups()
   find = result[1]
   error.append(find)
 return error
