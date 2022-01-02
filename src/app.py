from flask import Flask,render_template,request,url_for
import json
from web3 import Web3, HTTPProvider

blockchain_address = 'http://127.0.0.1:7545'
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.defaultAccount = web3.eth.accounts[1]

compiled_contract_path = '../build/contracts/election.json'
deployed_contract_address = '0xBd1d591EC46df9090abdf67e826Fa247372CA75B'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']

contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

app = Flask(__name__)
m=''


@app.route('/button1',methods=["GET","POST"])
def on():
	print("Button1")

	tx_hash = contract.functions.castVote(0).transact()
	web3.eth.waitForTransactionReceipt(tx_hash)

	return ('Vote Casted')

@app.route('/button2',methods=["GET","POST"])
def off():
	print('Button2')
	tx_hash = contract.functions.castVote(1).transact()
	web3.eth.waitForTransactionReceipt(tx_hash)

	return ('Vote Casted')

if __name__ == '__main__':
	app.run(debug=True)