![DAT158 image](./assets/DAT158-2.jpg)

# DAT158ML
Code and documentation for [DAT158](https://www.hvl.no/en/studies-at-hvl/study-programmes/course/dat158)-ML at HVL. Go to [Canvas](https://hvl.instructure.com) for information about the course.

# Installation
We recommend that you install Python through [Anaconda](https://www.anaconda.com/distribution). Choose "Python 3.6 version". Test your installation by running `python --version` in a terminal. The output should contain "Python 3.6" and «Anaconda». 

Then, go through the following steps: 
### Download the repository: 
```bash
git clone https://github.com/alu042/DAT158ML
cd DAT158ML
```
### Configure the Python environment
```bash
conda env update
```

### Activate environment:
```bash
conda activate dat158
```

### Install a Jupyter kernel
```bash
python -m ipykernel install --user --name dat158 --display-name "DAT158"
```
...and add collapsible headings in the notebooks (not necessary, but convenient)
```bash
jupyter nbextension enable collapsible_headings
```

### Test your installation
Run through the notebook `0.0-test.ipynb`:
```bash
jupyter notebook
```
You can also use [JupyterLab](https://github.com/jupyterlab/jupyterlab): `jupyter lab`.

## Update
The code and environment will be updated throughout the course. Run the following two commands regularly:
* Update code: `git pull`
* Update environment: `conda env update`




