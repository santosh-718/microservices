const express = require('express');
const app = express();

app.use(express.json());

app.get('/health', (req, res) => {
  res.json({ status: 'Order Service is running' });
});

app.get('/orders', (req, res) => {
  res.json([
    { id: 1, userId: 1, product: 'Laptop', amount: 999.99 },
    { id: 2, userId: 2, product: 'Mouse', amount: 29.99 }
  ]);
});

app.post('/orders', (req, res) => {
  res.status(201).json({ message: 'Order created', data: req.body });
});

const PORT = process.env.PORT || 3002;
app.listen(PORT, () => {
  console.log(`Order Service running on port ${PORT}`);
});
