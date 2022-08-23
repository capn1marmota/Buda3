import unittest
from red_de_metro.main import get_data


def main():
    assert get_data('src/red_de_metro/Conexiones.tsv') is header, data
    assert get_data('src/red_de_metro/Estaciones.tsv') is header, data


if __name__ == '__main__':
    unittest.main()
