import re
from pathlib import Path


class File:
    def __init__(self):
        self.filename = "readme.md"

    def add_header(self) -> None:
        context = "# [Leetcode](https://leetcode.com/u/vkta_tdm/) problem solving"
        self.write_file(context=context, mode="w")

    def add_dir(self, data: str, indent: int):
        data = data.replace("_", " ").title()
        context = f"\n{'    ' * indent}- {data}  "
        self.write_file(context=context, mode="a")

    def add_count(self, data: str):
        context = f" - _{data}_  "
        self.write_file(context=context, mode="a")

    def add_total(self, quantity):
        context = f"\n\n**TOTAL SOLVED**: _{quantity} problems_"
        self.write_file(context=context, mode="a")

    def add_files(self, data: list, indent: int, current_root: Path):
        context = ""
        for itm in data:
            context += (
                f"\n{'    ' * indent}- [x] "
                f"[{itm.name.replace("_", " ").replace(".py", "")}]"
                f"({itm.relative_to(current_root)})  "
            )
        self.write_file(context=context, mode="a")

    def write_file(self, context: str, mode: str) -> None:
        with open(self.filename, mode) as f:
            f.write(context)


class Statistics:
    def __init__(self, path: Path):
        self.path = path
        self.file: File = File()
        self.total: int = 0
        self.exceptions: list = ["test", "create_tree", "linked_list"]
        self.create_statistic()

    def create_statistic(self) -> None:
        self.file.add_header()
        self.go_by_dirs(path=self.path)
        self.file.add_total(self.total)

    def go_by_dirs(self, path: Path, indent: int = 0) -> None:
        directories = [
            itm
            for itm in path.iterdir()
            if not re.search(r"^\.|__\w+", itm.name)
            and all(i not in itm.name for i in self.exceptions)
        ]

        files = []

        if path != self.path:
            self.file.add_dir(data=path.name, indent=indent)
            indent += 1

        for itm in directories:
            if itm.is_file() and path != self.path:
                files.append(itm)
            elif itm.is_dir():
                self.go_by_dirs(path=itm, indent=indent)
        if files:
            quantity = len(files)
            self.file.add_count(quantity)
            self.file.add_files(data=files, indent=indent, current_root=self.path)
            self.total += quantity


if __name__ == "__main__":
    s = Statistics(Path(__file__).parent)
