import json


def csv_to_records(text: str) -> list[dict]:
    """Разбирает CSV с заголовком; все значения остаются строками."""
    data = []
    lines = text.splitlines()
    if not lines:
        return data

    head, *lines = lines
    head = head.split(",")
    for line in lines:
        if not line.strip():
            continue
        line = line.split(",")
        record = {}
        for i in range(len(head)):
            record[head[i]] = line[i]
        data.append(record)
    return data


def _parse_value(value: str):
    """Преобразует значение настройки в число, bool или строку."""
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False

    # Сначала пробуем целое число, затем дробное.
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def parse_settings(lines: list[str]) -> dict:
    """Разбирает учебный YAML без вложенности и без модуля yaml."""
    records = {}
    list_key = None
    for line in lines:
        # Убираем комментарий и пробелы; пустые строки пропускаем.
        line = line.split("#", 1)[0].strip()
        if not line:
            continue

        if line.startswith("- "):
            value = line[2:].strip()
            records[list_key].append(_parse_value(value))
            continue

        # Делим только по первому двоеточию: остальные могут быть в тексте.
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            records[key] = []
            list_key = key
        else:
            records[key] = _parse_value(value)
            list_key = None
    return records


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи из справочника, сохраняя приоритет самой записи."""
    data = []
    for row in rows:
        # Если совпадения нет, берём пустой словарь.
        combined = extra.get(row[key], {}).copy()
        # Поля исходной записи добавляем последними: они важнее справочника.
        combined.update(row)
        data.append(combined)
    return data


def records_to_json(records: list[dict]) -> str:
    """Возвращает читаемый JSON с кириллицей и отсортированными ключами."""
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
