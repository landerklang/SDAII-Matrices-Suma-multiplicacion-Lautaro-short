const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.post("/calcular", (req, res) => {
  const { matriz1, matriz2, operacion } = req.body;

  let resultado = [];

  if (operacion === "suma") {
    for (let i = 0; i <= matriz1.length; i++) {
      let fila = [];

      for (let j = 0; j <= matriz1[i].length; j++) {
        fila.push(matriz1[i][j] + matriz2[i][j]);
      }

      resultado.push(fila);
    }
  }

  res.json({ resultado });
});

app.listen(3000, () => {
  console.log("Servidor corriendo en http://localhost:3000");
});
