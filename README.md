# Bible Lover 

![Django deploy](https://github.com/tushortz/biblelover/workflows/Django%20deploy/badge.svg?branch=develop)

A Bible-based website with lots of features

## Documentation link for useful tools

* [Python](https://docs.python.org/3.8/tutorial/introduction.html)
* [Django](https://docs.djangoproject.com/en/3.0/intro/overview)
* [Git](https://git-scm.com/docs)
* [Theme (CSS/JS) library](https://preview.webpixels.io/quick-website-ui-kit/docs)

## Working on a new issue

1. Select an issue and assign it to yourself on [github issues](https://github.com/tushortz/biblelover/issues).


2. Make sure you are on the develop branch, do a `git pull` to update your branch. then `git checkout -b <new branch name>` to create and switch the new branch.

> **Note:** The new branch must not include spaces. The format is as follows
>
> * BIL (short for project name i.e. Bible Lover) followed by a dash (-)
> * Issue number e.g. 11 followed by a forward slash (/)
> * Short text describing the feature to be added
>
> So an example is:
> 
> **BIL-15/create-user-model**

3. After the fix add your files from the terminal or editor console and pass a commit message with `git commit -am "my message"`. then do a `git push -u origin <branch name>`

4. Once commit has been pushed, go back to github and **create a pull request** linking it to the `develop` branch.


## Setup

> **Note:** The `$PROJECT_DIRECTORY` is the folder where `manage.py` file is located.

### Requirement

#### Required

* Python (version >= 3.0)
* Text editor -> e.g. Visual Studio Code, Atom, Sublime text
* Database -> e.g. sqlite, postgres or mysql
* Git


#### Optional

* db browser for sqlite -> Provides a UI to view database structure and data directly


### Python version check

You need to setup a virtual environment first. Make sure you are running python version >= 3. Navigate to the `$PROJECT_DIRECTORY` and run the following command to check.


```
python --version
```

if the result is python version 2, then use this command

```
python3 --version
```

### Setting up a virtual environment

if the result above is python version >= 3.0, then run the following command to set up a virtual environment

```
python3 -m venv env
```

> **Note:** Whichever command shows python version >= 3.0 is the one to use in the command above and this should be run in the command prompt or terminal or powershell for windows.
>
> Once setup, you don't need to run the above command everytime unless you are re-initiating the virtual environment

### Activating virtual environment

> **Note:** This has to be done everytime you are working on the project so that every developer will have a consistent environment. Navigate to the `$PROJECT_DIRECTORY`

For windows OS, run

```
.\env\Scripts\activate
```

For MacOS or Linux, run

```
source env/bin/activate
```


#### Setting up django

After activating the virtual environment, install all the necessary modules by running.

```
pip install -r requirements.txt
```

You may need to update your version of pip by running
```python -m pip install --upgrade pip
```

> **Note:** You only need to run this once unless there is an update to the `requirements.txt` file

### Setting up a SECRET KEY

To set up a secret key, you need to add the key as an environment variable. This needs to be done only once.

#### For linux

open the `~/.bashrc` file and enter the following to the bottom of the file

```
export SECRET_KEY="<my_secret_key>"
```

save the file and exit. Update the changes into the terminal by running the following code in your current working terminal otherwise restart the terminal

```
source `~/.bashrc
```

#### For windows

Search `environment variables` and add a new entry to the `system environment variables`

* Environment Name: `SECRET_KEY`
* Environment Value: `<secret_key_value>`

After this, save and restart your terminal

### Running the project

Everytime a new model is created, run

```
python manage.py makemigrations
```

and make the change apply to the database by running

```
python manage.py migrate
```

### Loading test data into database

Usually when creating a new database, to save time and populate test data into database, run the following command


```
python manage.py loaddata testdata/seeds.json
```

### Viewing site

To view the site, make sure the server is running. If server is down or not running, run the following command to get the server up and running

```
python manage.py runserver
```

then navigate to http://localhost:8000



## Contributions

Fork the project and create a pull request.

> **Note:** Everytime you are about to continue working on a project, first run in the command line to update your repository.

```
git pull
```

> **Note:** Evertime you are working on a new ticket, always create a new branch and this would usually be from the `develop` branch.
