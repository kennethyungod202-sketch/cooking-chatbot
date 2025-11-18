"""
Chatbot service using Google Gemini API for cooking assistance.
"""
import os
import google.generativeai as genai


class CookingChatbot:
    def __init__(self, api_key=None):
        """
        Initialize the Cooking Chatbot with Google Gemini API key.
        
        Args:
            api_key (str): Google Gemini API key. If None, uses GEMINI_API_KEY env variable.
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable or api_key parameter is required")

        # Configure the Gemini API
        genai.configure(api_key=self.api_key)
        self.model = "gemini-2.5-flash"
        self.client = genai.GenerativeModel(self.model)
        self.system_prompt = """You are a helpful cooking assistant chatbot. 
        Your role is to help users with:
        - Recipe suggestions based on ingredients they have
        - Cooking techniques and methods
        - Nutritional information
        - Dietary restrictions and alternatives
        - Meal planning
        - Kitchen tips and tricks
        - Food safety guidelines

        Be friendly, concise, and provide practical advice. Always prioritize food safety."""

    def get_response(self, user_message, conversation_history=None):
        """
        Get a response from Google Gemini for a user message.
        
        Args:
            user_message (str): The user's message
            conversation_history (list): Previous messages in the conversation
            
        Returns:
            str: The chatbot's response
        """
        if not user_message or not user_message.strip():
            return "Please ask me something about cooking!"
        
        try:
            # Build the complete prompt with system instructions and message
            full_prompt = f"{self.system_prompt}\n\nUser: {user_message}"
            
            # Call Gemini API
            response = self.client.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=500,
                )
            )
            
            # Extract text from response
            if response.text:
                return response.text
            else:
                return "Sorry, I couldn't generate a response. Please try again."
                
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def suggest_recipe(self, ingredients):
        """
        Suggest recipes based on available ingredients.
        
        Args:
            ingredients (list): List of available ingredients
            
        Returns:
            str: Recipe suggestions
        """
        ingredient_str = ", ".join(ingredients)
        message = f"I have these ingredients: {ingredient_str}. Can you suggest me a recipe?"
        return self.get_response(message)

    def get_cooking_tips(self, dish):
        """
        Get cooking tips for a specific dish.
        
        Args:
            dish (str): The name of the dish
            
        Returns:
            str: Cooking tips
        """
        message = f"Give me some useful cooking tips for preparing {dish}."
        return self.get_response(message)

    def get_nutritional_info(self, food_item):
        """
        Get nutritional information for a food item.
        
        Args:
            food_item (str): The name of the food item
            
        Returns:
            str: Nutritional information
        """
        message = f"What are the nutritional facts for {food_item}?"
        return self.get_response(message)
