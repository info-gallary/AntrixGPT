
from flask import Flask, render_template, request, jsonify
import os
# from dotenv import load_dotenv
from langchain_community.llms import Ollama # type: ignore
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

app = Flask(__name__)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert assistant in space science, focusing on the solar system, space exploration, and how solar events affect Earth. Please provide accurate and detailed explanations.and dont give every answer to lengthy try conclude in one to two line only long answer for doubts regarding information request and give in hindi and greet yourself in short in hindi language."),
        ("user", "Question: {question}")
    ]
)

# Instantiate the LLM and output parser
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()

@app.route('/')
def index():
    # return app.send_static_file('index.html')
    return render_template('index.html')
# Route for Solar Safar
@app.route('/solarsafar')
def solar_safar():
    return render_template('SolarSafar/dist/index2.html')  # Render the Solar Safar page

# Route for Animation
# @app.route('/animation')
# def animation():
#     return render_template('cms.html')  # Render the Animation page

# Route for Community
@app.route('/community')
def community():
    return app.send_static_file('main.html')
  # Render the Community page

@app.route('/animation1')
def animation1():
    return render_template('eclipse.html')  # Template for Animation 1

@app.route('/animation2')
def animation2():
    return render_template('cms.html')  # Template for Animation 2

@app.route('/get_response', methods=['GET'])
def get_response():
    question = request.args.get('question')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Invoke the chain
        template_response = prompt.invoke({"question": question})
        llm_response = llm.invoke(template_response)
        response = output_parser.invoke(llm_response)
        print(response)  # Log the response to the console
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)