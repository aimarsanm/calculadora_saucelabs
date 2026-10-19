import { useState } from 'react';
import { OPERACIONES, calcular } from './operaciones.js';
import './App.css';

function parsearNumero(texto) {
  if (texto.trim() === '' || Number.isNaN(Number(texto))) {
    return null;
  }
  return Number(texto);
}

function App() {
  const [numero1, setNumero1] = useState('');
  const [numero2, setNumero2] = useState('');
  const [operacion, setOperacion] = useState('+');
  const [resultado, setResultado] = useState(null);
  const [error, setError] = useState('');

  const operacionSeleccionada = OPERACIONES.find((op) => op.simbolo === operacion);
  const esUnaria = operacionSeleccionada.unaria;

  function handleSubmit(evento) {
    evento.preventDefault();
    setResultado(null);
    setError('');

    const valor1 = parsearNumero(numero1);
    const valor2 = esUnaria ? 0 : parsearNumero(numero2);

    if (valor1 === null || valor2 === null) {
      setError('Introduce un número válido en todos los campos necesarios.');
      return;
    }

    try {
      const valorCalculado = calcular(valor1, valor2, operacion);
      if (!Number.isFinite(valorCalculado)) {
        throw new Error('El resultado no es un número finito.');
      }
      setResultado(valorCalculado);
    } catch (e) {
      setError(e.message);
    }
  }

  return (
    <main className="calculadora">
      <h1>Calculadora</h1>

      <form onSubmit={handleSubmit} noValidate>
        <label htmlFor="numero1">Número 1</label>
        <input
          id="numero1"
          type="number"
          step="any"
          value={numero1}
          onChange={(e) => setNumero1(e.target.value)}
        />

        <label htmlFor="operacion">Operación</label>
        <select
          id="operacion"
          value={operacion}
          onChange={(e) => setOperacion(e.target.value)}
        >
          {OPERACIONES.map((op) => (
            <option key={op.simbolo} value={op.simbolo}>
              {op.etiqueta}
            </option>
          ))}
        </select>

        <label htmlFor="numero2">Número 2</label>
        <input
          id="numero2"
          type="number"
          step="any"
          value={numero2}
          disabled={esUnaria}
          onChange={(e) => setNumero2(e.target.value)}
        />

        <button id="calcular" type="submit">
          Calcular
        </button>
      </form>

      {error && (
        <p id="error" className="error" role="alert">
          {error}
        </p>
      )}
      {resultado !== null && (
        <p id="resultado" className="resultado">
          {String(resultado)}
        </p>
      )}
    </main>
  );
}

export default App;
