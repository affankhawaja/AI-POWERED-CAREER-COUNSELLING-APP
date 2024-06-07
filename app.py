#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
import ucp_fyp  # This is the converted notebook script

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_notebook():
    data = request.get_json()
    # Example function call (replace 'your_function' with the actual function name)
    # result = ucp_fyp.your_function(data)
    result = {"message": "Replace this with actual function call and response"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

