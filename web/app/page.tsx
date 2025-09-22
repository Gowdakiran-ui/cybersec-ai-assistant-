'use client'

import { useState, useRef, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Send, Terminal, Shield, Zap, Command, Brain, AlertTriangle } from 'lucide-react'

interface Message {
  id: number
  text: string
  isUser: boolean
  timestamp: Date
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      text: "Welcome to CyberSec AI Assistant! I'm trained on ethical penetration testing, Linux security, and network analysis. How can I help you secure your systems today?",
      isUser: false,
      timestamp: new Date()
    }
  ])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSendMessage = async () => {
    if (!inputValue.trim() || isLoading) return

    const userMessage: Message = {
      id: Date.now(),
      text: inputValue,
      isUser: true,
      timestamp: new Date()
    }

    setMessages(prev => [...prev, userMessage])
    setInputValue('')
    setIsLoading(true)

    try {
      // For now, simulate API call with mock responses
      await new Promise(resolve => setTimeout(resolve, 1500))
      
      const botResponse = generateMockResponse(inputValue)
      
      const botMessage: Message = {
        id: Date.now() + 1,
        text: botResponse,
        isUser: false,
        timestamp: new Date()
      }

      setMessages(prev => [...prev, botMessage])
    } catch (error) {
      console.error('Error:', error)
      const errorMessage: Message = {
        id: Date.now() + 1,
        text: "I apologize, but I'm currently offline. Please try again later or run the model locally.",
        isUser: false,
        timestamp: new Date()
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const generateMockResponse = (query: string): string => {
    const lowerQuery = query.toLowerCase()
    
    if (lowerQuery.includes('nmap') || lowerQuery.includes('scan')) {
      return "For ethical port scanning, use: `nmap -sV -Pn <target>` (authorized lab only). Replace <target> with your test system IP. Always ensure you have explicit permission before scanning any network."
    }
    
    if (lowerQuery.includes('linux') || lowerQuery.includes('privilege') || lowerQuery.includes('escalation')) {
      return "For privilege escalation analysis:\n1. Check SUID binaries: `find / -perm -u=s -type f 2>/dev/null`\n2. Review sudo permissions: `sudo -l`\n3. Examine cron jobs: `cat /etc/crontab`\n\nAlways use these commands for defensive analysis in authorized environments only."
    }
    
    if (lowerQuery.includes('illegal') || lowerQuery.includes('hack') || lowerQuery.includes('exploit')) {
      return "I can't assist with unauthorized activities. I'm designed to help with ethical cybersecurity practices in controlled lab environments. Would you like help with defensive security measures instead?"
    }
    
    if (lowerQuery.includes('log') || lowerQuery.includes('analysis') || lowerQuery.includes('incident')) {
      return "For log analysis and incident response:\n1. Collect timestamps and source IPs\n2. Preserve evidence by copying logs\n3. Look for indicators of compromise (IOCs)\n4. Apply containment measures in your lab\n5. Plan remediation steps\n\nRemember to follow your organization's incident response procedures."
    }

    return "I specialize in ethical cybersecurity assistance. I can help with:\n• Authorized penetration testing procedures\n• Linux security analysis\n• Network reconnaissance (lab environments)\n• Incident response planning\n• Security tool usage\n\nPlease specify what cybersecurity topic you'd like help with, and I'll provide guidance for authorized testing environments."
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  return (
    <div className="min-h-screen bg-cyber-dark flex flex-col">
      {/* Header */}
      <motion.header 
        initial={{ y: -50, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        className="cyber-bg border-b border-cyber-green p-4"
      >
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-cyber-green rounded-lg">
              <Shield className="h-6 w-6 text-cyber-dark" />
            </div>
            <div>
              <h1 className="text-xl font-cyber font-bold text-cyber-green animate-glow">
                CyberSec AI Assistant
              </h1>
              <p className="text-sm text-gray-400">by Kiran Gowda.A</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2 text-cyber-blue">
              <Brain className="h-4 w-4" />
              <span className="text-sm">GPT Model Active</span>
            </div>
            <div className="flex items-center space-x-2 text-cyber-green">
              <div className="w-2 h-2 bg-cyber-green rounded-full animate-pulse-green"></div>
              <span className="text-sm">Online</span>
            </div>
          </div>
        </div>
      </motion.header>

      {/* Warning Banner */}
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="bg-cyber-red/20 border-y border-cyber-red/50 p-2"
      >
        <div className="max-w-6xl mx-auto flex items-center justify-center space-x-2 text-cyber-red text-sm">
          <AlertTriangle className="h-4 w-4" />
          <span>FOR AUTHORIZED TESTING ONLY • EDUCATIONAL PURPOSES • ETHICAL USE REQUIRED</span>
          <AlertTriangle className="h-4 w-4" />
        </div>
      </motion.div>

      {/* Chat Container */}
      <div className="flex-1 max-w-6xl mx-auto w-full p-4 flex flex-col">
        {/* Messages */}
        <div className="flex-1 overflow-y-auto space-y-4 mb-4">
          <AnimatePresence>
            {messages.map((message) => (
              <motion.div
                key={message.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                className={`flex ${message.isUser ? 'justify-end' : 'justify-start'}`}
              >
                <div className={`max-w-2xl p-4 rounded-lg ${
                  message.isUser 
                    ? 'message-user font-mono' 
                    : 'cyber-bg cyber-border text-cyber-green'
                }`}>
                  {!message.isUser && (
                    <div className="flex items-center space-x-2 mb-2">
                      <Terminal className="h-4 w-4" />
                      <span className="text-xs font-bold text-cyber-blue">CYBERSEC_AI</span>
                      <span className="text-xs text-gray-500">
                        {message.timestamp.toLocaleTimeString()}
                      </span>
                    </div>
                  )}
                  
                  {message.isUser && (
                    <div className="flex items-center space-x-2 mb-2">
                      <Command className="h-4 w-4" />
                      <span className="text-xs font-bold">USER</span>
                      <span className="text-xs opacity-70">
                        {message.timestamp.toLocaleTimeString()}
                      </span>
                    </div>
                  )}
                  
                  <div className="whitespace-pre-wrap font-mono text-sm">
                    {message.text}
                  </div>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
          
          {isLoading && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="flex justify-start"
            >
              <div className="cyber-bg cyber-border p-4 rounded-lg">
                <div className="flex items-center space-x-2">
                  <Terminal className="h-4 w-4 text-cyber-blue" />
                  <span className="text-xs font-bold text-cyber-blue">CYBERSEC_AI</span>
                </div>
                <div className="text-cyber-green font-mono text-sm mt-2">
                  <span className="terminal-prompt"></span>
                  <span className="loading-dots">Analyzing</span>
                </div>
              </div>
            </motion.div>
          )}
          
          <div ref={messagesEndRef} />
        </div>

        {/* Input */}
        <motion.div 
          initial={{ y: 50, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          className="cyber-bg cyber-border rounded-lg p-4"
        >
          <div className="flex items-end space-x-3">
            <div className="flex-1">
              <div className="flex items-center space-x-2 mb-2">
                <Zap className="h-4 w-4 text-cyber-orange" />
                <span className="text-xs text-cyber-orange font-bold">SECURE TERMINAL</span>
              </div>
              <textarea
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Enter your cybersecurity query... (e.g., 'How do I scan for open ports safely?')"
                className="w-full bg-transparent text-cyber-green font-mono text-sm resize-none focus:outline-none placeholder-gray-500 terminal-prompt"
                rows={3}
                disabled={isLoading}
              />
            </div>
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={handleSendMessage}
              disabled={isLoading || !inputValue.trim()}
              className="p-3 bg-cyber-green text-cyber-dark rounded-lg font-bold disabled:opacity-50 disabled:cursor-not-allowed hover:bg-cyber-blue transition-colors"
            >
              <Send className="h-5 w-5" />
            </motion.button>
          </div>
          
          <div className="flex items-center justify-between text-xs text-gray-500 mt-2">
            <span>Press Enter to send • Shift+Enter for new line</span>
            <span>{inputValue.length}/500</span>
          </div>
        </motion.div>
      </div>

      {/* Footer */}
      <motion.footer 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="cyber-bg border-t border-cyber-green p-4 text-center text-xs text-gray-500"
      >
        <p>
          CyberSec AI Assistant v1.0 • Built with nanoGPT • 
          <span className="text-cyber-green"> Ethical Cybersecurity Education Only</span>
        </p>
        <p className="mt-1">
          © 2024 Kiran Gowda.A • For authorized testing and educational purposes
        </p>
      </motion.footer>
    </div>
  )
}