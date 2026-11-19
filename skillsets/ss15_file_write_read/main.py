
"""runs functions file"""
import functions as f


def main():
    """program entry"""

    f.get_requirements()

    help(f.write_read_file)
    help(f.file_write)
    help(f.file_read)

    f.write_read_file()


if __name__ == "__main__":
    main()
