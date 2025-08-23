🎰 USA Lottery Number Generator

A Flask web application that generates 5 sets of Mega Millions lottery numbers for USA using various generation methods including random, frequency analysis, and past winner selection.

## ✨ Features

- **5 Sets Generation**: Generates 5 different Mega Millions number combinations at once
- **Multiple Generation Methods**:
  - Random Numbers: Completely random selection
  - Frequency-Based: Uses historical data to pick most frequent numbers
  - Past Winner: Selects from previous winning combinations
- **Date Selection**: Choose a reference date for historical analysis
- **Interactive UI**: Clean, responsive design with gradient backgrounds
- **Clear & Regenerate**: Easy button to clear results and generate new numbers
- **Mobile Friendly**: Responsive design that works on all devices

## 🎯 How It Works

1. Select a reference date
2. Choose your preferred generation method
3. Click "Generate My Numbers!" 
4. View your 5 sets of Mega Millions numbers (5 white balls + 1 mega ball each)
5. Use "Clear & Generate New Numbers" to get fresh combinations

## 🚀 Live Demo

This app is deployed on Replit and ready to use! Simply click the Run button to start the Flask server.

## 📋 Requirements

- Python 3.10+
- Flask 2.2.0+
- Modern web browser

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/nc-lottery-generator.git
   cd nc-lottery-generator
   ```

2. **Install dependencies** (automatically handled by Replit):
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

4. **Access the app**:
   - Local: `http://localhost:5000`
   - Replit: Use the provided web preview URL

## 📁 Project Structure

```
nc-lottery-generator/
├── main.py                 # Flask application main file
├── templates/
│   └── lottery.html        # Web interface template
├── pyproject.toml          # Python dependencies
├── .replit                 # Replit configuration
└── README.md               # This file
```

## 🎲 Generation Methods

### Random Numbers
- Generates completely random Mega Millions combinations
- White balls: 1-70 (5 numbers)
- Mega ball: 1-25 (1 number)

### Frequency-Based
- Analyzes mock historical data to find most frequent numbers
- Selects numbers that have appeared most often in past draws
- Uses frequency analysis for both white balls and mega ball

### Past Winner
- Randomly selects from previous winning combinations
- Uses mock historical data for demonstration
- Gives you numbers that have actually won before

## 🔧 Technical Details

- **Backend**: Python Flask framework
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: CSS Grid/Flexbox with gradient designs
- **Data**: Mock lottery API simulation (ready for real API integration)
- **Responsive**: Mobile-first design approach

## 🌟 Key Features

- **Real-time Generation**: Instant number generation via AJAX
- **Error Handling**: Comprehensive error management
- **User Experience**: Intuitive interface with visual feedback
- **Cross-platform**: Works on desktop, tablet, and mobile
- **No Database Required**: Runs entirely in-memory

## 🚀 Deployment on Replit

This project is optimized for Replit deployment:

1. Fork this repository
2. Open in Replit
3. Click the Run button
4. Your lottery generator is live!

The app automatically binds to `0.0.0.0:5000` for Replit compatibility.

## 📊 Mock Data

The application currently uses mock historical lottery data for demonstration. In a production environment, you would integrate with:

- Official NC Lottery API
- Lottery data providers
- Historical winning number databases

## 🎨 Customization

### Styling
- Modify `templates/lottery.html` for UI changes
- Update CSS variables for color schemes
- Responsive breakpoints can be adjusted

### Generation Logic
- Add new generation methods in `main.py`
- Modify number ranges for different lottery types
- Integrate real lottery APIs

## 🔮 Future Enhancements

- [ ] Real lottery API integration
- [ ] Statistical analysis dashboard
- [ ] Number pattern visualization
- [ ] Lucky number saving
- [ ] Multiple lottery game support
- [ ] Historical win rate tracking

## 📝 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For questions or issues:
- Create an issue on GitHub
- Contact through Replit community
- Check the [Replit documentation](https://docs.replit.com)

## ⚠️ Disclaimer

This is a number generator for entertainment purposes only. Playing the lottery should be done responsibly. This tool does not guarantee winning numbers or improve your chances of winning.

---

**Good luck with your lottery numbers! 🍀**
