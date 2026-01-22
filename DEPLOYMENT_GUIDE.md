# 🚀 Deployment Guide: Automobile Sales Dashboard

This guide will help you deploy your Dash dashboard to **Render** (free tier available, easiest option).

## Option 1: Render (Recommended - Easiest)

### Step 1: Prepare Your Repository

1. **Make sure your project structure looks like this:**
   ```
   Automobile-Sales-Recession-Analysis/
   ├── data/
   │   └── automobile_sales.csv
   ├── dashboard/
   │   └── app.py
   ├── requirements.txt
   ├── Procfile
   └── README.md
   ```

2. **Copy the CSV file to the dashboard folder** (for easier access):
   ```bash
   # On Windows PowerShell:
   Copy-Item data\automobile_sales.csv dashboard\
   
   # On Mac/Linux:
   cp data/automobile_sales.csv dashboard/
   ```

### Step 2: Update requirements.txt

Add `gunicorn` to your requirements.txt (already done if you used the one I created).

### Step 3: Create GitHub Repository

1. **Initialize git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Dashboard ready for deployment"
   ```

2. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Name it: `Automobile-Sales-Recession-Analysis`
   - Don't initialize with README (you already have one)
   - Click "Create repository"

3. **Push your code:**
   ```bash
   git remote add origin https://github.com/alinazir105/Automobile-Sales-Recession-Analysis.git
   git branch -M main
   git push -u origin main
   ```

### Step 4: Deploy to Render

1. **Sign up/Login to Render:**
   - Go to https://render.com
   - Sign up with your GitHub account (free)

2. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select `Automobile-Sales-Recession-Analysis`

3. **Configure Settings:**
   - **Name**: `automobile-sales-dashboard` (or any name you like)
   - **Environment**: `Python 3`
   - **Python Version**: `3.11.9` (IMPORTANT: Set this in Advanced settings)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn dashboard.app:server`
   - **Plan**: Free (for now)
   
   **Note**: Make sure to set Python version to 3.11.9 in Advanced settings to avoid compatibility issues!

4. **Add Environment Variables** (if needed):
   - Usually not needed for this project

5. **Click "Create Web Service"**
   - Render will automatically build and deploy
   - Wait 5-10 minutes for first deployment

6. **Get Your Live URL:**
   - Once deployed, you'll get a URL like: `https://automobile-sales-dashboard.onrender.com`
   - Add this to your README!

### Step 5: Update README with Live Link

Add this to your README.md:
```markdown
## 🌐 Live Demo

[View Live Dashboard](https://your-app-name.onrender.com)
```

---

## Option 2: Heroku (Alternative)

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

### Steps:

1. **Install Heroku CLI:**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create Heroku App:**
   ```bash
   heroku create your-app-name
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

5. **Open your app:**
   ```bash
   heroku open
   ```

---

## Option 3: Streamlit Cloud (If Converting to Streamlit)

**Note**: Your current app is Dash, not Streamlit. If you want to use Streamlit Cloud, you'd need to convert the dashboard. This is more work but Streamlit Cloud is very easy to use.

---

## Troubleshooting

### Common Issues:

1. **"Module not found" errors:**
   - Make sure all dependencies are in `requirements.txt`
   - Check that versions are compatible

2. **"File not found" errors:**
   - Make sure CSV file is in the right location
   - Check the path in `app.py`

3. **App crashes on startup:**
   - Check Render/Heroku logs
   - Make sure `gunicorn` is in requirements.txt
   - Verify `Procfile` is correct

4. **Slow loading:**
   - First load on free tier can be slow (cold start)
   - This is normal for free hosting

---

## Testing Locally Before Deployment

Test that your app works with gunicorn locally:

```bash
# Install gunicorn
pip install gunicorn

# Test run
cd dashboard
gunicorn app:server
```

Then visit `http://localhost:8000`

---

## Next Steps After Deployment

1. ✅ Add live demo link to README
2. ✅ Test all dashboard features on live site
3. ✅ Share link in your portfolio/resume
4. ✅ Update LinkedIn/GitHub with project link

---

**Need Help?** Check Render's documentation: https://render.com/docs

