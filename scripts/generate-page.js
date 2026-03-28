#!/usr/bin/env node

/**
 * AI Builders Digest - Page Generator
 * 
 * Fetches the latest digest data from follow-builders feed,
 * processes it, and saves as JSON for the frontend.
 * 
 * Usage: node generate-page.js
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

// ===== Config =====
const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT_DIR = join(__dirname, '..');
const DATA_DIR = join(ROOT_DIR, 'data');
const OUTPUT_FILE = join(DATA_DIR, 'digest.json');

// Default feed URLs
const FEED_X_URL = process.env.FEED_X_URL || 'https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-x.json';
const FEED_PODCASTS_URL = process.env.FEED_PODCASTS_URL || 'https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-podcasts.json';

// ===== Fetch =====
async function fetchJSON(url) {
  try {
    const res = await fetch(url);
    if (!res.ok) {
      console.error(`Failed to fetch ${url}: ${res.status}`);
      return null;
    }
    return res.json();
  } catch (error) {
    console.error(`Error fetching ${url}:`, error.message);
    return null;
  }
}

// ===== Process Builders =====
function processBuilders(feedData) {
  if (!feedData || !feedData.x) return [];
  
  const builders = [];
  
  for (const builder of feedData.x) {
    if (!builder.tweets || builder.tweets.length === 0) continue;
    
    // Process tweets - only keep substantive ones
    const processedTweets = builder.tweets
      .map(tweet => ({
        id: tweet.id,
        text: tweet.text,
        createdAt: tweet.createdAt,
        url: tweet.url,
        likes: tweet.likes || 0,
        retweets: tweet.retweets || 0,
        replies: tweet.replies || 0,
        isQuote: tweet.isQuote,
      }))
      .filter(tweet => isSubstantive(tweet.text));
    
    if (processedTweets.length === 0) continue;
    
    builders.push({
      name: builder.name,
      handle: builder.handle,
      bio: builder.bio || '',
      tweets: processedTweets,
    });
  }
  
  return builders;
}

// Filter for substantive tweets
function isSubstantive(text) {
  if (!text) return false;
  
  // Skip very short tweets
  if (text.length < 50) return false;
  
  // Skip pure engagement bait
  const lowValuePatterns = [
    /^wow/i,
    /^(lol|haha|great|amazing|awesome|love this)/i,
    /congrats/i,
    /thank you/i,
    /welcome back/i,
  ];
  
  for (const pattern of lowValuePatterns) {
    if (pattern.test(text.trim())) return false;
  }
  
  return true;
}

// ===== Process Podcasts =====
function processPodcasts(feedData) {
  if (!feedData || !feedData.podcasts) return [];
  
  return feedData.podcasts.map(podcast => ({
    name: podcast.name,
    title: podcast.title || '',
    url: podcast.url || '',
    description: podcast.description || '',
  }));
}

// ===== Get Date String =====
function getDateString() {
  const now = new Date();
  const beijingTime = new Date(now.toLocaleString('en-US', { timeZone: 'Asia/Shanghai' }));
  
  const year = beijingTime.getFullYear();
  const month = String(beijingTime.getMonth() + 1).padStart(2, '0');
  const day = String(beijingTime.getDate()).padStart(2, '0');
  
  return `${year}-${month}-${day}`;
}

// ===== Main =====
async function main() {
  console.log('🔄 Fetching latest digest data...');
  
  // Ensure data directory exists
  if (!existsSync(DATA_DIR)) {
    mkdirSync(DATA_DIR, { recursive: true });
  }
  
  // Fetch feeds
  const [feedX, feedPodcasts] = await Promise.all([
    fetchJSON(FEED_X_URL),
    fetchJSON(FEED_PODCASTS_URL),
  ]);
  
  if (!feedX) {
    console.error('❌ Failed to fetch X feed, using cached data if available');
    // Try to read existing data
    if (existsSync(OUTPUT_FILE)) {
      console.log('📄 Using existing digest.json');
      return;
    } else {
      // Create empty placeholder
      writeFileSync(OUTPUT_FILE, JSON.stringify({ 
        builders: [], 
        podcasts: [],
        date: getDateString(),
        stats: { totalTweets: 0, totalBuilders: 0 }
      }, null, 2));
      return;
    }
  }
  
  // Process data
  const builders = processBuilders(feedX);
  const podcasts = processPodcasts(feedPodcasts);
  const totalTweets = builders.reduce((sum, b) => sum + b.tweets.length, 0);
  
  // Build output
  const digest = {
    date: feedX.generatedAt ? new Date(feedX.generatedAt).toLocaleDateString('zh-CN', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    }) : getDateString(),
    builders,
    podcasts,
    stats: {
      totalTweets,
      totalBuilders: builders.length,
      totalPodcasts: podcasts.length,
      feedGeneratedAt: feedX.generatedAt,
    },
  };
  
  // Save
  writeFileSync(OUTPUT_FILE, JSON.stringify(digest, null, 2));
  console.log(`✅ Saved digest: ${builders.length} builders, ${totalTweets} tweets, ${podcasts.length} podcasts`);
}

main().catch(console.error);
