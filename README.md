# 🚀 Job Portal Skills API

A comprehensive RESTful API that provides detailed skills information for various job positions. Perfect for job portals, career websites, recruitment platforms, and skill assessment tools.

**Live API:** [https://job-potal-skill-api.vercel.app/](https://job-potal-skill-api.vercel.app/)

---

## 📋 Overview

This API provides:

- **36+ Job Positions** across Technology, Design, Business, and Finance domains
- **100-200+ Skills per Position** including modern frameworks, tools, and technologies
- **Updated for 2025** with the latest industry-relevant skills
- **Secure API Key Authentication** to protect your data
- **Fast & Scalable** - Deployed on Vercel's edge network

---

## 🔑 API Access

### Get Your API Key

This API requires authentication using an API key. To get access:

**📧 Email:** [chamath@chamathdilshan.com](mailto:chamath@chamathdilshan.com)

**Subject:** API Key Request - Job Portal Skills API

**Include:**

- Your name/company
- Use case description
- Expected usage volume

You'll receive your API key within 24 hours!

---

## 🚀 Quick Start

### Making Your First Request

```bash
curl -X GET "https://job-potal-skill-api.vercel.app/api/positions" \
     -H "X-API-Key: your_api_key_here"
```

### Response Example

```json
{
  "positions": [
    "Software Developer",
    "Data Scientist",
    "UI/UX Designer",
    "Product Manager",
    ...
  ],
  "total_count": 36
}
```

---

## 📍 Available Endpoints

### 1. Root Endpoint (Public)

**GET** `/`

No authentication required. Returns API information.

```bash
curl https://job-potal-skill-api.vercel.app/
```

---

### 2. Get All Positions

**GET** `/api/positions`

Returns a list of all available job positions.

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     https://job-potal-skill-api.vercel.app/api/positions
```

**Response:**

```json
{
  "positions": ["Software Developer", "Data Scientist", ...],
  "total_count": 36
}
```

---

### 3. Get Skills for Position

**GET** `/api/skills/{position}`

Get detailed skills list for a specific job position.

**Path Parameters:**

- `position` (string): Job position name

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     "https://job-potal-skill-api.vercel.app/api/skills/Software Developer"
```

**Response:**

```json
{
  "position": "Software Developer",
  "skills": [
    "JavaScript",
    "TypeScript",
    "React",
    "Next.js",
    "Node.js",
    "Docker",
    ...
  ],
  "skills_count": 150
}
```

---

### 4. Search Position Suggestions

**GET** `/api/suggestions?q={query}`

Search for position suggestions based on a query string.

**Query Parameters:**

- `q` (string): Search query (minimum 2 characters)

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     "https://job-potal-skill-api.vercel.app/api/suggestions?q=engineer"
```

**Response:**

```json
{
  "query": "engineer",
  "suggestions": [
    "Software Engineer",
    "DevOps Engineer",
    "Cloud Engineer",
    ...
  ]
}
```

---

### 5. Get All Categories

**GET** `/api/categories`

Get all job categories available in the system.

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     https://job-potal-skill-api.vercel.app/api/categories
```

---

### 6. Get All Jobs with Categories

**GET** `/api/all-jobs`

Get all job positions organized by categories.

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     https://job-potal-skill-api.vercel.app/api/all-jobs
```

---

## 💻 Code Examples

### JavaScript (Fetch API)

```javascript
const API_KEY = 'your_api_key_here';
const BASE_URL = 'https://job-potal-skill-api.vercel.app';

async function getSkills(position) {
  const response = await fetch(`${BASE_URL}/api/skills/${position}`, {
    headers: {
      'X-API-Key': API_KEY,
    },
  });

  const data = await response.json();
  console.log(data);
}

getSkills('Software Developer');
```

### Python (Requests)

```python
import requests

API_KEY = 'your_api_key_here'
BASE_URL = 'https://job-potal-skill-api.vercel.app'

headers = {'X-API-Key': API_KEY}

# Get all positions
response = requests.get(f'{BASE_URL}/api/positions', headers=headers)
positions = response.json()

# Get skills for a position
response = requests.get(
    f'{BASE_URL}/api/skills/Data Scientist',
    headers=headers
)
skills = response.json()
print(skills)
```

### Node.js (Axios)

```javascript
const axios = require('axios');

const API_KEY = 'your_api_key_here';
const BASE_URL = 'https://job-potal-skill-api.vercel.app';

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'X-API-Key': API_KEY,
  },
});

