import glob
import os

print("Este script converte de mol2 para pdbqt. Ele deve estar na pasta em que os arquivos mol2 estão.")

pasta = glob.glob("*.mol2")

for i in pasta:
	print(i)
	saida = i.replace("mol2", "pdbqt")
	comando = f"/home/thor/MGLTools-1.5.7/mgltools_x86_64Linux2_1.5.7/bin/pythonsh /home/thor/MGLTools-1.5.7/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -l {i} -o {saida}"
	#print(comando)	
	os.system(comando)

print("fim")
