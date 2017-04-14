# Python Environments for Science and Engineering

This presentation was originally designed for:

https://www.meetup.com/PyMNtos-Twin-Cities-Python-User-Group/events/237061548/

A sample script was developed, `fit_data.py`, to illusrate running python code under various development environments.  The following environments were installed and setup to run this script:

* Python (3) terminal + Sublimetext editor 
* PyCharm IDE (community edition)
* Rodeo IDE
* Jupyter Notebook

Additionally, a datafile named `python_feedback.txt` was filled with voting results on the question: *Do you or would you see yourself using this environment?*  The data was compiled at the end, the associated Jupyter notebook cell run, and hence slide updated.

## Building Slides

1. Download this repository
    - Download the [reveal.js](https://github.com/hakimel/reveal.js.git)
2. Run this command:
    
> jupyter-nbconvert --to slides --reveal-prefix=<path to reveal.js> SlidesPythonSciEng.ipynb
    
where `<path to reveal.js>` should be replaced with the appropriate path.


## Change Log

```
2017-04-14 [HMokhtarzadeh]: First version of presentation.
```
