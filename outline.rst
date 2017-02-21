*******
Outline
*******

http://meopar.ca/training/ws2017
http://meopar.ca/ws2017-schedule


Session Description
===================

In Code Automation we will focus on managing model configurations,
initial and boundary conditions files,
forcing files,
model runs,
and run results files.
We'll use version control tools and scripting in Bash and Python to work in the file and run management framework to make model runs efficient and reproducible so that the focus of research stays on gaining insight from model runs.


Big Picture Overview
====================

* Definition
* Software Tools
* Assignment #1
* Organizing Your Modeling Research Life
* Assignment #2
* Writing Automation Tools
* Assignment #3


Definition
==========

Use software tools to automate tasks that are:
* tedious
* error-prone
* complicated
* repeated often
to document the story of your research,
and to make it more likely to be well organized and reproducible.

Your most important collaborators are your past and future selves - be kind to them!


Software Tools
==============

* Version Control
* Backups
* Model Runs Management
* Results Visualization


Version Control
---------------

* The most important automation tool you'll learn about this week!
*
* Version Control All The Things! (Almost...)
  * Code
  * Manuscripts of proposals, papers
  * Research notes, work log
  * Course work assignments
  * Pre- and Post-processing techniques and code

* If you are not using version control already, start! today!
* Find a local expert and use the version control tool that they use if it is:
  * Git
  * Mercurial (hg)
  * Subversion (maybe)
  But probably not if they have a grey beard like mine (or even id they don't) and say "We don't use *traditional* version control, per se", or "I have this system of shell scripts that I wrote that does that..."

* Assignment #1:
  * Create a repo for notes from this week.
  * Add and commit something about each session
  * Bonus points for putting it on GitLab or another web hosting service
  * More bonus points for making it public and sharing the URL

* What not to version control:
  * Some large binary files
  * They require lots of memory to process; ~2x their size
  * A full copy is stored every time they are committed, so frequently changed binary files make the repo grow quickly
  * Less of an issue for "hard won" binary files that aren't changed often; e.g.
    * NEMO bathymetry, coordinates, mesh masks
    * Consider using a separate repo if you are developing bathymetry, and then commit the "final" version in your working model parameters repo
  * If they aren't under version control, they need to be backed up, redundantly


Backups
-------

* For your laptop, get at least one portable USB drive, back up to it regularly with a tool like Time Capsule (Mac), and keep the drive separate from your laptop as much as possible. Even better to have 2 portable drives stored in different locations, or use a cloud backup service in addition to at least one portable drive.
* For workstations and HPC find out what is backed up, how often, and how long it is retained for.
* If you don't feel that you can recover in less than a day to the point where you can do research again, you should be worried, and you should take action to get less worried.


Model Runs Management
---------------------

* model configurations
* initial and boundary conditions files
* forcing files
* executing model runs
* run results files
* analysis and visualization

* Custom model code
  * MY_SRC in NEMO
  * ln3 in ww3
  * Try keeping your custom code in a repo you control and symlinking it into the place where the model lets you put it

* Try to use tools that other people create and *maintain*
  * NEMO-Cmd
  * ww3 run_tests ??
  * Avoiding "not invented here" is hard
* If the tools are open-source on GitLab, Github, Bitbucket, etc. learn how to look at their repos to judge their maturity, quality, and how well maintained they are

* Sooner or later, though, you will have to write your own tools

* If you don't or can't script it, write notes/documentation about the exact steps, and put those notes/docs under version control, of course!


Results Visualization
---------------------

* Try to use tools that let you write code to create and adjust figures and animations rather than using a GUI tool to make adjustments:
  * Python and matplotlib, panda, xarray
  * Matlab
* If you don't or can't script it, write notes/documentation about the exact steps, and put those notes/docs under version control, of course!


Organizing Your Modeling Research Life
======================================

Temporary Run Directories
-------------------------


Assignment #2
-------------

Create a diagram of repos and directories for your research.


Writing Automation Tools
========================

Shell Scripts
-------------


Python
------

* argparse
* shutil
* datetime (arrow)

* subprocess
* glob
* pathlib


Assignment #3
-------------

Managing Ariane output

* Intro Ariane
* Create a Python tool to run in an Ariane run directory that takes 2 arguments:
  * a model run date
  * a results directory parent
  The tool will:
  * Create a new results directory under the results directory parent.
    The name of the directory will be derived from the model run date argument.
  * Move the namelist and initial particle positions files into the new results directory.
  * Move the traj.txt output file from Ariane into the new results directory, renaming it to include the model run date; e.g. traj_20160417.txt
