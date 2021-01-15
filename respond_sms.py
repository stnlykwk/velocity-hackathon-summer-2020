from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'Hi' or body == 'Menu':
        resp.message(
        '''
        Hi, this is your Scotiabank SMS assistant!
        Please enter the number of the service you are looking for:
        1. Check your Chequing account balance(s) and transactions
        2. Check your Saving account balance(s) and transactions
        3. Check your credit card balance(s) and transactions
        4. View your bills
        5. Pay your next bill

        For more information, you may call 1-800-4-SCOTIA (1-800-472-6842)
        or click https://play.google.com/store/apps/details?id=com.scotiabank.banking to open the Scotiabank Mobile App.


        PLEASE NOTE: You have a bill that is due in three days, please make sure to pay on time to avoid any fees. Thank you very much!
        '''
        )
    elif body == '1':
        resp.message(
        '''
        Your chequing account number is :541658153
        Current available balance is : $6511 
        The most recent 5 transactions:
        Miku - $65.23
        Aritzia - $354.43
        Transfer IN from Savings - $1000.00
        E-transfer to James - $89.35
        E-transfer to Samir - $32.51

        To return to the main menu, please respond with "Menu".
        To exit, please respond with "Bye".
        '''
        )
    elif body == '2':
        resp.message(
        '''
        Your saving account number is :685465141
        Current available balance is : $10,532 
        The most recent 5 transactions:
        Interest - $2.40
        Interest - $2.23
        ATM Deposit - $1563.00
        Transfer OUT to Chequing - $1000.00
        Payroll - $2354.35

        To return to the main menu, please respond with "Menu".
        To exit, please respond with "Bye".
        '''
        )
    elif body == '3':
        resp.message(
        '''
        ScotiaGold AMEX
        ---
        Current balance is : $5621 
        The most recent 5 transactions:
        Miku - $195.35
        JaBistro - $109.65
        Gyu-Bee - $135.53
        Home Depot - $354.65
        King Taps - $69.54


        Scotia Passport Visa Infinite
        ---
        Hertz - $45.32
        Fairmont - $234.54
        Air Canada - $31.21

        To return to the main menu, please respond with "Menu".
        To exit, please respond with "Bye".
        '''
        )
    elif body == '4':
        resp.message(
        '''
        You have two upcoming automated payments
        Alectra Utilities - Amount: $245 - Date 20200720
        Enbridge Natural Gas - Amount $90.25 - Date 20200825

        To return to the main menu, please respond with "Menu".
        To exit, please respond with "Bye".
        '''
        )
    elif body == '5':
        resp.message(
        '''
        Your next bill payment is:
        1. Alectra Utilities - Amount: $245 - Due date 20200812
        Please respond with "Yes" if you would like to make this payment.

        To return to the main menu, please respond with "Menu".
        To exit, please respond with "Bye".
        '''
        )
    elif body == 'Yes':
        resp.message(
        '''
        Congratulations! You have successfully paid your bill to Alectra Utilities.
        You may check this payment online at https://www.scotiabank.ca or via the Scotiabank Mobile App https://play.google.com/store/apps/details?id=com.scotiabank.banking.

        To return to the main menu, please respond with "Menu".
        To exit, please respond with "Bye".
        '''
        )
    elif body == 'Bye':
        resp.message(
        '''
        Thank you for banking with Scotibank!

        We hope you have a wonderful rest of your day, goodbye!
        '''
        )


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
