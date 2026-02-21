
'''
The Task: The "Resilient LLM Wrapper"

Scenario: You are building a production-grade wrapper for an LLM (like OpenAI or Anthropic). You need to handle specific failures:

RateLimitError: When you hit API limits (should trigger a Warning log).

ValidationInferenceError: When the LLM returns "junk" that isn't valid JSON (should trigger an Error log + Traceback).

AuthenticationError: A critical failure (should stop the program).

'''

import logging
import json
import time

# --- 1. THE SIGNALS (Custom Exceptions) ---
class AIError(Exception): """Base class for our system"""
class RateLimitError(AIError): """Non-fatal: Need to wait"""
class ValidationError(AIError): """Data issue: Bad LLM output"""
class AuthError(AIError): """Fatal: Key is dead"""

# --- 2. THE WORKER (Logic that triggers the signals) ---
def mock_llm_api(api_key, request_count, mock_response):
    """
    This function simulates the actual 'hit' to an AI service.
    It checks for conditions and 'raises' the specific signal.
    """
    if api_key != "SECRET_123":
        raise AuthError("Invalid API Key! Access Denied.")
    
    if request_count > 3:
        raise RateLimitError("Rate limit exceeded. Please slow down.")
    
    try:
        return json.loads(mock_response)
    except json.JSONDecodeError:
        raise ValidationError(f"LLM returned garbage: {mock_response}")

# --- 3. THE HANDLER (The 'Program' that manages the signals) ---
def run_ai_task(key, hits, data):
    try:
        print(f"\n--- Testing Scenario: {data[:15]}... ---")
        result = mock_llm_api(key, hits, data)
        logging.info(f"Success! Result: {result}")
        
    except AuthError as e:
        # Action: Stop the whole pipeline
        logging.critical(f"AUTH FAILURE: {e}")
        print("Critical failure. Check your environment variables!")
        
    except RateLimitError as e:
        # Action: Wait and retry (Simulation)
        logging.warning(f"LIMIT HIT: {e}")
        print("Backing off for 2 seconds...")
        time.sleep(2)
        
    except ValidationError as e:
        # Action: Log the bad data for the engineers to see
        logging.error("DATA CORRUPTION", exc_info=True)
        print("The LLM hallucinated invalid JSON. Check app.log for details.")
        
    except AIError as e:
        # Action: Catch-all for any other AI related issues
        logging.error(f"General AI Error: {e}")

# --- 4. EXECUTION (Triggering the 4 classes) ---
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Trigger 1: AuthError
run_ai_task("WRONG_KEY", 1, '{"status": "ok"}')

# Trigger 2: RateLimitError
run_ai_task("SECRET_123", 10, '{"status": "ok"}')

# Trigger 3: ValidationError
run_ai_task("SECRET_123", 1, 'Invalid non-json string')

# Trigger 4: Success (No Error)
run_ai_task("SECRET_123", 1, '{"prediction": "sunny"}')