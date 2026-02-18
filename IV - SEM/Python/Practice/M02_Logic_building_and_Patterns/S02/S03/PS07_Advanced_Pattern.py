def inverted_left(n: int) -> None:
    """Print a left-aligned inverted right-angled triangle of height `n`."""
    for i in range(n, 0, -1):
        print('*' * i)


def inverted_right_aligned(n: int) -> None:
    """Print a right-aligned inverted right-angled triangle of height `n`."""
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * i)


def main() -> None:
    """Simple CLI: first token is size, optional second token is 'left' or 'right'."""
    try:
        raw = input('Enter size (positive integer, optionally followed by space and "left" or "right"): ').strip().split()
        if not raw:
            print('No input provided.')
            return
        n = int(raw[0])
        align = raw[1].lower() if len(raw) > 1 else 'left'
        if n <= 0:
            print('Enter a positive integer.')
            return
        if align.startswith('r'):
            inverted_right_aligned(n)
        else:
            inverted_left(n)
    except ValueError:
        print('Invalid input.')


if __name__ == '__main__':
    main()

