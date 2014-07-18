import braintree

from flask import Flask, request, render_template
app = Flask(__name__)

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="3266cd6r66pw5y6s",
                                  public_key="4c9fcnpgv3rpzp84",
                                  private_key="016b4e4d7ae55870ef9c797478b18706")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/clienttoken", methods=["GET"])
def clienttoken():
        return braintree.ClientToken.generate()

@app.route("/create_transaction", methods=["GET","POST"])
def create_transaction():
    result = braintree.Transaction.sale({
                                        "amount": "35.00",
                                        "payment_method_nonce": request.args.get('payment_method_nonce',''),
                                        "options": {
                                        "submit_for_settlement": True
                                        }
                                        })
    if result.is_success:
        return "<h1>Success! Transaction ID: {0}</h1>".format(result.transaction.id)
    else:
        return "<h1>Error: {0}</h1>".format(result.message)
if __name__ == '__main__':
    app.run(debug=True)