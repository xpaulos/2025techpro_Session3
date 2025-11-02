### Code Explanation

A Python script using the Flask web framework that will generate a webpage with 30 squares, each filled with a unique color. The script uses a predefined list of 30 specific hex color codes. The colors are stored in a list variable named colors. Each square has also a unique name of a fruit. The text for each square is defined in a separate config.json file and is loaded by the Flask application.

### Open wsl ubuntu <br>

### Prepare environment to be able to work and debugg the code<br>

Install python3 apt-get install python3<br>
Verify installation python3 --version<br>
Install python-pip ---> sudo apt install python3-pip<br>
Verify installation pip --version<br>
Install flask ---> pip install flask<br>
Verify installation flask --version<br>

### Prepare your folder and git<br>

create a folder named colorssq under your home directory ---> mkdir colorssq<br>
Initialize a git repository ---> git init<br>

### Configure your git global set up<br>

Check your git set up ---> git config list<br>
If not already much you username and emails with one you have created for github <br>
git config --global user.name "your username"<br>
git config --global user.email " your email address"<br>

### Prepare you github account<br>

Go to github.com and login to your account<br>
Go to https://github.com/xpaulos/2025techpro_Session3 and fork the repository with the same name in your account (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)<br>
Go back to WSL ubuntu and create an ssh key for your github account (https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)<br>
ssh-keygen -t ed25519 -C "your_email@example.com"<br>
cat ~/.ssh/id_ed25519.pub<br>
Copy the key<br>
Go to https://github.com/settings/keys<br>
Click create new ssh key, give it a name and paste the key you copied earlier from the terminal. Click save<br>
check your machines connection with your github account ---> ssh -T git@github.com<br>
Add the remote repository for pull and push requests<br>
git remote add origin https://github.com/OWNER/REPOSITORY.git<br>
Verify the remote<br>
git remote -V<br>

# You are now ready to start contributin to the project.<br>

> > > > > > > a8260e07ba77d24944d0a2232c0043ff69ec460a
