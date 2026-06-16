def start(input_val: str) -> str:
    start = 0
    end = 1
    result = []
    while start < len(input_val):
        current = input_val[start]
        while end < len(input_val) and current == input_val[end]:
            end += 1

        result.append(f"{end - start}{current}")
        start = end

    return "".join(result)


if __name__ == "__main__":
    input_val = "AAAAAA"
    output_val = "5A4B3C"
    print(start(input_val))
