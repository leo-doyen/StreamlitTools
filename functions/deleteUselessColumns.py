def drop_useless_col(df):
    col_to_drop=[]
    new_df=df
    for col in df.columns:
        #print(col)
        #print(df[col].dtypes)
        #print(df[col].value_counts())
        print('____________________________-')
        if len(df[col].value_counts()) <= 1:
            print(df[col].value_counts())
            col_to_drop.append(col)
        elif len(df[col].value_counts()) == 2:
            print('cas de deux')
            print(col)
            print(df[col].value_counts(normalize=True))
            #print(df[col].value_counts(normalize=True)[1])
            if df[col].value_counts(normalize=True)[0]<0.1 :
                line_to_drop= (df[col].value_counts().reset_index().iloc[0])[0]
                print('modalitée à supprimer::',line_to_drop)
                col_to_drop.append(col)
                new_df=new_df[df[col] != line_to_drop]
            elif df[col].value_counts(normalize=True)[1]<0.1:
                line_to_drop= (df[col].value_counts().reset_index().iloc[1])[0]
                print('modalitée à supprimer::',line_to_drop)
                col_to_drop.append(col)
                new_df=new_df[new_df[col] != line_to_drop]
                print(new_df[col].value_counts())
    print('colonnes to drop   ',col_to_drop)  
    return new_df.drop(col_to_drop, axis=1)
# drop_useless_col()