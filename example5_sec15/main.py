from csv_reader import CSVStringTablePrinter
from csv_reader import CSVFileTreePrinter


def execute():
    printer = CSVStringTablePrinter(
        'おはよう,Good Morning\nこんにちは,Good Afternoon\nこんばんは,Good Evening')
    printer.print()
    printer.close()

    printer = CSVFileTreePrinter('example5_sec15/sec15.csv')
    printer.print()
    printer.close()


if __name__ == "__main__":
    execute()
