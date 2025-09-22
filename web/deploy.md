# Deployment Guide

## Quick Deploy to Vercel (Recommended)

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy from the web directory
```bash
cd web
vercel --prod
```

### 4. Follow the prompts:
- Set up and deploy? **Yes**
- Which scope? Choose your account
- Link to existing project? **No** (for first time)
- What's your project's name? **cybersec-chatbot** (or your preferred name)
- In which directory is your code located? **./** 

## Alternative: GitHub + Vercel Integration

### 1. Push to GitHub
```bash
git add .
git commit -m "Add cybersec chatbot web interface"
git push origin main
```

### 2. Connect to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Set root directory to `web/`
5. Deploy!

## Local Development

### 1. Install dependencies
```bash
cd web
npm install
```

### 2. Run development server
```bash
npm run dev
```

### 3. Open browser
Visit `http://localhost:3000`

## Environment Variables (Optional)

In Vercel dashboard, add these environment variables:

- `NEXT_PUBLIC_API_URL`: Your model API endpoint (if using external API)
- `NEXT_PUBLIC_ENABLE_ANALYTICS`: Enable analytics (true/false)

## Custom Domain (Optional)

1. In Vercel dashboard, go to your project
2. Click "Domains" tab
3. Add your custom domain
4. Follow DNS configuration instructions

## Performance Tips

- The app is already optimized for Vercel's Edge Runtime
- Static assets are automatically cached
- API routes have CORS enabled for integration flexibility

## Troubleshooting

### Build Issues
- Ensure all dependencies are in package.json
- Check Node.js version compatibility (14+)

### Deployment Issues  
- Verify web/ directory structure
- Check vercel.json configuration
- Review build logs in Vercel dashboard

### Runtime Issues
- Check browser console for errors
- Verify API endpoints are accessible
- Test responsive design on different devices