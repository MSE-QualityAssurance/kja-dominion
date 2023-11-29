# app.py
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from main import initialize_supply, current_player, draw_card, play_actions, buy_cards, cleanup

app = Flask(__name__)
CORS(app)

# Your existing route for rendering the HTML
@app.route('/')
def index():
    return render_template('index.html')

# New route for game actions
@app.route('/play_turn', methods=['POST'])
def play_turn():
    # Get the player from the request (you might need to adjust this based on your frontend logic)
    player = request.json.get('player', None)
    
    # Execute game logic for a turn
    # For simplicity, let's assume there's a single player
    if player == 'player1':
        play_turn_for_player(player1)
    elif player == 'player2':
        play_turn_for_player(player2)
    else:
        return jsonify({'error': 'Invalid player specified'}), 400

    return jsonify({'message': 'Turn played successfully'})


def play_turn_for_player(player):
    player.actions = 1
    player.buys = 1
    player.coins = 0

    draw_card(player)
    
    # Actions phase
    play_actions(player)
    
    # Buy phase
    buy_cards(player)
    
    # Cleanup phase
    cleanup(player)


if __name__ == '__main__':
    initialize_supply()
    app.run(debug=True)
