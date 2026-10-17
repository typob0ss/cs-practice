import math


def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}: {line!r}")

    city, temp_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if not city or not date:
        raise ValueError(f"Город и дата не могут быть пустыми: {line!r}")

    try:
        temp = float(temp_str)
    except ValueError as err:
        raise ValueError(f"Некорректная температура {temp_str!r}: {line!r}") from err

    if math.isnan(temp) or math.isinf(temp):
        raise ValueError(f"Температура должна быть конечным числом: {line!r}")

    return {
        "city": city,
        "temperature": temp,
        "date": date,
    }


def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        totals[city] = totals.get(city, 0.0) + temp
        counts[city] = counts.get(city, 0) + 1

    return {city: round(totals[city] / counts[city], 1) for city in totals}


def warmest_city(records: list[dict]) -> str:
    if not records:
        raise ValueError("Список записей пуст")

    averages = average_by_city(records)
    best_city, _ = min(averages.items(), key=lambda item: (-item[1], item[0]))
    return best_city
