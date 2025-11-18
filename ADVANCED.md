# Advanced Customization Guide

## 🎨 UI Customization

### Change Chat Colors

Edit `chatbot_app/templates/chatbot/index.html`

**User Message Color:**
```css
/* Find line ~150 */
.user .message-content {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    /* Change to any gradient */
}
```

**Bot Message Color:**
```css
/* Find line ~156 */
.assistant .message-content {
    background: #e0e0e0;
    /* Change to any color */
}
```

**Header Background:**
```css
/* Find line ~31 */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Popular Color Schemes

```css
/* Ocean Blue */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Sunset Orange */
background: linear-gradient(135deg, #FF6B6B 0%, #FFD93D 100%);

/* Forest Green */
background: linear-gradient(135deg, #6BCB77 0%, #4D96FF 100%);

/* Purple Dream */
background: linear-gradient(135deg, #9D84B7 0%, #A0D8F7 100%);

/* Coral Pink */
background: linear-gradient(135deg, #FF6B6B 0%, #FF8E72 100%);
```

### Change Font

Add to `<head>` section:
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

<style>
    body {
        font-family: 'Poppins', sans-serif;
    }
</style>
```

Other font options:
- `'Roboto'` - Modern, clean
- `'Playfair Display'` - Elegant, serif
- `'Inter'` - Professional
- `'Nunito'` - Friendly

### Add Logo or Icon

Edit `index.html` header:
```html
<div class="header">
    <h1>🍳 Cooking Chatbot</h1>
    <!-- Add logo here -->
    <img src="/static/logo.png" alt="Logo" style="height: 40px;">
</div>
```

## 🤖 AI Behavior Customization

### Change System Prompt

Edit `chatbot_app/chatbot_service.py`, lines 24-32:

```python
self.system_prompt = """You are a professional culinary expert.
You provide detailed cooking techniques, ingredient substitutions,
and nutritional advice. Always include tips for beginners.
Format responses in an easy-to-read way."""
```

### Pre-built System Prompts

**Professional Chef:**
```python
"""You are a professional Michelin-trained chef. Provide sophisticated 
cooking advice, advanced techniques, and gourmet recipes. Focus on 
flavor combinations and presentation."""
```

**Health-Conscious:**
```python
"""You are a nutrition expert and healthy cooking specialist. 
Always suggest healthier alternatives. Provide calorie counts 
and nutritional benefits for all recipes."""
```

**Budget-Friendly:**
```python
"""You are a budget cooking expert. Suggest affordable recipes 
using inexpensive ingredients. Always provide cost estimates 
and money-saving cooking tips."""
```

**Cultural Cuisine:**
```python
"""You are an expert in various world cuisines. Help users 
prepare authentic dishes from different cultures. Provide 
traditional techniques and ingredient substitutions."""
```

### Change AI Model

Edit `chatbot_app/chatbot_service.py`, line 22:

```python
# Fast & Cheap (current)
self.model = "gpt-3.5-turbo"

# Better Quality & Slightly Slower
self.model = "gpt-4"

# Best of Both Worlds
self.model = "gpt-4-turbo-preview"
```

### Adjust Response Temperature

Edit line 47 in `chatbot_service.py`:

```python
response = openai.ChatCompletion.create(
    temperature=0.7,  # 0-1: Lower = precise, Higher = creative
    max_tokens=500,   # Maximum response length
)
```

- `temperature=0.3` - Very accurate, factual
- `temperature=0.7` - Balanced (default)
- `temperature=1.0` - Very creative, less accurate

## 🗄️ Database Customization

### Add New Message Fields

Edit `chatbot_app/models.py`:

```python
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Add new fields
    rating = models.IntegerField(default=0)  # User rating
    tokens_used = models.IntegerField(default=0)  # Track API usage
    category = models.CharField(max_length=50, default='general')  # Message type
```

After editing, run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Add User Preferences

Create new model:

```python
class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dietary_restriction = models.CharField(max_length=100)
    cuisine_preference = models.CharField(max_length=100)
    skill_level = models.CharField(
        max_length=20,
        choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')]
    )
    
    def __str__(self):
        return f"{self.user.username}'s Preferences"
```

## 🔌 API Endpoints

### Add New Endpoint

Edit `chatbot_app/views.py`:

```python
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def suggest_recipe(request):
    """API endpoint for recipe suggestions"""
    try:
        data = json.loads(request.body)
        ingredients = data.get('ingredients', [])
        
        chatbot = CookingChatbot()
        suggestion = chatbot.suggest_recipe(ingredients)
        
        return JsonResponse({'recipe': suggestion})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
```

Add to `chatbot_app/urls.py`:

```python
urlpatterns = [
    # ... existing urls ...
    path('api/recipe/', views.suggest_recipe, name='suggest_recipe'),
]
```

### Use from Frontend

```javascript
fetch('/api/recipe/', {
    method: 'POST',
    body: JSON.stringify({
        ingredients: ['chicken', 'rice', 'broccoli']
    })
})
.then(response => response.json())
.then(data => console.log(data.recipe));
```

## 🔍 Search & Filter

### Add Search to History

Edit `chatbot_app/views.py`:

```python
from django.db.models import Q

def search_conversations(request):
    """Search conversations by content"""
    query = request.GET.get('q', '')
    
    conversations = Conversation.objects.filter(
        messages__content__icontains=query
    ).distinct()
    
    return render(request, 'chatbot/search.html', {
        'conversations': conversations,
        'query': query
    })
```

## 📊 Analytics

### Track Usage

Add to `chatbot_app/views.py`:

```python
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)

# In your chat_api view
logger.info(f"User asked: {user_message[:100]}...")
logger.info(f"Response generated in {time.time() - start_time:.2f}s")
```

### View Logs

```bash
python manage.py runserver --log-level DEBUG
```

## 🚀 Performance Optimization

### Cache Responses

Edit `chatbot_app/views.py`:

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # Cache for 5 minutes
def common_recipes(request):
    """Get commonly requested recipes"""
    pass
```

### Async Processing

Install Celery:
```bash
pip install celery redis
```

Offload API calls to background:

```python
from celery import shared_task

@shared_task
def generate_response(message_id):
    """Generate response in background"""
    message = Message.objects.get(id=message_id)
    chatbot = CookingChatbot()
    response = chatbot.get_response(message.content)
    # Save response
```

## 📱 Mobile Optimization

The default template is already mobile-responsive, but you can enhance it:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

<style>
    @media (max-width: 600px) {
        .container {
            max-height: 100vh;
            max-width: 100%;
        }
        
        .message-content {
            max-width: 85%;
        }
    }
</style>
```

## 🔐 Authentication

### Add User Login

Create template `templates/login.html`:

```html
{% extends 'base.html' %}

{% block content %}
<form method="post">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Login</button>
</form>
{% endblock %}
```

Edit `views.py`:

```python
from django.contrib.auth.decorators import login_required

@login_required
def chatbot_view(request):
    return render(request, 'chatbot/index.html')
```

## 🌐 Internationalization (i18n)

Make the chatbot multi-language:

```python
from django.utils.translation import gettext as _

self.system_prompt = _("You are a helpful cooking assistant...")
```

Add to `settings.py`:

```python
LANGUAGE_CODE = 'en-us'
USE_I18N = True
```

## 📧 Email Notifications

Send email when conversation is saved:

```python
from django.core.mail import send_mail

send_mail(
    'New Conversation Saved',
    f'Conversation {conversation.id} saved successfully',
    'from@example.com',
    ['to@example.com'],
)
```

## 🔔 Webhook Integration

Integrate with external services:

```python
import requests

def send_webhook(event_type, data):
    """Send webhook to external service"""
    webhook_url = os.getenv('WEBHOOK_URL')
    requests.post(webhook_url, json={
        'event': event_type,
        'data': data
    })
```

---

## 📚 Resources

- Django Customization: https://docs.djangoproject.com/
- OpenAI Fine-tuning: https://platform.openai.com/docs/guides/fine-tuning
- CSS Tricks: https://css-tricks.com/
- Bootstrap: https://getbootstrap.com/

---

**Happy Customizing!** 🎨
