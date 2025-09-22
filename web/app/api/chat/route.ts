import { NextRequest, NextResponse } from 'next/server'

export async function POST(req: NextRequest) {
  try {
    const { message } = await req.json()

    if (!message || typeof message !== 'string') {
      return NextResponse.json(
        { error: 'Message is required and must be a string' },
        { status: 400 }
      )
    }

    // Security check - refuse potentially harmful requests
    const harmfulKeywords = ['exploit', 'hack', 'attack', 'illegal', 'unauthorized']
    const lowerMessage = message.toLowerCase()
    
    if (harmfulKeywords.some(keyword => lowerMessage.includes(keyword))) {
      return NextResponse.json({
        response: "I can't assist with unauthorized activities. I'm designed to help with ethical cybersecurity practices in controlled lab environments. Would you like help with defensive security measures instead?"
      })
    }

    // For production, you would integrate with your trained model here
    // This is a placeholder that simulates the model response
    const response = await generateModelResponse(message)

    return NextResponse.json({ response })

  } catch (error) {
    console.error('API Error:', error)
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    )
  }
}

async function generateModelResponse(query: string): Promise<string> {
  // Simulate model processing time
  await new Promise(resolve => setTimeout(resolve, 1000))

  const lowerQuery = query.toLowerCase()
  
  // Enhanced response patterns based on your training data
  if (lowerQuery.includes('nmap') || lowerQuery.includes('scan') || lowerQuery.includes('port')) {
    return `For ethical port scanning in authorized environments:

**Template**: \`nmap -sV -Pn <target>\`

**Explanation**:
- \`-sV\`: Service version detection
- \`-Pn\`: Skip ping (assume host is up)
- \`<target>\`: Replace with authorized IP/hostname

**Important**: Only use on systems you own or have explicit written permission to test.

**Example for lab use**:
\`nmap -sV -Pn 192.168.1.100\`

Would you like me to explain other nmap options for authorized testing?`
  }
  
  if (lowerQuery.includes('linux') || lowerQuery.includes('privilege') || lowerQuery.includes('escalation')) {
    return `For privilege escalation analysis in authorized environments:

**1. SUID Binary Analysis**:
\`find / -perm -u=s -type f 2>/dev/null\`

**2. Sudo Permissions**:
\`sudo -l\`

**3. Cron Jobs**:
\`cat /etc/crontab\`
\`ls -la /etc/cron*\`

**4. Process Analysis**:
\`ps aux | grep root\`

**5. Network Connections**:
\`netstat -tulpn\`

**Remember**: Use these commands for defensive analysis in your own lab environment. Always ensure proper authorization before system analysis.`
  }
  
  if (lowerQuery.includes('log') || lowerQuery.includes('analysis') || lowerQuery.includes('incident')) {
    return `**Incident Response Methodology**:

**1. Preparation**:
- Identify critical assets
- Document normal baseline behavior
- Prepare incident response kit

**2. Detection & Analysis**:
- Monitor logs: \`tail -f /var/log/auth.log\`
- Check failed logins: \`grep "Failed password" /var/log/auth.log\`
- Analyze connections: \`netstat -an | grep ESTABLISHED\`

**3. Containment**:
- Isolate affected systems
- Preserve evidence
- Document everything with timestamps

**4. Eradication & Recovery**:
- Remove malware/unauthorized access
- Patch vulnerabilities
- Restore from clean backups

**5. Post-Incident**:
- Lessons learned documentation
- Update security measures
- Staff training

Need help with specific log analysis techniques?`
  }

  if (lowerQuery.includes('sql') || lowerQuery.includes('injection') || lowerQuery.includes('web')) {
    return `**Web Application Security - Defensive Approach**:

**SQL Injection Prevention**:
- Use parameterized queries/prepared statements
- Input validation and sanitization
- Principle of least privilege for database accounts

**Example (Safe)**:
\`\`\`python
# Good - Parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Bad - Vulnerable to injection
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
\`\`\`

**Testing in Lab Environment**:
- Use tools like OWASP ZAP for authorized testing
- Set up vulnerable apps like DVWA for learning
- Practice secure coding patterns

**Key Principle**: Always focus on secure development and authorized testing environments.`
  }

  // Default response for general cybersecurity queries
  return `I'm your CyberSec AI Assistant, trained on ethical cybersecurity practices. I can help with:

🔒 **Authorized Penetration Testing**
• Network reconnaissance (lab environments)
• Service enumeration techniques
• Ethical hacking methodologies

🐧 **Linux Security**
• System hardening procedures
• Log analysis and monitoring
• Privilege escalation detection

🌐 **Network Security**
• Firewall configuration
• Network segmentation
• Traffic analysis

📊 **Incident Response**
• Evidence collection procedures
• Threat hunting techniques
• Recovery strategies

Please specify what area you'd like help with, and remember - all guidance is for authorized testing environments only!

**Example queries**:
- "How do I securely scan for open ports?"
- "What are signs of privilege escalation?"
- "How do I analyze suspicious log entries?"`
}

export async function GET() {
  return NextResponse.json({
    message: 'CyberSec AI Assistant API is running',
    version: '1.0.0',
    status: 'healthy'
  })
}