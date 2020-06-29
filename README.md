# Cherry Customer Service bot
### What and Why?
* Highly competitive technology driven era
* Customers are always on the hunt for the more customized solution
* Tough to satisfy the requirement of customers manually
* Users and customers  require solutions that are qualitative and at the same time simple to use
* In this scenario, chatbots comes as an easy solution to satisfy the need of today’s customer base 
* For business, having a chatbot can really help to achieve thicker customer base offering quality support and solution
* Bots help but don’t replace customer service agents

### How is it built?
* NLU- JointBERT
* DST- RuleBased
* Policy- RuleBased
* NLG- TemplateNLG

## Instructions to run on Google Colab - 

Run the following steps on each cell of your Google Colab notebook

* Clone and configure this repo, by pasting the below command.
```
!git clone https://github.com/Malavikka/ConvLab-2.git && cd ConvLab-2 && pip install -e .
```

* Install `flask_ngork`

```
!pip install flask_ngrok
```

* Run the Flask app
```python
!python /content/ConvLab-2/deploy/app.py
```

* Click on the second URL for google colab as shown in the image below-

![](images/)

* Add ‘/chat’ to the URL mentioned above on your browser

![](images/)

> Note: Refer to []()
