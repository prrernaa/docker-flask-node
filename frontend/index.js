const express = require("express");
const axios   = require("axios");
const path    = require("path");

const app  = express();
const PORT = 3000;
const FLASK_URL = process.env.FLASK_URL || "http://backend:5000";

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
  res.render("index", { error: null, success: null });
});

app.post("/submit", async (req, res) => {
  const { name, email, message } = req.body;
  if (!name || !email || !message) {
    return res.render("index", { error: "All fields are required.", success: null });
  }
  try {
    const response = await axios.post(`${FLASK_URL}/submit`, { name, email, message });
    res.render("success", { message: response.data.message });
  } catch (err) {
    const errorMsg = err.response?.data?.message || "Something went wrong.";
    res.render("index", { error: errorMsg, success: null });
  }
});

app.listen(PORT, () => {
  console.log(`Frontend running on http://localhost:${PORT}`);
});
