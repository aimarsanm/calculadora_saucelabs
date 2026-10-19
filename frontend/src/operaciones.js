export const OPERACIONES = [
  { simbolo: '+', etiqueta: 'Suma (+)', unaria: false },
  { simbolo: '-', etiqueta: 'Resta (-)', unaria: false },
  { simbolo: '*', etiqueta: 'Multiplicación (*)', unaria: false },
  { simbolo: '/', etiqueta: 'División (/)', unaria: false },
  { simbolo: '**', etiqueta: 'Potencia (**)', unaria: false },
  { simbolo: '//', etiqueta: 'División entera (//)', unaria: false },
  { simbolo: '%', etiqueta: 'Módulo (%)', unaria: false },
  { simbolo: '√', etiqueta: 'Raíz cuadrada (√)', unaria: true },
  { simbolo: 'c', etiqueta: 'Cubo (c)', unaria: true },
  { simbolo: '√3', etiqueta: 'Raíz cúbica (√3)', unaria: true },
  { simbolo: 'cbrt', etiqueta: 'Raíz cúbica (cbrt)', unaria: true },
  { simbolo: 'abs', etiqueta: 'Valor absoluto (abs)', unaria: true },
  { simbolo: 'neg', etiqueta: 'Negación (neg)', unaria: true },
  { simbolo: 'ln', etiqueta: 'Logaritmo natural (ln)', unaria: true },
];

function comprobarDivisorNoNulo(divisor) {
  if (divisor === 0) {
    throw new Error('No se puede dividir entre cero.');
  }
}

export function calcular(numero1, numero2, operacion) {
  switch (operacion) {
    case '+':
      return numero1 + numero2;
    case '-':
      return numero1 - numero2;
    case '*':
      return numero1 * numero2;
    case '/':
      comprobarDivisorNoNulo(numero2);
      return numero1 / numero2;
    case '**':
      return numero1 ** numero2;
    case '//':
      comprobarDivisorNoNulo(numero2);
      return Math.floor(numero1 / numero2);
    case '%':
      comprobarDivisorNoNulo(numero2);
      return ((numero1 % numero2) + numero2) % numero2;
    case '√':
      if (numero1 < 0) {
        throw new Error('La raíz cuadrada de un número negativo no es real.');
      }
      return Math.sqrt(numero1);
    case 'c':
      return numero1 ** 3;
    case '√3':
    case 'cbrt':
      return Math.cbrt(numero1);
    case 'abs':
      return Math.abs(numero1);
    case 'neg':
      return -numero1;
    case 'ln':
      if (numero1 <= 0) {
        throw new Error('El logaritmo natural requiere un número positivo.');
      }
      return Math.log(numero1);
    default:
      throw new Error('Operación inválida.');
  }
}
