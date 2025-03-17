def longestCommonPrefix(strings):
    if not strings:
        return "Nenhum"

    prefix = strings[0]

    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return "Nenhum"

    return prefix


if __name__ == "__main__":
    print(f"\nMaior Prefixo Comum: {longestCommonPrefix(['flower', 'flow', 'flight', 'nap'])}\n")
    print(f"\nMaior Prefixo Comum: {longestCommonPrefix(['flower', 'flow', 'flight'])}\n")
