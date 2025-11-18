# Cooking Chatbot - AI-Powered Cooking Assistant

A Django-based web application that provides an intelligent cooking assistant using OpenAI's GPT-3.5 Turbo model. The chatbot can help with recipes, cooking techniques, nutritional information, meal planning, and kitchen tips.

## 🌟 Features

- **AI-Powered Cooking Assistance**: Uses OpenAI's GPT-3.5 Turbo for intelligent responses
- **Recipe Suggestions**: Get recipe recommendations based on available ingredients
- **Cooking Tips**: Learn useful cooking techniques and tips
- **Nutritional Information**: Get nutritional facts for food items
- **Conversation History**: Store and retrieve past conversations
- **Responsive UI**: Beautiful, mobile-friendly web interface
- **Real-time Chat**: Instant responses from the AI assistant
- **Food Safety Guidelines**: Safety advice for food preparation

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
- OpenAI API Key

## 🚀 Installation

### 1. Clone or Navigate to the Project

```bash
cd chatbot_project
```

### 2. Create and Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```bash
# On Windows (PowerShell)
Copy-Item .env.example .env

# On macOS/Linux
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
DEBUG=True
SECRET_KEY=your_django_secret_key_here
```

**To get an OpenAI API Key:**
1. Visit https://platform.openai.com/
2. Sign up or log in to your account
3. Go to API keys section
4. Create a new secret key
5. Copy and paste it in your `.env` file

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📚 Project Structure

```
chatbot_project/
├── chatbot_app/
│   ├── migrations/
│   ├── templates/
│   │   └── chatbot/
│   │       ├── index.html          # Main chat interface
│   │       └── history.html        # Conversation history
│   ├── static/                     # Static files (CSS, JS)
│   ├── admin.py                    # Admin configuration
│   ├── apps.py                     # App configuration
│   ├── chatbot_service.py          # Chatbot service with OpenAI
│   ├── models.py                   # Database models
│   ├── urls.py                     # URL routing
│   ├── views.py                    # View functions
│   └── __init__.py
├── chatbot_project/
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Project URL configuration
│   ├── wsgi.py                     # WSGI configuration
│   └── __init__.py
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore file
└── README.md                       # This file
```

## 🔧 API Endpoints

### Chat Endpoint
**POST** `/chat/`

Request body:
```json
{
    "message": "How to make pasta carbonara?",
    "conversation_id": 1
}
```

Response:
```json
{
    "response": "Pasta carbonara is an Italian dish...",
    "conversation_id": 1,
    "message_id": 10
}
```

### Home Page
**GET** `/`

Displays the main chat interface.

### Conversation History
**GET** `/history/`

Shows all previous conversations (login required).

## 💡 Usage Examples

### Start Chatting
1. Open `http://127.0.0.1:8000/`
2. Type your cooking question
3. Press Enter or click Send
4. Get instant AI-powered responses

### Example Questions
- "What can I make with chicken, rice, and broccoli?"
- "How do I make hollandaise sauce?"
- "What are the nutritional facts for 100g of salmon?"
- "Give me tips for making perfect scrambled eggs"
- "What are some vegetarian recipes?"

## 🔐 Security Notes

- Never commit `.env` file to version control
- Change the `SECRET_KEY` in production
- Set `DEBUG=False` in production
- Use a secure database backend (e.g., PostgreSQL) in production
- Implement rate limiting for API endpoints
- Use HTTPS in production

## 📦 Dependencies

- **Django 4.2.7**: Web framework
- **python-dotenv 1.0.0**: Environment variable management
- **openai 1.3.5**: OpenAI API client
- **requests 2.31.0**: HTTP library

## 🗄️ Database Models

### Conversation
Stores conversation sessions between users and the chatbot.

### Message
Stores individual messages in a conversation with role (user/assistant).

## 🛠️ Development Tips

### Clear Database
```bash
python manage.py flush
```

### Create Database Migrations
```bash
python manage.py makemigrations
```

### Access Django Admin
Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

### Debug Mode
Enable/disable debug mode in `.env`:
```
DEBUG=True    # For development
DEBUG=False   # For production
```

## 🚨 Troubleshooting

### Module Not Found Errors
Ensure virtual environment is activated and all dependencies are installed:
```bash
pip install -r requirements.txt
```

### OpenAI API Key Error
- Verify the API key is correctly set in `.env`
- Check that your OpenAI account has available credits
- Ensure the API key has proper permissions

### Port Already in Use
If port 8000 is busy, specify a different port:
```bash
python manage.py runserver 8001
```

### Database Errors
Reset migrations:
```bash
python manage.py migrate --fake-initial
```

## 📝 Customization

### Change System Prompt
Edit the `system_prompt` in `chatbot_service.py` to modify chatbot behavior.

### Add Custom Commands
Extend the `CookingChatbot` class in `chatbot_service.py` with new methods.

### Styling
Modify CSS in HTML templates located in `chatbot_app/templates/chatbot/`

## 🤝 Contributing

Feel free to customize and extend this project for your needs.

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

For issues with:
- **Django**: https://docs.djangoproject.com/
- **OpenAI API**: https://platform.openai.com/docs/
- **Python**: https://www.python.org/

## 🎯 Next Steps

1. Add user authentication
2. Implement conversation ratings
3. Add recipe database integration
4. Implement voice input/output
5. Add multiple language support
6. Deploy to production (Heroku, AWS, etc.)

---

**Happy Cooking!** 👨‍🍳👩‍🍳
