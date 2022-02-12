import os

print("Updating Packages...\n\n")
os.system('sudo apt-get update')

print("Getting Required Packages from Repositories...\n\n")
os.system('sudo apt-get install git -y')

packages={"Icon Packages":"git clone https://github.com/daniruiz/flat-remix.git"}

icon_path=os.path.join("/","usr","share","icons")
os.chdir(icon_path)
print("Getting {}".format(packages.keys()[0]))
os.system("git clone {}".format(packages['Icon Packages']))

for folder in os.listdir(os.path.join(icon_path,'flat-remix')):
    if "Flat" in folder:
        os.system('sudo mv {} {}'.format(os.path.join(icon_path,"flat-remix",folder),icon_path))

for folder in os.listdir(icon_path):
    if "Flat" in folder:
        os.system('sudo gtk-update-icon-cache {}'.format(os.path.join(icon_path,folder)))


os.system('sudo rm -r flat-remix')
