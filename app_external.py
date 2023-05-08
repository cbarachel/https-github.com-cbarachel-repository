import subprocess

# run a command in the terminal
# Is -1 means list files and folders with details
# Is -1 uses lowercase L, not 1 (one)
subprocess.run(["git", "--version"])
subprocess.run(["git", "status"])
