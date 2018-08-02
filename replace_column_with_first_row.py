#Chunk'a code
def replace_column_headers_with_first_row(df, split_variable, row_replacing_column_header):
    """
    :param df: DataFrame with no column headers or unnecessary columns headers
    :param split_variable: string variable on which we need to split
    :param row_replacing_column_header: integer denoting row iof dataframe
    """
    if [len(x.split(split_variable)) for x in df_column_list].count(1) == len(df_column_list):
        df.columns = df.iloc[row_replacing_column_header]
        df = df.drop(df.index[row_replacing_column_header])
    return df