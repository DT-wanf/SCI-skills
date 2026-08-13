from pathlib import Path
import json
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
errors: list[str] = []


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        capture_output=True,
        check=False,
    )


with tempfile.TemporaryDirectory() as temp_dir:
    temp = Path(temp_dir)

    data = temp / "data.csv"
    data.write_text(
        "group,value,note\nA,1.0,ok\nA,2.0,ok\nB,3.0,\nB,NA,check\n",
        encoding="utf-8",
    )
    profiled = run(str(SCRIPTS / "profile_figure_data.py"), str(data), "--group", "group")
    if profiled.returncode != 0:
        errors.append(f"profile_figure_data failed: {profiled.stderr or profiled.stdout}")
    else:
        report = json.loads(profiled.stdout)
        if report.get("rows") != 4 or report.get("group_counts", {}).get("group") != {"A": 2, "B": 2}:
            errors.append("profile_figure_data returned unexpected counts")

    good_source = temp / "figure.py"
    good_source.write_text(
        "import pandas as pd\nimport matplotlib.pyplot as plt\n"
        "df = pd.read_csv('data.csv')\nfig, ax = plt.subplots()\n"
        "ax.plot(df['value'])\nfig.savefig('figure.svg')\n",
        encoding="utf-8",
    )
    validated = run(
        str(SCRIPTS / "validate_figure_source.py"),
        str(good_source),
        "--result-figure",
        "--json",
    )
    if validated.returncode != 0:
        errors.append(f"valid result source rejected: {validated.stdout}")
    else:
        report = json.loads(validated.stdout)
        if report.get("status") != "PASS_WITH_WARNINGS" or not report.get("reads_input"):
            errors.append("valid source did not receive expected execution warning")

    bad_source = temp / "bad.py"
    bad_source.write_text(
        "import matplotlib.pyplot as plt\nplt.plot([1, 2, 3])\nplt.savefig('fake.png')\n",
        encoding="utf-8",
    )
    rejected = run(
        str(SCRIPTS / "validate_figure_source.py"),
        str(bad_source),
        "--result-figure",
        "--json",
    )
    if rejected.returncode == 0:
        errors.append("result source without real input was accepted")

    svg = temp / "figure.svg"
    svg.write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="89mm" height="60mm" viewBox="0 0 89 60">'
        '<text x="5" y="10">Result</text></svg>',
        encoding="utf-8",
    )
    inspected = run(str(SCRIPTS / "inspect_figure_output.py"), str(svg))
    if inspected.returncode != 0:
        errors.append(f"inspect_figure_output failed: {inspected.stdout}")
    else:
        report = json.loads(inspected.stdout)
        details = report.get("details", {})
        if details.get("format") != "SVG" or details.get("editable_text_elements") != 1:
            errors.append("SVG inspection returned unexpected metadata")

if errors:
    print("FIGURE TOOL TESTS FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("FIGURE TOOL TESTS PASSED")
print("Tools checked: 3")
