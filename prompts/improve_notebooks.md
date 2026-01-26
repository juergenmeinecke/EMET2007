# Econometrics Notebook Update Instructions

## Context
You are updating Jupyter notebooks for an undergraduate econometrics course (EMET2007). 
Have a look into ./underhood/computer_labs/Python/notebooks where you find pairs of files:
- `week_N.ipynb` — Student exercises (empty code cells)
- `week_N_solution.ipynb` — Tutor solutions

You will create improved versions of these following the instructions below. Put these new versions
in ./underhood/computer_labs/Python/notebooks/claude using the original naming conventions.

## Student Notebook (`week_N.ipynb`)

**Goals:** Make exercises clear and accessible for students learning both econometrics and Python.

- Modernize Python code (use current pandas/matplotlib/statsmodels idioms)
- Make exercise instructions explicit and actionable
- Add brief hints in empty code cells as comments
- Include "why we're doing this" context connecting to statistical concepts
- Reference relevant textbook sections (Stock & Watson) where appropriate
- **Scaffold complex tasks:** Break multi-step exercises into numbered sub-steps; for new concepts, provide a worked example before asking students to apply it independently

## Solution Notebook (`week_N_solution.ipynb`)

**Goals:** Help tutors teach effectively and anticipate student difficulties.

Include everything from the student notebook, plus:

- Complete, working solutions for all exercises (code only—outputs not required)
- Tutor notes marked with `> **📝 TUTOR NOTE:**` that include:
  - Common student mistakes and how to address them
  - Key points for interpretation of results
  - Discussion questions to pose
  - Time estimates where helpful
- Brief interpretations after statistical output (what do the numbers mean?)

## General Principles

1. **Preserve** the learning objectives, datasets, and core statistical methods
2. **Modernize** Python syntax without over-complicating
3. **Clarify** without being verbose
4. **Anticipate** where students struggle

## Specific Updates

### Data Loading
Use a single GitHub URL that works in all environments:
```python
df = pd.read_csv('https://raw.githubusercontent.com/juergenmeinecke/EMET2007/refs/heads/main/datasets/earnings_and_height.csv')
```
Remove the separate Colab/Anaconda setup cells.

### Statistical Tests
Replace custom t-test functions with `scipy.stats`:
```python
from scipy import stats
# Two-sample t-test (Welch's, unequal variances)
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
```

### HTML Export Exercise
Replace the current Colab/Anaconda-specific instructions with:
```markdown
## Exporting Your Work

To submit your work, export this notebook as HTML:
- **JupyterLab / Jupyter Notebook:** File → Save and Export Notebook As → HTML
- **Google Colab:** File → Download → Download .ipynb, then upload to [nbviewer](https://nbviewer.org) or use File → Print → Save as PDF

Open the exported file to verify it contains all your code and outputs.
```

## Python Patterns to Prefer

```python
# Dummy variables
df['above_median'] = (df['x'] > df['x'].median()).astype(int)

# Plotting
fig, ax = plt.subplots()
ax.scatter(df['x'], df['y'], alpha=0.5)
ax.set_xlabel('X'); ax.set_ylabel('Y')
plt.show()

# Regression
model = smf.ols('y ~ x', data=df).fit()
print(model.summary())
```
