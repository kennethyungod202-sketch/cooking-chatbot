from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import os

from .chatbot_service import CookingChatbot
from .models import Conversation, Message


def index(request):
    """Render the main chatbot page."""
    return render(request, 'chatbot/index.html')


@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    """
    API endpoint to handle chat messages.
    Expects JSON with: message, conversation_id (optional)
    """
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        conversation_id = data.get('conversation_id')
        
        if not user_message:
            return JsonResponse({'error': 'Message cannot be empty'}, status=400)
        
        # Get or create conversation
        if conversation_id:
            conversation = get_object_or_404(Conversation, id=conversation_id)
        else:
            conversation = Conversation.objects.create()
        
        # Save user message
        Message.objects.create(
            conversation=conversation,
            role='user',
            content=user_message
        )
        
        # Get conversation history for context
        history = []
        for msg in conversation.messages.all():
            history.append({
                'role': msg.role,
                'content': msg.content
            })
        
        # Get response from chatbot
        chatbot = CookingChatbot()
        response_text = chatbot.get_response(user_message, history[:-1])  # Exclude current user message
        
        # Save assistant message
        Message.objects.create(
            conversation=conversation,
            role='assistant',
            content=response_text
        )
        
        return JsonResponse({
            'response': response_text,
            'conversation_id': conversation.id,
            'message_id': Message.objects.filter(conversation=conversation).last().id
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def conversation_history(request):
    """View to display user's conversation history."""
    conversations = Conversation.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'chatbot/history.html', {'conversations': conversations})
