from pathlib import Path

Path('data/chunks').mkdir(parent = True , exists_ok = True)

print('folder created: ',Path ('data/chunks').exists())
