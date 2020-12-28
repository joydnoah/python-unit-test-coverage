import coverage
import os
cov = coverage.coverage()
cov.load()

with open(os.devnull, "w") as f:
    total = cov.report(file=f)

os.environ["COVERAGE"] = str(total)