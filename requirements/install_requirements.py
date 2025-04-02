import subprocess
import pkg_resources
import sys

def install_packages():
	with open(r"C:\Users\amine\Desktop\Gestion des Projets\Credit Risk Assessment Model\requirements\requirements.txt", 'r') as file :
		packages = file.readlines()
		installed_packages = {pkg.key for pkg in pkg_resources.working_set}
		for package in packages:
			package_name = package.strip()
			if package_name not in installed_packages:
				subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
			else:
				print(f"{package_name} is already installed.")

if __name__ == "__main__":
	install_packages()