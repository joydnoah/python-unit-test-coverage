import os
import sys
import json
import coverage
import github

def get_color(total):
    if total > 80:
        return "brightgreen"
    if total > 30 and total < 80:
        return "orange"
    return "red"

cov = coverage.coverage()
cov.load()

with open(os.devnull, "w") as f:
    total = cov.report(file=f)

print(total)
total = round(total, 2)

API_TOKEN = sys.argv[1]
GIST_ID = sys.argv[2]

gh = github.Github(API_TOKEN)
gist = gh.get_gist(GIST_ID)
gist.edit(
    description="new description",
    files={
        "coverage.json": github.InputFileContent(
            content=json.dumps({
                "schemaVersion":1,
                "label": "coverage",
                "message": f"{total}%",
                "color": get_color(total)
            })
        )
    },
)