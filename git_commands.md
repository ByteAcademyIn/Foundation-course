
### To install git on your system
sudo apt-get update

sudo apt-get install git


### Configure it to your account
git config --global user.name "Your Name"

git config --global user.email "youremail@domain.com"


### Clone this repository
git clone https://github.com/ByteAcademyIn/Foundation-course.git


### Create a branch with your name
git checkout -b branch_name


### Switch between branches
git checkout branch_name


### Add files/changes to the repo
git add .

or

git add filename


### Committ the changes
git commit -m "commit message"


### Push the changes to your branche
git push origin branch_name
