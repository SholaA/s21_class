def remove_list_item(*, the_list, the_item):
  new_list = [item for item in the_list if item != the_item]
  return new_list

def plot_x_by_class_y(*, table, x_column, y_column):
  assert isinstance(table, pd.core.frame.DataFrame), f'table is not a dataframe but instead a {type(table)}'
  assert x_column in table.columns, f'unrecognized column: {x_column}. Check spelling and case.'
  assert y_column in table.columns, f'unrecognized column: {y_column}. Check spelling and case.'
  assert table[y_column].nunique()<=5, f'y_column must be of 5 categories or less but has {table[y_column].nunique()}'

  pd.crosstab(table[x_column], table[y_column]).plot(kind='bar', figsize=(15,8), grid=True, logy=True)
  return None
