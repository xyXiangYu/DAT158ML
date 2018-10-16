![DAT158 image](./assets/DAT158-2_english_small.png)

# DAT158ML
Code and documentation for [DAT158](https://www.hvl.no/en/studies-at-hvl/study-programmes/course/dat158)-ML at HVL. Go to [Canvas](https://hvl.instructure.com/courses/3039) for information about the course.

# Installation
We recommend that you install Python through [Anaconda](https://www.anaconda.com/distribution). Choose "Python 3.6 version". Test your installation by running `python --version` in a terminal. The output should contain "Python 3.6" and «Anaconda». 

After you've made sure that Anaconda is installed, go through the following steps: 
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
If you're using Linux or MacOS and the above command fails, run 
```bash 
source ~/.bash_profile
``` 
and try `conda activate dat158` again. If that fails, use `source activate dat158` instead.

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

# Troubleshooting

* If you use Windows and get an error on the form `ImportError: DLL load failed: The operating system cannot run %1`, try changing the installed version of `intel-openmp` by running `conda install -c defaults intel-openmp -f` in the DAT158 environment. Make sure you're in the correct environment (first do a `conda activate dat158`).


