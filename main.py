import pandas as pd
import argparse


def remove_query_string(url_series):
    # Sử dụng vectorized str.partition để tách nhanh hơn
    return url_series.str.partition('?')[0]


def process_excel(input_path, output_path):
    # Đọc chỉ cột 'url' để tiết kiệm bộ nhớ nếu có thể
    try:
        df = pd.read_excel(input_path, usecols=['url'])
    except ValueError:
        raise ValueError("Không tìm thấy cột 'url' trong file excel.")

    df['url'] = remove_query_string(df['url'])
    df = df.drop_duplicates(subset='url', ignore_index=True)
    df.to_excel(output_path, index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process Excel file to remove query strings from URLs.')
    parser.add_argument('--input', '-i', type=str, default='input.xlsx', help='Input Excel file path')
    parser.add_argument('--output', '-o', type=str, default='group_urls.xlsx', help='Output Excel file path')
    args = parser.parse_args()

    process_excel(args.input, args.output)