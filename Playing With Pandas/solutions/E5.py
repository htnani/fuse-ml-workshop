df.groupby(by=['Survived', 'Pclass'])['Pclass'].count().unstack('Survived').plot(kind='bar')
