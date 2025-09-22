import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'CyberSec AI Assistant | Kiran Gowda',
  description: 'Advanced cybersecurity chatbot trained on penetration testing, Linux commands, and network security',
  keywords: 'cybersecurity, penetration testing, AI assistant, chatbot, nmap, Linux security',
  authors: [{ name: 'Kiran Gowda.A' }],
  viewport: 'width=device-width, initial-scale=1',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  )
}