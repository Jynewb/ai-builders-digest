// ===== AI Builders Digest - Frontend =====

const DATA_FILE = 'data/digest.json';
const REFRESH_INTERVAL = 30 * 60 * 1000; // 30 minutes

// ===== Init =====
document.addEventListener('DOMContentLoaded', () => {
  setCurrentDate();
  loadDigest();
  setInterval(loadDigest, REFRESH_INTERVAL);
});

function setCurrentDate() {
  const now = new Date();
  const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
  const formatted = new Intl.DateTimeFormat('zh-CN', options).format(now);
  document.getElementById('currentDate').textContent = formatted;
}

async function loadDigest() {
  const container = document.getElementById('digestContainer');
  
  try {
    const response = await fetch(DATA_FILE + '?t=' + Date.now());
    if (!response.ok) throw new Error('Failed to load digest');
    
    const data = await response.json();
    renderDigest(data);
  } catch (error) {
    console.error('Error loading digest:', error);
    container.innerHTML = `
      <div class="empty-state">
        <h3>暂无内容</h3>
        <p>今天的 digest 还在准备中，请稍后再来。</p>
        <p style="margin-top: 12px; font-size: 0.85rem;">数据将在每天早上 7:50 (北京时间) 自动更新</p>
      </div>
    `;
  }
}

function renderDigest(data) {
  const container = document.getElementById('digestContainer');
  const { builders = [], date = '', stats = {} } = data;
  
  // Update stats
  const totalTweets = stats.totalTweets || builders.reduce((sum, b) => sum + (b.tweets?.length || 0), 0);
  const totalBuilders = builders.length;
  document.getElementById('totalStats').textContent = 
    `${totalBuilders} builders · ${totalTweets} posts`;
  
  if (!builders || builders.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <h3>今天的 digest 还在准备中</h3>
        <p>数据将在每天早上 7:50 (北京时间) 自动更新</p>
      </div>
    `;
    return;
  }
  
  let html = `<p class="section-title">X / Twitter · ${date}</p>`;
  
  builders.forEach(builder => {
    if (!builder.tweets || builder.tweets.length === 0) return;
    
    const initial = builder.name ? builder.name.charAt(0).toUpperCase() : '?';
    
    html += `
      <section class="builder-section">
        <div class="builder-header">
          <div class="builder-avatar">${initial}</div>
          <div class="builder-info">
            <h2>${escapeHtml(builder.name || 'Unknown')}</h2>
            <p class="builder-bio">
              ${builder.bio ? escapeHtml(builder.bio) : ''}
              ${builder.handle ? `<span class="builder-handle">@${escapeHtml(builder.handle)}</span>` : ''}
            </p>
          </div>
        </div>
        
        ${builder.tweets.map(tweet => renderTweet(tweet)).join('')}
      </section>
    `;
  });
  
  container.innerHTML = html;
}

function renderTweet(tweet) {
  const { text = '', textZh = '', likes = 0, retweets = 0, replies = 0, url = '', createdAt = '' } = tweet;
  
  // Chinese priority: show textZh if available, else English
  const displayText = textZh || text;
  const dateStr = createdAt ? formatDate(createdAt) : '';
  
  // SVG icons
  const heartIcon = `<svg class="stat-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>`;
  const rtIcon = `<svg class="stat-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5 0-.28-.03-.56-.08-.83A7.72 7.72 0 0023 3z"/></svg>`;
  const replyIcon = `<svg class="stat-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>`;
  const linkIcon = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/></svg>`;
  
  return `
    <article class="tweet-card">
      <div class="tweet-content">
        <p class="tweet-text">${autoLink(escapeHtml(displayText))}</p>
      </div>
      <div class="tweet-meta">
        <div class="tweet-stats">
          <span class="stat likes">${heartIcon} ${formatNumber(likes)}</span>
          <span class="stat retweets">${rtIcon} ${formatNumber(retweets)}</span>
          <span class="stat replies">${replyIcon} ${formatNumber(replies)}</span>
          ${dateStr ? `<span class="stat">${dateStr}</span>` : ''}
        </div>
        ${url ? `<a href="${escapeHtml(url)}" target="_blank" rel="noopener" class="tweet-link">${linkIcon} 查看原文</a>` : ''}
      </div>
    </article>
  `;
}

function parseBilingual(tweet) {
  const text = tweet.text || '';
  const textZh = tweet.textZh || '';
  
  if (textZh) {
    return { en: text, zh: textZh };
  }
  
  // Fallback: try to detect Chinese in text
  const chineseRegex = /[\u4e00-\u9fa5]/;
  if (chineseRegex.test(text)) {
    return { en: '', zh: text };
  }
  
  return { en: text, zh: '' };
}

function autoLink(text) {
  // Convert URLs to links
  const urlRegex = /(https?:\/\/[^\s<>"]+)/g;
  return text.replace(urlRegex, '<a href="$1" target="_blank" rel="noopener">$1</a>');
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

function formatNumber(num) {
  if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'k';
  }
  return num.toString();
}

function formatDate(dateStr) {
  try {
    const date = new Date(dateStr);
    const now = new Date();
    const diff = now - date;
    
    // Less than 24 hours
    if (diff < 24 * 60 * 60 * 1000) {
      const hours = Math.floor(diff / (60 * 60 * 1000));
      if (hours > 0) return `${hours}h ago`;
      const mins = Math.floor(diff / (60 * 1000));
      return `${mins}m ago`;
    }
    
    // Format as date
    const month = date.getMonth() + 1;
    const day = date.getDate();
    return `${month}/${day}`;
  } catch {
    return '';
  }
}

function markdownToHtml(text) {
  if (!text) return '';
  // Escape HTML first
  let html = escapeHtml(text);
  // Bold: **text**
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  // Links: [text](url)
  html = html.replace(/\[(.*?)\]\((https?:\/\/[^\s<>"]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  // Line breaks
  html = html.replace(/\n/g, '<br>');
  return html;
}
