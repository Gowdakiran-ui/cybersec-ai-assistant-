# 🌟 CyberSec AI Assistant - Web Interface Setup

## 🎯 Overview

You now have a professional, cyberpunk-themed web interface for your cybersecurity chatbot! This guide will help you get it running locally and deploy it to Vercel.

## 🚀 Quick Setup

### 1. Navigate to Web Directory
```bash
cd web
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Start Development Server
```bash
npm run dev
```

### 4. Open in Browser
Visit: `http://localhost:3000`

## 🌐 Deploy to Vercel (Production)

### Option 1: Vercel CLI (Recommended)
```bash
# Install Vercel CLI globally
npm install -g vercel

# Deploy from web directory
cd web
vercel --prod
```

### Option 2: GitHub + Vercel Dashboard
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Set root directory to `web/`
6. Deploy!

## ✨ Features You'll See

### 🎨 Visual Design
- **Cyberpunk Theme**: Dark background with glowing green accents
- **Terminal Aesthetics**: Command-line style interface
- **Smooth Animations**: Professional transitions and effects
- **Responsive**: Perfect on desktop, tablet, and mobile

### 🔒 Security Features
- **Ethical Warnings**: Prominent disclaimers about authorized use only
- **Input Validation**: Automatic filtering of harmful requests
- **Safe Responses**: Built-in refusal mechanisms for illegal activities

### 💬 Chat Interface
- **Real-time Messaging**: Instant responses with typing indicators
- **Message History**: Scrollable conversation log
- **Keyboard Shortcuts**: Enter to send, Shift+Enter for new line
- **Character Counter**: Input length tracking

### 🛡️ Cybersecurity Focus
- **Terminal Prompts**: Authentic command-line styling
- **Code Highlighting**: Proper formatting for commands
- **Safety Reminders**: Authorization requirements in every response

## 🔧 Customization

### Colors (in `tailwind.config.js`)
```javascript
'cyber-dark': '#0a0a0a',    // Main dark background
'cyber-green': '#00ff41',   // Primary green accent
'cyber-blue': '#00d4ff',    // Secondary blue accent
'cyber-red': '#ff0040',     // Warning red
```

### Fonts
- **Primary**: JetBrains Mono (monospace terminal font)
- **Headers**: Orbitron (futuristic sci-fi font)

## 🔌 Model Integration

### Current State
- Uses intelligent mock responses based on your training data
- Simulates the behavior of your trained model
- Includes all the ethical guidelines from your training questions

### Connect Real Model (Optional)
To connect your actual trained model:

1. **Create Model Server** (Python Flask/FastAPI):
```python
from flask import Flask, request, jsonify
import torch
from model import GPT

app = Flask(__name__)
model = GPT.load_from_checkpoint('models/ckpt.pt')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json['prompt']
    response = model.generate(prompt)
    return jsonify({'response': response})
```

2. **Update Web API** (in `web/app/api/chat/route.ts`):
```typescript
const response = await fetch('http://localhost:8000/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ prompt: message })
})
```

## 📱 Mobile Experience

The interface is fully responsive and includes:
- Touch-friendly chat interface
- Optimized font sizes for mobile
- Swipe-friendly message scrolling
- Mobile keyboard optimization

## 🎭 Demo Content

The web interface includes realistic responses for:
- nmap scanning questions
- Linux privilege escalation queries
- Incident response procedures
- Log analysis techniques
- Web application security
- Ethical hacking guidelines

## 🛠️ Development

### File Structure
```
web/
├── app/
│   ├── api/chat/route.ts    # Chat API endpoint
│   ├── globals.css          # Cyberpunk styling
│   ├── layout.tsx          # App layout
│   └── page.tsx            # Main chat interface
├── package.json            # Dependencies
├── tailwind.config.js      # Custom theme
└── vercel.json            # Deployment config
```

### Available Scripts
```bash
npm run dev     # Development server
npm run build   # Production build
npm run start   # Production server
npm run lint    # Code linting
```

## 🌟 Live Demo

Once deployed, your chatbot will be accessible at:
- `https://your-project-name.vercel.app`
- Custom domain (if configured)

## 💡 Tips

1. **Performance**: The app uses Next.js 14 for optimal performance
2. **SEO**: Includes proper meta tags and descriptions
3. **Analytics**: Easy to add Google Analytics or other tracking
4. **PWA Ready**: Can be converted to a Progressive Web App

## ⚠️ Important Notes

- **Mock Responses**: Currently uses simulated responses
- **Security**: All responses emphasize ethical, authorized use
- **Responsive**: Tested on all major browsers and devices
- **Production Ready**: Optimized for Vercel deployment

Your cybersecurity chatbot now has a professional web interface that matches the quality of your AI model! 🔐✨