#from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request
import convlab2
from convlab2.nlu.jointBERT.multiwoz import BERTNLU
from convlab2.nlu.milu.multiwoz import MILU
from convlab2.dst.rule.multiwoz import RuleDST
from convlab2.policy.rule.multiwoz import RulePolicy
from convlab2.nlg.template.multiwoz import TemplateNLG
from convlab2.dialog_agent import PipelineAgent, BiSession
from convlab2.evaluator.multiwoz_eval import MultiWozEvaluator
from pprint import pprint
import random
import numpy as np
import torch

app = Flask(__name__)
#run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return "<h1>Running Flask on Google Colab!</h1>"
#define app routes
@app.route("/chat")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    sys_nlu = BERTNLU()
    sys_dst = RuleDST()
    sys_policy = RulePolicy()
    sys_nlg = TemplateNLG(is_user=False)
    sys_agent = PipelineAgent(sys_nlu, sys_dst, sys_policy, sys_nlg, name='sys')
    return str(sys_agent.response(userText))

@app.route('/process',methods=['POST'])
def process():
    user_input = request.form['user_input']
    sys_nlu = BERTNLU()
    sys_dst = RuleDST()
    sys_policy = RulePolicy()
    sys_nlg = TemplateNLG(is_user=False)
    sys_agent = PipelineAgent(sys_nlu, sys_dst, sys_policy, sys_nlg, name='sys')
    bot_response = str(sys_agent.response(user_input))
    print("Cherry: "+bot_response)
    return render_template('index.html',user_input=user_input,bot_response=bot_response)

if __name__ == "__main__":
    app.run()
