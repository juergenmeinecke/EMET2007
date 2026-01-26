# Econometrics Notebook Update Instructions

For all ipynb-files in the directory
./underhood/computer_labs/Python/notebooks/claude/notebooks_new/
do this:

change all relative paths to csv-files to an absolute path as per this example:

```python
df = pd.read_csv('../datasets/earnings_and_height.csv')
```

changes to:

```python
df = pd.read_csv('https://raw.githubusercontent.com/juergenmeinecke/EMET2007/refs/heads/main/datasets/earnings_and_height.csv')
```

This implies that the distinction between Colab users and Anaconda/Jupyter users is no longer
necessary. 

Update all all ipynb-files in the directory
./underhood/computer_labs/Python/notebooks/claude/notebooks_new/
accordingly.

