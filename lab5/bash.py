import subprocess


result = subprocess.run("pytest", stdout=subprocess.PIPE, shell=True)


print(result.stdout)