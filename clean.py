import pandas as pd
import argparse

def clean(input1, input2, output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)

    merged_data = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    merged_data.drop(['id'], axis=1, inplace=True)

    merged_data.dropna(inplace=True)

    merged_data = merged_data[~merged_data['job'].str.contains('insurance|Insurance')]

    merged_data.to_csv(output, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='respondent_contact.csv file')
    parser.add_argument('input2', help='respondent_other.csv file')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()

    clean(args.input1, args.input2, args.output)