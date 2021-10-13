Lesson Description - Project Overview
and Setup: Load-Testing CLI
Python is an amazing scripting language, and one way that we can use it is to create
scripts and command line tools. For our first command line project, we're going to
build a CLI that will allow us to load-test a web site to see how many requests can be
handled in a set amount of time. In this lesson, we'll cover the layout of our project
and discuss how we want it to be used.
Documentation for This Video
Setup.py for Humans
Pipenv
Python .gitignore
Starting with README.md
Before building a project, it's a good idea to conceptualize how it should be used.
This prevents us from building features that aren't really needed. An interesting way
to do this is to write the README for the project first. Our project is called assualt,
so let's create a directory with a README.md in it and a directory to eventually hold
our package's modules:
Our tool needs to do a few things:
Take a URL to make requests to.
Make a number of requests (this should be configurable).
Make requests with a certain amount of concurrency (this should be
configurable).
Output some general stats about the requests. It should optionally allow for
JSON file output of this information.
Here's an example of what it will look like to make 3000 requests:
•
•
•
$ mkdir -p assault/assault
$ cd assault
$ touch assault/__init__.py
$ touch README.md
•
•
•
• 
Here's what our README.md will look like:
assault/README.md
$ assault -r 3000 -c 10 https://example.com
.... Done!
--- Results ---
Successful requests 3000
Slowest 0.010s
Fastest 0.001s
Average 0.003s
Total time 2.400s
Requests Per Minute 90000
Requests Per Second 1250
# assault
A simple CLI load testing tool.
## Installation
Install using `pip`:
```
$ pip install assault
```
## Usage
The simplest usage of `assault` requires only a URL to test against
and 500 requests synchronously (one at a time). This is what it
would look like:
```
$ assault https://example.com
.... Done!
--- Results ---
Successful requests 500
Slowest 0.010s
Fastest 0.001s
Average 0.003s
Total time 0.620s
Requests Per Minute 48360
Requests Per Second 806
```
If we want to add concurrency, we'll use the `-c` option, and we can 
With our documentation in place, we at least have something to come back to if we
lose track of what we should be working towards.
use the `-r` option to specify how many requests that we'd like to
make:
```
$ assault -r 3000 -c 10 https://example.com
.... Done!
--- Results ---
Successful requests 3000
Slowest 0.010s
Fastest 0.001s
Average 0.003s
Total time 2.400s
Requests Per Minute 90000
Requests Per Second 1250
```
If you'd like to see these results in JSON format, you can use the `-
j` option with a path to a JSON file:
```
$ assault -r 3000 -c 10 -j output.json https://example.com
.... Done!
```
## Development
For working on `assult`, you'll need to have Python >= 3.7 (because
we'll use `asyncio`) and [`pipenv`][1] installed. With those
installed, run the following command to create a virtualenv for the
project and fetch the dependencies:
```
$ pipenv install --dev
...
```
Next, activate the virtualenv and get to work:
```
$ pipenv shell
...
(assault) $
```
[1]: https://docs.pipenv.org/en/latest/
The setup.py
Some of the other files that we'll want to have before we dig into the code are the se
tup.py and the .gitignore. These files can be written by hand, but there are some
pretty great starting points out there.
For the setup.py, we can use the setup.py for Humans. We'll need to make some
modifications, but this file will save us a lot of time.
Let's download the file and start modifying it:
As for our modifications, we'll want to change things in the # Package meta-data
section to be about assault:
setup.py (partial)
We'll also want to change any mention of Python 3.6.0 to Python 3.7.0.
The .gitignore
For our .gitignore file, we're going to use the one for Python maintained by GitHub.
We can pull it down using the following curl command:
At this point it makes sense to also intialize our project as a Git repository, so let's
do that:
$ curl -O https://raw.githubusercontent.com/navdeep-G/setup.py/
master/setup.py
# Package meta-data.
NAME = 'assault'
DESCRIPTION = 'A Python based web load testing tool.'
URL = 'https://github.com/example/assault'
EMAIL = 'me@example.com'
AUTHOR = 'Example Person'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.1.0'
$ curl https://raw.githubusercontent.com/github/gitignore/master/
Python.gitignore -o .gitignore
Using Pipenv for our Virtual Environment
Finally, we're going to use Pipenv to manage our virtual environment and
development dependencies. Since we're creating an installable library, we'll also need
to add dependencies to the setup.py later on, but Pipenv is still useful for us while
we're developing.
Let's initialize our environment using Python 3.7 and install twine as a development
dependency as specified by the setup.py to get the python setup.py upload
feature:
Now we're ready to make our first commit and then start developing our tool:
$ git init
$ pipenv install --python python3.7 twine --dev
...
$ git add --all .
$ git commit -m 'Initial commit'