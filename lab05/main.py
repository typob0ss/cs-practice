from pathlib import Path

from logstats import count_levels, format_report, top_errors

TOP_ERRORS_COUNT = 3


def main() -> None:
    path = input().strip()

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, TOP_ERRORS_COUNT)

    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))

    report_path = Path(__file__).parent / "report.txt"
    with open(report_path, "w", encoding="utf-8") as report:
        report.write(format_report(counts, errors))


if __name__ == "__main__":
    main()
