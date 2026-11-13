def count_by_extension(paths: list[str]) -> dict[str, int]:
    extensions = {}
    for path in paths:
        name = path.split("/")[-1]  # only the file name, not the folders
        extension = name.split(".")[-1].lower() if "." in name else ""
        extensions[extension] = extensions.get(extension, 0) + 1
    return extensions


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    # more "/" wins; on a tie the alphabetically smaller path wins
    return min(paths, key=lambda path: (-path.count("/"), path))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size = n_bytes
    unit = 0
    while size >= 1024 and unit < len(units) - 1:
        size /= 1024
        unit += 1
    return f"{size:.1f} {units[unit]}"
