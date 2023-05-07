from typing import List, Literal, Optional


def parse_bullet_list(list_str: str) -> Optional[List[str]]:
    try:
        if list_str is None:
            return []
        if list_str.strip() == "":
            return []
        list_str = list_str.replace("\n*", "\n-")
        items = list_str.split("\n-")
        items = [line.strip().strip("- \n\t").strip("* \n\t") for line in items]
        items = [line for line in items if line != ""]
        if len(items) == 0:
            return []
        return items
    except Exception as e:
        return []


def select_testing_framework_from_str(data_str: str) -> Literal["pytest", "unittest"]:
    if "unittest" in data_str.lower():
        return "unittest"
    else:
        return "pytest"