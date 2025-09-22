# CyberSec AI Assistant - Web Interface

A modern, cyberpunk-themed web interface for the CyberSec AI Assistant chatbot.

## Features

🎨 **Modern Cyberpunk UI**
- Dark theme with glowing green accents
- Terminal-style interface
- Smooth animations and transitions
- Responsive design for all devices

🔒 **Security-First Design**
- Ethical use warnings prominently displayed
- Input validation and safety checks
- Built-in refusal mechanisms for harmful requests

⚡ **Real-time Chat Interface**
- Instant message rendering
- Typing indicators
- Auto-scroll to latest messages
- Keyboard shortcuts (Enter to send, Shift+Enter for new line)

## Tech Stack

- **Framework**: Next.js 14 with App Router
- **Styling**: Tailwind CSS with custom cyberpunk theme
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **TypeScript**: Full type safety

## Quick Start

### 1. Install Dependencies
```bash
cd web
npm install
```

### 2. Development Server
```bash
npm run dev
```

Visit `http://localhost:3000` to see the interface.

### 3. Build for Production
```bash
npm run build
npm start
```

## Vercel Deployment

### Option 1: Vercel CLI
```bash
npm install -g vercel
vercel --prod
```

### Option 2: GitHub Integration
1. Push to GitHub repository
2. Connect repository to Vercel
3. Deploy automatically on push

## API Integration

The web interface currently uses mock responses. To integrate with your trained model:

1. **Local Model Server**: Set up a Flask/FastAPI server to serve your model
2. **API Endpoint**: Update `/app/api/chat/route.ts` to call your model server
3. **Environment Variables**: Add API endpoint configuration

### Example Model Integration
```typescript
// In /app/api/chat/route.ts
const response = await fetch('http://localhost:8000/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ prompt: message })
})
```

## Customization

### Colors (tailwind.config.js)
```javascript
colors: {
  'cyber-dark': '#0a0a0a',    // Main background
  'cyber-gray': '#1a1a1a',    // Secondary background
  'cyber-green': '#00ff41',   // Primary accent
  'cyber-blue': '#00d4ff',    // Secondary accent
  'cyber-red': '#ff0040',     // Warning/error
}
```

### Fonts
- **Primary**: JetBrains Mono (terminal style)
- **Headers**: Orbitron (futuristic)

### Animations
- Glow effects on important elements
- Smooth transitions between states
- Terminal-style typing animations

## Security Features

### Input Validation
- XSS protection through React's built-in escaping
- Input length limits
- Harmful keyword detection

### Content Safety
- Automated refusal of harmful requests
- Ethical use disclaimers
- Authorization requirement reminders

## File Structure

```
web/
├── app/
│   ├── api/chat/route.ts     # Chat API endpoint
│   ├── globals.css           # Global styles
│   ├── layout.tsx           # Root layout
│   └── page.tsx             # Main chat interface
├── public/                  # Static assets
├── package.json            # Dependencies
├── next.config.js          # Next.js configuration
├── tailwind.config.js      # Tailwind configuration
└── postcss.config.js       # PostCSS configuration
```

## Environment Variables

Create `.env.local` for local development:
```bash
# Optional: API endpoint for model server
NEXT_PUBLIC_API_URL=http://localhost:8000

# Optional: Enable/disable features
NEXT_PUBLIC_ENABLE_MOCK=true
```

## Performance

- **Next.js 14**: Latest optimizations
- **Server-side rendering**: Fast initial load
- **Component lazy loading**: Efficient resource usage
- **Optimized images**: Automatic WebP conversion

## Browser Support

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support
- Mobile browsers: Responsive design

## Contributing

1. Fork the repository
2. Create feature branch
3. Test on multiple devices
4. Submit pull request

## License

MIT License - See main project LICENSE file.