// Get all positions
api.get('/api/positions').then(response => console.log(response.data));

// Get skills
api
  .get('/api/skills/Frontend Developer')
  .then(response => console.log(response.data));
```

---

## 🎯 Available Job Positions

### Technology (18 positions)

- Software Developer
- Software Engineer
- Full Stack Developer
- Frontend Developer
- Backend Developer
- Mobile Developer
- DevOps Engineer
- Cloud Engineer
- Data Scientist
- Data Analyst
- Data Engineer
- Machine Learning Engineer
- AI Engineer
- Quality Assurance Engineer
- QA Tester
- System Administrator
- Network Engineer
- Security Engineer

### Design & Product (5 positions)

- UI/UX Designer
- Graphic Designer
- Web Designer
- Product Manager
- Technical Writer

### Business & Management (8 positions)

- Project Manager
- Business Analyst
- Scrum Master
- Marketing Manager
- Sales Manager
- Customer Success Manager
- HR Manager
- Digital Marketing Specialist

### Finance & Other (5 positions)

- Financial Analyst
- Accountant
- Database Administrator
- Content Writer
- SEO Specialist

---

## 🛠️ Tech Stack

- **Framework:** FastAPI (Python)
- **Deployment:** Vercel (Serverless)
- **Authentication:** API Key (X-API-Key header)
- **Data:** 5000+ skills across 36+ positions

---

## 📖 Documentation

### Interactive API Documentation

Visit the live API documentation (requires API key):

- **Swagger UI:** [https://job-potal-skill-api.vercel.app/docs](https://job-potal-skill-api.vercel.app/docs)
- **ReDoc:** [https://job-potal-skill-api.vercel.app/redoc](https://job-potal-skill-api.vercel.app/redoc)

---

## 🔒 Security

- ✅ API Key Authentication required for all endpoints (except root)
- ✅ Rate limiting enabled
- ✅ CORS configured for secure access
- ✅ No personal data storage
- ✅ Secure environment variable management

---

## 📊 Response Format

All API responses follow this structure:

### Success Response (200)

```json
{
  "position": "Software Developer",
  "skills": [...],
  "skills_count": 150
}
```

### Error Response (401 Unauthorized)

```json
{
  "detail": "Invalid or missing API Key"
}
```

### Error Response (404 Not Found)

```json
{
  "detail": "Position not found"
}
```

---

## 💡 Use Cases

- **Job Portals:** Display required skills for job postings
- **Career Websites:** Help users understand skill requirements
- **Recruitment Platforms:** Match candidates with required skills
- **Learning Platforms:** Create skill-based learning paths
- **Resume Builders:** Suggest relevant skills for positions
- **Skill Assessment Tools:** Build position-specific tests

---

## 📞 Contact & Support

**Developer:** Chamath Dilshan

**Email:** [chamath@chamathdilshan.com](mailto:chamath@chamathdilshan.com)

**For:**

- API Key requests
- Technical support
- Feature requests
- Bug reports
- Partnership inquiries

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Features Coming Soon

- [ ] Industry-specific skill filtering
- [ ] Skill level indicators (Beginner/Intermediate/Advanced)
- [ ] Skill trends and popularity metrics
- [ ] Custom skill recommendations
- [ ] Batch processing endpoints
- [ ] Webhook support

---

## 📈 API Status

- **Status:** ✅ Live and Operational
- **Uptime:** 99.9%
- **Region:** Global (Vercel Edge Network)
- **Response Time:** < 100ms average

---

## 🤝 Contributing

While this is a private API, we welcome feedback and suggestions!

Email us at [chamath@chamathdilshan.com](mailto:chamath@chamathdilshan.com) with:

- Feature suggestions
- Missing skills or positions
- Bug reports
- Documentation improvements

---

## ⚡ Rate Limits

- **Free Tier:** 1000 requests/day
- **Pro Tier:** Custom limits available

Contact us for enterprise plans!

---

**Made with ❤️ by Chamath Dilshan**

**Live API:** [https://job-potal-skill-api.vercel.app/](https://job-potal-skill-api.vercel.app/)
