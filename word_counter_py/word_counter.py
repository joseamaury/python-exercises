def count_text_metrics(text: str) -> dict:
    # Calculate basic text metrics
    chars_total = len(text)
    chars_no_spaces = len(text.replace(" ", ""))
    words = len(text.split())
    lines = 0 if not text else text.count("\n") + 1
    sentences = sum(text.count(p) for p in (".", "!", "?"))

    return {
        "chars_total": chars_total,
        "chars_no_spaces": chars_no_spaces,
        "words": words,
        "lines": lines,
        "sentences": sentences,
    }


def letter_frequency(text: str, ignore_case: bool = True) -> dict:
    # Count letter frequency (A-Z)
    if ignore_case:
        text = text.lower()

    freq = {}
    for ch in text:
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1

    return dict(sorted(freq.items()))


def print_menu() -> None:
    # Display user options
    print("\nChoose an option:")
    print("1) Characters (with spaces)")
    print("2) Characters (without spaces)")
    print("3) Words")
    print("4) Lines")
    print("5) Sentences (approx.)")
    print("6) Full summary")
    print("7) Letter frequency")
    print("0) Exit")


def main() -> None:
    print("=== Text Counter ===")
    text = input("Type your text here:\n> ").strip()

    if not text:
        print("No text provided. Exiting.")
        return

    metrics = count_text_metrics(text)

    while True:
        print_menu()
        choice = input("\nOption: ").strip()

        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            print(f"\nCharacters (with spaces): {metrics['chars_total']}")
        elif choice == "2":
            print(f"\nCharacters (without spaces): {metrics['chars_no_spaces']}")
        elif choice == "3":
            print(f"\nWords: {metrics['words']}")
        elif choice == "4":
            print(f"\nLines: {metrics['lines']}")
        elif choice == "5":
            print(f"\nSentences (approx.): {metrics['sentences']}")
        elif choice == "6":
            print("\n--- Summary ---")
            for key, value in metrics.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        elif choice == "7":
            freq = letter_frequency(text)
            for letter, count in freq.items():
                print(f"{letter}: {count}")
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()