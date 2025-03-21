from flask import Flask, jsonify
import scrape_website


app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currenty Rate API</h1><p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_curr>-<out_curr>')
def api(in_curr, out_curr):
    rate = scrape_website.get_currency_rate(in_curr, out_curr)
    result_dictionary = {
        'input_currency': in_curr,
        'output_currency': out_curr,
        'rate_exchange_rate':rate
    }
    return jsonify(result_dictionary)

# app.run(host='0.0.0.0')
app.run()