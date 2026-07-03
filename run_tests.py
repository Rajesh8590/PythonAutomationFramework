import argparse
import subprocess
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("--suite", default="smoke")

args = parser.parse_args()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

results = f"reports/{args.suite}_{timestamp}/allure-results"
report = f"reports/{args.suite}_{timestamp}/allure-report"

ALLURE = r"C:\Program Files\allure-2.44.0\bin\allure.bat"

# STEP 1 - Run pytest
subprocess.run([
    "pytest",
    "-m",
    args.suite,
    "--alluredir=" + results
], check=True)

# STEP 2 - Generate Allure Report
subprocess.run([
    ALLURE,
    "generate",
    results,
    "-o",
    report,
    "--clean"
], check=True)

# STEP 3 - Open Report
subprocess.run([
    ALLURE,
    "open",
    report
], check=True)