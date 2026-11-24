"""Entry: the single letter Z, for "zero sleep", in "One Letter for Your Day"."""

from pathlib import Path

LETTER = "Z"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"
    output_file.write_bytes(LETTER.encode("ascii"))
    if output_file.read_bytes() != b"Z":
        raise SystemExit("Output verification failed: entry.txt must contain exactly b'Z'.")


if __name__ == "__main__":
    main()
