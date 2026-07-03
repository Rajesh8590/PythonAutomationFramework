import argparse
import subprocess
import sys
from datetime import datetime

import os

print("JAVA_HOME =", os.environ.get("JAVA_HOME"))
print("PATH =", os.environ.get("PATH"))
parser = argparse.ArgumentParser()
parser.add_argument("--suite", default="smoke")
args = parser.parse_args()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

results = f"reports/{args.suite}_{timestamp}/allure-results"
report = f"reports/{args.suite}_{timestamp}/allure-report"

ALLURE = r"C:\Program Files\allure-2.44.0\bin\allure.bat"

# Run pytest
subprocess.run([
    sys.executable,
    "-m",
    "pytest",
    "-m",
    args.suite,
    "--alluredir=" + results
], check=True)

# Generate report
subprocess.run([
    ALLURE,
    "generate",
    results,
    "-o",
    report,
    "--clean"
], check=True)

# Open report
'''subprocess.run([
    ALLURE,
    "open",
    report
], check=True)'''