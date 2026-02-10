const express = require("express");
require("dotenv").config();

const connectDB = require("./src/config/db");
const diaryRoutes = require("./src/routes/diary.routes");

const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  res.json({ ok: true });
});

app.use("/diary", diaryRoutes);

const PORT = process.env.PORT || 3000;

(async () => {
  await connectDB(process.env.MONGODB_URI);

  app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
  });
})();

