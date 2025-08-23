
from flask import Flask, render_template, request, jsonify
import requests
import random
from datetime import datetime, timedelta
from collections import Counter
import json

app = Flask(__name__)

# Mock API endpoint - in real implementation, you'd use actual lottery API
LOTTERY_API_BASE = "https://api.lottery.com/v2/draws"  # Example endpoint

@app.route('/')
def index():
    return render_template('lottery.html')

@app.route('/generate', methods=['POST'])
def generate_numbers():
    try:
        selected_date = request.form.get('date')
        generation_method = request.form.get('method', 'random')
        
        # For demo purposes, we'll simulate API data since actual lottery APIs often require keys
        # In production, you'd replace this with actual API calls
        historical_data = get_mock_historical_data(selected_date)
        
        if generation_method == 'frequency':
            numbers = generate_by_frequency(historical_data)
        elif generation_method == 'past_winner':
            numbers = select_past_winner(historical_data)
        else:
            numbers = generate_random_numbers()
        
        return jsonify({
            'success': True,
            'numbers': numbers,
            'date': selected_date,
            'method': generation_method
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

def get_mock_historical_data(selected_date):
    """
    Simulate historical lottery data. In production, replace with actual API calls:
    
    Example API call:
    response = requests.get(f"{LOTTERY_API_BASE}/megamillions", params={
        'start_date': selected_date,
        'state': 'NC'
    })
    return response.json()
    """
    
    # Mock data for demonstration
    mock_draws = []
    base_date = datetime.strptime(selected_date, '%Y-%m-%d') if selected_date else datetime.now()
    
    for i in range(10):  # Last 10 draws
        draw_date = base_date - timedelta(days=i*3)
        numbers = sorted(random.sample(range(1, 71), 5))  # Mega Millions white balls
        mega_ball = random.randint(1, 25)  # Mega Ball
        
        mock_draws.append({
            'date': draw_date.strftime('%Y-%m-%d'),
            'numbers': numbers,
            'mega_ball': mega_ball
        })
    
    return mock_draws

def generate_by_frequency(historical_data):
    """Generate numbers based on frequency analysis of past draws"""
    all_numbers = []
    all_mega_balls = []
    
    for draw in historical_data:
        all_numbers.extend(draw['numbers'])
        all_mega_balls.append(draw['mega_ball'])
    
    # Count frequency
    number_freq = Counter(all_numbers)
    mega_freq = Counter(all_mega_balls)
    
    # Select most frequent numbers
    most_frequent = [num for num, count in number_freq.most_common(5)]
    
    # If we don't have enough frequent numbers, fill with random
    while len(most_frequent) < 5:
        new_num = random.randint(1, 70)
        if new_num not in most_frequent:
            most_frequent.append(new_num)
    
    mega_ball = mega_freq.most_common(1)[0][0] if mega_freq else random.randint(1, 25)
    
    return {
        'white_balls': sorted(most_frequent[:5]),
        'mega_ball': mega_ball
    }

def select_past_winner(historical_data):
    """Select a random past winning combination"""
    if not historical_data:
        return generate_random_numbers()
    
    random_draw = random.choice(historical_data)
    return {
        'white_balls': random_draw['numbers'],
        'mega_ball': random_draw['mega_ball']
    }

def generate_random_numbers():
    """Generate completely random Mega Millions numbers"""
    white_balls = sorted(random.sample(range(1, 71), 5))
    mega_ball = random.randint(1, 25)
    
    return {
        'white_balls': white_balls,
        'mega_ball': mega_ball
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
