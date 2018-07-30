mode_embarked = new_df['Embarked'].mode()
new_df['Embarked'] = new_df['Embarked'].fillna(mode_embarked[0])
