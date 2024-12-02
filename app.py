from flask import Flask, render_template, request, jsonify
from api_handler import fetch_stock_ratios

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/comparestocks', methods=['GET', 'POST'])
def compare_stocks():
    if request.method == 'GET':
        # Render the compare stocks page
        return render_template('compare.html')

    if request.method == 'POST':
        selectedStocks = request.get_json().get('stocks', [])
        print(selectedStocks)
        # Hard-coded stock symbols or other POST handling logic
        hardcoded_stocks = ["AAPL", "MSFT"]  # Example stocks
        try:
            stock_data = fetch_stock_ratios(selectedStocks)
            # print(stock_data)
            transformed_data = [
        {
            'symbol': symbol,
            'pe_ratio': details.get('P/E Ratio', 'N/A'),
            'eps': details.get('EPS', 'N/A'),
            'roa': details.get('ROE', 'N/A')  # Rename as 'ROA' for consistency
        }
        for symbol, details in stock_data.items()
    ]
            return jsonify(transformed_data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
