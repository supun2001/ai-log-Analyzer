import ollama
import os
import json

# Ollama model
MODEL_ID = "llama3.2" 

def analyze_alerts(file_path, output_path):
    try:
        with open(file_path, 'r') as f:
            alerts = json.load(f)
        
        results = []
        
        for alert in alerts:
            description = alert.get('rule', {}).get('description', 'Unknown alert')
            level = alert.get('rule', {}).get('level', 0)
            agent = alert.get('agent', {}).get('name', 'Unknown')
            timestamp = alert.get('timestamp', '')
            data = alert.get('data', {})
            srcip = data.get('srcip', 'Local')
            
            prompt = f"Explain this security alert in simple terms:\nDescription: {description}\nDetails: {json.dumps(data)}"
            
            print(f"--- Analyzing Alert: {description} ---")
            
            try:
                response = ollama.chat(model=MODEL_ID, messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ])
                analysis_text = response['message']['content']
                print(analysis_text)
                print("\n")
                
                results.append({
                    "timestamp": timestamp,
                    "description": description,
                    "level": level,
                    "agent": agent,
                    "srcip": srcip,
                    "analysis": analysis_text
                })
                
            except Exception as e:
                print(f"Error calling Ollama: {e}")
        
        # Save to dashboard public folder
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"Analysis saved to {output_path}")
            
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")

if __name__ == "__main__":
    # Use paths relative to this script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "attacks.json")
    output_file = os.path.join(base_dir, "dashboard", "public", "alerts.json")
    
    analyze_alerts(input_file, output_file)






