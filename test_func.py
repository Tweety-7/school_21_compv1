import unittest
from comp import main_m

str_help = '"Для отображения информации о возможности программы: python computorv1 -h", "для отображение промежуточных шагов -s",\
          "для чтения выражения из файла -f", "для отображение ошибок входа -v",\
          "неравенство должно быть квадратным и не содержать отрицательных стеепней", "общий вид выражения: a*x^2 + b*x^1 +c = 0",\
          "я справлюсь с вещественными числами и сокращением подобных членов,", "смогу вывести ирроцианальные корни и переживу, если ты пропустишь * или ^ для первой степени",\
          "давай поиграем кто быстрее? введи: python comp.py x^2 + 3x - 4 = 0"'


class MainTestCase(unittest.TestCase):
    """тесты для мейн"""
    def test_first(self):
        """ вывод хелпа при пустом входе"""
        help_f = main_m(inarg=['comp.py'])
        self.assertAlmostEqual(help_f, str_help)

if __name__ == "__name__":
    print(str_help)
unittest.main()
