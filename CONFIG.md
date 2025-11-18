# Cooking Chatbot - Configuration Guide

## Environment Variables

Create a `.env` file in the root directory with these variables:

```bash
# Required: OpenAI API Configuration
OPENAI_API_KEY=sk-your-api-key-here

# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Configuration (optional)
# Defaults to SQLite3
# DB_ENGINE=django.db.backends.sqlite3
# DB_NAME=db.sqlite3

# Server Configuration
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Getting OpenAI API Key

### Step-by-Step:

1. **Go to OpenAI Platform**
   - Visit: https://platform.openai.com/

2. **Sign In or Create Account**
   - Use your email or GitHub account
   - Verify your email

3. **Generate API Key**
   - Click your profile → "API keys" (top right)
   - Or visit: https://platform.openai.com/api-keys
   - Click "Create new secret key"
   - Give it a name (e.g., "Cooking Chatbot")

4. **Copy Your Key**
   - Copy the key immediately (you won't see it again!)
   - It looks like: `sk-...`

5. **Add to .env**
   - Add to your `.env` file:
   ```
   OPENAI_API_KEY=sk-your-actual-key
   ```

6. **Set Up Billing** (if not already done)
   - Go to: https://platform.openai.com/account/billing/overview
   - Add a payment method
   - Set usage limits if desired

## Cost Information

OpenAI API uses a pay-as-you-go model:

- **GPT-3.5 Turbo**: ~$0.0005 per 1000 tokens
  - Very affordable for testing and light usage
  - 1 message ≈ 100-500 tokens

- **Monitoring Costs**:
  - Check usage: https://platform.openai.com/account/usage/overview
  - Set usage limits: https://platform.openai.com/account/billing/limits

## Customization

### Change AI Model

Edit `chatbot_app/chatbot_service.py`:

```python
# Line 22
self.model = "gpt-4"  # Change to gpt-4 for better responses
```

Available models:
- `gpt-3.5-turbo` (default, fast, cheap)
- `gpt-4` (better quality, slower, expensive)
- `gpt-4-turbo-preview` (best of both)

### Modify Chatbot Personality

Edit `chatbot_app/chatbot_service.py`:

```python
# Lines 24-32
self.system_prompt = """You are a friendly cooking expert.
You help with recipes and cooking techniques.
You always prioritize food safety."""
```

### Change UI Theme

Edit `chatbot_app/templates/chatbot/index.html`:

```css
/* Lines 17-19 */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change colors to:
#FF6B6B (red)
#4ECDC4 (teal)
#45B7D1 (blue)
#96CEB4 (green)
*/
```

## Database Configuration

Default is SQLite3 (file-based, no setup needed).

### To use PostgreSQL:

1. **Install PostgreSQL**
2. **Install Python driver**:
   ```bash
   pip install psycopg2-binary
   ```

3. **Update .env**:
   ```
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=cooking_chatbot
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. **Update settings.py**:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
           'NAME': os.getenv('DB_NAME', BASE_DIR / 'db.sqlite3'),
           'USER': os.getenv('DB_USER', ''),
           'PASSWORD': os.getenv('DB_PASSWORD', ''),
           'HOST': os.getenv('DB_HOST', ''),
           'PORT': os.getenv('DB_PORT', ''),
       }
   }
   ```

## Production Deployment

### Before going live:

1. **Change SECRET_KEY**
   - Use a new, secure key
   - Generate: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

2. **Set DEBUG=False**
   ```
   DEBUG=False
   ```

3. **Update ALLOWED_HOSTS**
   ```
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

4. **Use Environment Variable for API Key**
   - Never hardcode API keys
   - Always use environment variables

5. **Use Production Database**
   - PostgreSQL recommended
   - Managed database service preferred

6. **Enable HTTPS**
   - Use SSL certificate
   - Add SECURE_SSL_REDIRECT=True

7. **Set up monitoring**
   - Monitor API usage
   - Set up error logging
   - Monitor application performance

### Deployment Platforms:

- **Heroku** (simplest)
  - Free tier available
  - Excellent for testing

- **AWS**
  - EC2, Elastic Beanstalk, or Lightsail
  - More control and scalability

- **DigitalOcean**
  - Simple droplets
  - Affordable

- **PythonAnywhere**
  - Python-friendly hosting

## Troubleshooting

### "Invalid API Key"
- Check the key is correct in `.env`
- Make sure there are no extra spaces
- Verify key hasn't been revoked

### "Rate Limit Exceeded"
- You've hit API rate limits
- Wait a few moments and retry
- Check your usage limits

### "Context Length Exceeded"
- Conversation history is too long
- Clear the database or start new conversation
- Increase max_tokens in settings if needed

### "Connection Error"
- Check internet connection
- Verify OpenAI API status
- Check firewall settings

## Security Best Practices

1. ✅ **Store API key in .env**
   ```
   OPENAI_API_KEY=sk-...
   ```

2. ✅ **Add .env to .gitignore**
   Already done in project

3. ✅ **Never share API key**
   - Not in code
   - Not in documentation
   - Not in screenshots

4. ✅ **Rotate keys regularly**
   - Generate new keys on OpenAI dashboard
   - Delete old keys

5. ✅ **Use environment variables everywhere**
   - Development
   - Staging
   - Production

6. ✅ **Monitor API usage**
   - Check OpenAI dashboard regularly
   - Set up usage alerts

## Support

- **OpenAI Help**: https://help.openai.com/
- **API Documentation**: https://platform.openai.com/docs/
- **Status Page**: https://status.openai.com/
- **Forum**: https://community.openai.com/

---

**Need help?** Check QUICKSTART.md for common commands!
