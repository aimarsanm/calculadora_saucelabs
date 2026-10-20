import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

URL_FRONTEND = os.environ.get('FRONTEND_URL', 'http://192.168.68.106:5173')
TIMEOUT_SEGUNDOS = 5
SAUCE_URL = 'https://ondemand.eu-central-1.saucelabs.com:443/wd/hub'


class TestFrontendCalculadora(unittest.TestCase):

    def run(self, resultado=None):
        resultado = super().run(resultado)
        fallido = any(caso is self for caso, _ in resultado.failures + resultado.errors)
        if getattr(self, 'driver', None) is not None:
            self.driver.execute_script(f"sauce:job-result={'failed' if fallido else 'passed'}")
            self.driver.quit()
        return resultado

    def setUp(self):
        usuario = os.environ.get('SAUCE_USERNAME')
        clave = os.environ.get('SAUCE_ACCESS_KEY')
        if not usuario or not clave:
            self.fail('Define las variables de entorno SAUCE_USERNAME y SAUCE_ACCESS_KEY.')

        opciones = ChromeOptions()
        opciones.browser_version = 'latest'
        opciones.platform_name = 'Windows 11'
        opciones.set_capability('sauce:options', {
            'username': usuario,
            'accessKey': clave,
            'build': 'calculadora-frontend',
            'name': self.id(),
            'tunnelName': 'mi-tunel-local',
        })
        self.driver = webdriver.Remote(command_executor=SAUCE_URL, options=opciones)
        self.espera = WebDriverWait(self.driver, TIMEOUT_SEGUNDOS)

        self.driver.get(URL_FRONTEND)
        self.espera.until(EC.presence_of_element_located((By.ID, 'calcular')))

    def _texto(self, id_elemento):
        elementos = self.driver.find_elements(By.ID, id_elemento)
        return elementos[0].text if elementos else None

    def _calcular(self, numero1, operacion, numero2=None):
        campo1 = self.driver.find_element(By.ID, 'numero1')
        campo1.clear()
        campo1.send_keys(numero1)

        Select(self.driver.find_element(By.ID, 'operacion')).select_by_value(operacion)

        if numero2 is not None:
            campo2 = self.driver.find_element(By.ID, 'numero2')
            campo2.clear()
            campo2.send_keys(numero2)

        self.driver.find_element(By.ID, 'calcular').click()
        self.espera.until(lambda d: self._texto('resultado') or self._texto('error'))

    def test_titulo_visible(self):
        titulo = self.driver.find_element(By.TAG_NAME, 'h1')
        self.assertEqual('Calculadora', titulo.text)

    def test_suma(self):
        self._calcular('1', '+', '2')
        self.assertEqual('3', self._texto('resultado'))

    def test_resta(self):
        self._calcular('5', '-', '3')
        self.assertEqual('2', self._texto('resultado'))

    def test_multiplicacion(self):
        self._calcular('4', '*', '3')
        self.assertEqual('12', self._texto('resultado'))

    def test_division(self):
        self._calcular('10', '/', '2')
        self.assertEqual('5', self._texto('resultado'))

    def test_division_entre_cero_muestra_error(self):
        self._calcular('10', '/', '0')
        self.assertIsNone(self._texto('resultado'))
        self.assertEqual('No se puede dividir entre cero.', self._texto('error'))

    def test_potencia(self):
        self._calcular('2', '**', '3')
        self.assertEqual('8', self._texto('resultado'))

    def test_division_entera(self):
        self._calcular('7', '//', '2')
        self.assertEqual('3', self._texto('resultado'))

    def test_modulo(self):
        self._calcular('7', '%', '3')
        self.assertEqual('1', self._texto('resultado'))

    def test_raiz_cuadrada_ignora_segundo_operando(self):
        Select(self.driver.find_element(By.ID, 'operacion')).select_by_value('√')
        self.assertFalse(self.driver.find_element(By.ID, 'numero2').is_enabled())

        self._calcular('16', '√')
        self.assertEqual('4', self._texto('resultado'))

    def test_raiz_cuadrada_negativa_muestra_error(self):
        self._calcular('-16', '√')
        self.assertIsNone(self._texto('resultado'))
        self.assertEqual('La raíz cuadrada de un número negativo no es real.', self._texto('error'))

    def test_cubo(self):
        self._calcular('3', 'c')
        self.assertEqual('27', self._texto('resultado'))

    def test_raiz_cubica(self):
        self._calcular('27', 'cbrt')
        self.assertEqual('3', self._texto('resultado'))

    def test_valor_absoluto(self):
        self._calcular('-5', 'abs')
        self.assertEqual('5', self._texto('resultado'))

    def test_negacion(self):
        self._calcular('5', 'neg')
        self.assertEqual('-5', self._texto('resultado'))

    def test_logaritmo_natural_de_cero_muestra_error(self):
        self._calcular('0', 'ln')
        self.assertIsNone(self._texto('resultado'))
        self.assertEqual('El logaritmo natural requiere un número positivo.', self._texto('error'))

    def test_campo_vacio_muestra_error(self):
        self._calcular('', '+', '2')
        self.assertIsNone(self._texto('resultado'))
        self.assertEqual('Introduce un número válido en todos los campos necesarios.', self._texto('error'))

    def test_segundo_campo_se_habilita_en_operaciones_binarias(self):
        Select(self.driver.find_element(By.ID, 'operacion')).select_by_value('abs')
        self.assertFalse(self.driver.find_element(By.ID, 'numero2').is_enabled())

        Select(self.driver.find_element(By.ID, 'operacion')).select_by_value('+')
        self.assertTrue(self.driver.find_element(By.ID, 'numero2').is_enabled())


if __name__ == '__main__':
    unittest.main()