const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files
app.use(express.static(path.join(__dirname)));

// API endpoint to get carousel images
app.get('/api/carousel-images', (req, res) => {
  const carouselDir = path.join(__dirname, 'img', 'carousel');
  
  try {
    const files = fs.readdirSync(carouselDir)
      .filter(file => /\.(png|jpg|jpeg|gif|webp)$/i.test(file))
      .sort();
    
    res.json(files);
  } catch (error) {
    console.error('Error reading carousel directory:', error);
    res.status(500).json({ error: 'Failed to read carousel images' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
