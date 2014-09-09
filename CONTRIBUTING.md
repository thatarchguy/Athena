# How to contribute

I simply cannot access the huge number of platforms and configurations to run this project on.
I want to keep it as easy as possible to contribute changes that
get things working in your environment. There are a few guidelines that I
need contributors to follow so that I can have a chance of keeping on
top of things.

I use [Waffle.io](https://waffle.io/thatarchguy/Athena) to better manage issues:

## Getting Started

* Make sure you have a [GitHub account](https://github.com/signup/free)
* Submit a ticket for your issue, assuming one does not already exist.
  * Clearly describe the issue including steps to reproduce when it is a bug.
  * Make sure you fill in the earliest version that you know has the issue.
* Fork the repository on GitHub

##Types of Contributions

###Report Bugs

Report bugs at https://github.com/thatarchguy/Athena/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

###Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

###Implement Features

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

###Write Documentation

Athena could always use more documentation.

###Submit Feedback

The best way to send feedback is to file an issue at https://github.com/thatarchguy/Athena/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.


##Setting up

Setup for Local Development

1. Fork the `Athena` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/Athena.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv Athena
    $ cd Athena/
    $ python setup.py develop
or
    $ make env

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature
   
   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests:

    $ flake8 Athena tests
    $ python setup.py test

   To get flake8, just pip install them into your virtualenv. 

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.




