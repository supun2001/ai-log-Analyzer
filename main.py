import ollama
import os
import json
import time

# Ollama model
MODEL_ID = "llama3.2" 

def analyze_alerts(file_path):
    try:
        with open(file_path, 'r') as f:
            alerts = json.load(f)
        
        for alert in alerts:
            description = alert.get('rule', {}).get('description', 'Unknown alert')
            data = alert.get('data', {})
            
            prompt = f"Explain this security alert in simple terms:\nDescription: {description}\nDetails: {json.dumps(data)}"
            
            print(f"--- Analyzing Alert: {description} ---")
            
            try:
                response = ollama.chat(model=MODEL_ID, messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ])
                print(response['message']['content'])
                print("\n")
                
            except Exception as e:
                print(f"Error calling Ollama: {e}")
                print("Make sure the Ollama application is running and you have the model downloaded (ollama pull llama3.2)")
            
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")

if __name__ == "__main__":
    analyze_alerts("attacks.json")




