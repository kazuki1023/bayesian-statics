import numpy as np
import scipy.stats as stats

# 仮想データ
n = 100  # 試行回数
k = 40   # 成功回数
p_hat = k / n  # 成功率

# Wilson Score Intervalの計算
alpha = 0.05
confidence = 1 - alpha
ci_wilson = stats.binom.interval(confidence, n=n, p=p_hat, loc=0)
ci_wilson = [ci_wilson[0] / n, ci_wilson[1] / n]

print(f"Wilson Score Interval: {ci_wilson}")
