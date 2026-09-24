import subprocess
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python run_scenario.py <path/to/v1.conf>")

    config_path = Path(sys.argv[1])

    if not config_path.is_file():
        raise SystemExit(f"Config not found: {config_path}")

    scenario_dir = config_path.parent
    ratio_path = scenario_dir / "result_ratio.json"

    subprocess.run(
        ["locust", f"--config={config_path}"],
        check=True,
    )

    with ratio_path.open("w", encoding="utf-8") as ratio_file:
        subprocess.run(
            [
                "locust",
                f"--config={config_path}",
                "--show-task-ratio-json",
            ],
            stdout=ratio_file,
            check=True,
        )

    print(f"Ratio saved to: {ratio_path}")


if __name__ == "__main__":
    main()