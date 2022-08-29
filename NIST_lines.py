import argparse
from NIST_Line import NIST_line


def initParser():
    parser = argparse.ArgumentParser(description="To jest opis")
    parser.add_argument('element', help='Name of element from NIST Database',type=str)
    parser.add_argument('line', help='Value of wavelength to be searched', type=float)
    parser.add_argument('n', help='Number of wavelengths to be searched', type=float)
    parser.add_argument('filename', help='Name of the file with output', type=str)
    parser.add_argument('--low_w', help='Minimum wavelength value', type=int, default=200)
    parser.add_argument('--upper_w', help='Maximum wavelength value', type=int, default=900)
    parser.add_argument('--sp_num', help='List of ionization stages', nargs='+', type=int, default=[1,2])

    return parser


if __name__ == '__main__':
    parser = initParser()
    args = parser.parse_args()
    line = NIST_line(element=args.element, low_w=args.low_w, upper_w=args.upper_w, sp_num=args.sp_num)
    print(args)
