from django.test import TestCase
from .models import GuessNumbers
# Create your tests here.
class GuessNumbersTestCase(TestCase):

    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected number')
        g.generate() # 로또 번호 생성
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lottos) > 20) # 20개 이상의 로또 번호가 생성되었는지 확인
# TDD : Test Driven Development
