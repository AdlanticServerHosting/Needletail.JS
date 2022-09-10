from Naked.toolshed.shell import execute_js, muterun_js
from rich.console import Console

response = muterun_js('index.js')
success = execute_js('index.js')
console = Console()

if success:
  pass
else:
  cerr = response.stderr.decode("utf-8").split("\n")
  cfile = open(cerr[0].split(":")[0], "r")
  cfilesplit = cfile.read().split("\n")
  cfile.close()

  cfilelength = len(cfilesplit)
  if int(cerr[0].split(":")[1]) - 1 < 2:
    if int(cerr[0].split(":")[1]) - 1 == 0:
      pass
    else:
      console.print("       " + str(int(cerr[0].split(":")[1]) - 1) + ". | " + cfilesplit[int(cerr[0].split(":")[1]) - 2])
  else:
    console.print("       " + str(int(cerr[0].split(":")[1]) - 1) + ". | " + cfilesplit[int(cerr[0].split(":")[1]) - 2])
  console.print("    [red bold]=> " + str(cerr[0].split(":")[1]) + ". | " + cfilesplit[int(cerr[0].split(":")[1]) - 1])
  if int(cerr[0].split(":")[1]) < cfilelength:
    console.print("       " + str(int(cerr[0].split(":")[1]) + 1) + ". | " + cfilesplit[int(cerr[0].split(":")[1])])
  else:
    print("ing")
  print("Boo...")