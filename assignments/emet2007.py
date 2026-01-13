import numpy as np
def t_test(x1, x2):
    numerator = x1.mean() - x2.mean()  # aka point estimate
    se1 = x1.std() / np.sqrt(len(x1))
    se2 = x2.std() / np.sqrt(len(x2))
    denominator = np.sqrt(se1**2 + se2**2)
    t_stat = numerator / denominator  # our t statistic
    ci_lb = numerator - 1.96 * denominator  # lower bound
    ci_ub = numerator + 1.96 * denominator  # upper bound
    ci = (ci_lb, ci_ub)
    print('Two-sample t-test')
    print(f'Mean in group 1: {x1.mean()}')
    print(f'Mean in group 2: {x2.mean()}')
    print(f'Point estimate for difference in means: {numerator}')
    print(f'Test statistic: {t_stat}')
    print(f'95% confidence interval: {ci}')
    return numerator, t_stat, ci
