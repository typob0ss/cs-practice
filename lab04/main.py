import sys
from stats import average_by_city, read_valid, warmest_city


def main() -> None:
    lines = sys.stdin.read().splitlines()

    non_empty_lines = [line for line in lines if line.strip()]
    valid_records = read_valid(lines)
    skipped_count = len(non_empty_lines) - len(valid_records)

    print(len(valid_records))
    print(skipped_count)

    if valid_records:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        print(f"{averages[best_city]:.1f}")


if __name__ == "__main__":
    main()
