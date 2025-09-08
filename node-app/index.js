const express = require("express");
const app = express();
const PORT = 3000;

// simple route
app.get("/", (req, res) => {
  res.send("Hello from Express server!");
});

// bind to all interfaces
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Express server running on port ${PORT}`);
});
