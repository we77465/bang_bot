import os
for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        print(f'cmds.{Filename[:-3]}')