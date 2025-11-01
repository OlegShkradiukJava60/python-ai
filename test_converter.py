from unittest import TestCase, main
from pandas import DataFrame
from converter import enumerator, columnsMapper, convertX

class TestConverter(TestCase):
    def setUp(self):
        self.df = DataFrame({
            "Company": ['Toyota', 'Toyota', 'Hundai', 'Hundai', 'Hundai'],
            "Model":   ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']
        })

    def test_enumerator(self):
        expected = {
            'Toyota': 0,
            'Hundai': 1
        }
        actual = enumerator(self.df['Company'].unique())
        self.assertEqual(expected, actual)

    def test_columnsMapper(self):
        cmap = columnsMapper(['Company', 'Model'], self.df)
        self.assertEqual({'Toyota': 0, 'Hundai': 1}, cmap['Company'])
        self.assertEqual(
            {'Camry': 0, 'Corolla': 1, 'i10': 2, 'Elantra': 3, 'Kona': 4},
            cmap['Model']
        )

    def test_convertX(self):
        mapper = {
            'Company': {'Toyota': 0, 'Hundai': 1},
            'Model':   {'Camry': 0, 'Corolla': 1, 'i10': 2, 'Elantra': 3, 'Kona': 4}
        }
        df_converted = convertX(self.df, mapper)
        expected = {"Company": [0, 0, 1, 1, 1], "Model": [0, 1, 2, 3, 4]}
        self.assertEqual(expected, df_converted.to_dict(orient="list"))

if __name__ == '__main__':
    main()
