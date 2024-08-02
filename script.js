import { Game } from "./game.js";

const table = document.getElementById("board");

function createTable(tableData) {
  const table = document.createElement("table");
  const tableBody = document.createElement("tbody");

  tableData.forEach(function (rowData) {
    const row = document.createElement("tr");

    rowData.forEach(function (cellData) {
      const cell = document.createElement("td");
      cell.appendChild(document.createTextNode(cellData));
      row.appendChild(cell);
    });

    tableBody.appendChild(row);
  });

  table.appendChild(tableBody);
  document.body.appendChild(table);
}

createTable([
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 1, 1, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0],
]);

const game = new Game(table);

game.start();
