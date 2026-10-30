from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "test_logs"
OUT.mkdir(parents=True, exist_ok=True)

result = subprocess.run(
    [sys.executable, "-m", "pytest", "-v", "--junitxml", str(OUT / "junit.xml")],
    cwd=ROOT,
    text=True,
    capture_output=True,
)
log = OUT / "pytest_run.txt"
# Keep successful test output clean; Python startup diagnostics from the host
# environment are not part of the test result.
content = result.stdout
if result.returncode != 0 and result.stderr:
    content += "\n" + result.stderr
log.write_text(content, encoding="utf-8")
print(result.stdout)
print(f"Exit code: {result.returncode}; log: {log}")
sys.exit(result.returncode)
