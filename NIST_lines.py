import argparse
from NIST_Line import NIST_Line


def initParser():
    parser = argparse.ArgumentParser(description="NIST Database webscraping searches for closest lines.")
    parser.add_argument('element', help='Name of element from NIST Database',type=str)
    parser.add_argument('line', help='Value of wavelength to be searched', type=float)
    parser.add_argument('n', help='Number of wavelengths to be searched', type=int)
    parser.add_argument('filename', help='Name of the file with output', type=str)
    parser.add_argument('--low_w', help='Minimum wavelength value', type=int, default=200)
    parser.add_argument('--upper_w', help='Maximum wavelength value', type=int, default=900)
    parser.add_argument('--sp_num', help='List of ionization stages', nargs='+', type=int, default=[1,2])
    parser.add_argument('--threshold', help='Intensity threshold', type=float, default=0)

    return parser


if __name__ == '__main__':
    parser = initParser()
    args = parser.parse_args()
    if (args.low_w in range(199, 901)) & (args.upper_w in range(199, 901)):
        line = NIST_Line(element=args.element, low_w=args.low_w, upper_w=args.upper_w, sp_num=args.sp_num)
        lines_df = line.search_n_nearest_lines(args.line, args.n)
        lines_df.to_csv(args.filename+'.csv')
    else:
        print('Wavelength must be in range 200-900 nm, check low_w, upper_w parameters')

