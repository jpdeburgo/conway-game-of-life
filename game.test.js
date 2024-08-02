const { Game } = require("./game.js");
test("testGameStartsOnButtonPress", () => {
  const game = new Game();
  expect(game.start()).toEqual("Game started");
});
