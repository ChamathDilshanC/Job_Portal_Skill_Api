# 🚀 Job Portal Skills API

A comprehensive RESTful API that provides detailed skills information for various job positions. Perfect for job portals, career websites, recruitment platforms, and skill assessment tools.

**Live API:** [https://job-potal-skill-api.vercel.app/](https://job-potal-skill-api.vercel.app/)

---

## 📋 Overview

This API provides:

- **36+ Job Positions** across Technology, Design, Business, and Finance domains
- **100-200+ Skills per Position** including modern frameworks, tools, and technologies
- **400+ Academic Degrees & Certifications** from undergraduate to professional qualifications
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

### 7. Get All Degrees

**GET** `/api/degrees`

Get all available academic degrees and certifications (400+ degrees).

**Query Parameters:**

- `limit` (optional): Maximum number of degrees to return (1-500, default: 100)

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     "https://job-potal-skill-api.vercel.app/api/degrees?limit=50"
```

**Response:**

```json
{
  "degrees": [
    "Bachelor of Science (BSc)",
    "Master of Business Administration (MBA)",
    "Doctor of Philosophy (PhD)",
    ...
  ],
  "total_count": 400
}
```

---

### 8. Search Degrees

**GET** `/api/degrees/search?q={query}`

Search for degrees based on a query string.

**Query Parameters:**

- `q` (string): Search query (minimum 1 character)
- `limit` (optional): Maximum results (1-50, default: 10)

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     "https://job-potal-skill-api.vercel.app/api/degrees/search?q=computer&limit=10"
```

**Response:**

```json
{
  "degrees": [
    "Bachelor of Science in Computer Science (BSc CS)",
    "Master of Computer Applications (MCA)",
    "Diploma in Computer Science",
    ...
  ],
  "query": "computer",
  "total_count": 10
}
```

---

### 9. Get Degree Categories

**GET** `/api/degrees/categories`

Get all degree categories (Undergraduate, Graduate, Doctoral, Diplomas, Professional).

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     https://job-potal-skill-api.vercel.app/api/degrees/categories
```

---

### 10. Get Degrees by Category

**GET** `/api/degrees/categories/{category}`

Get degrees from a specific category.

**Path Parameters:**

- `category` (string): Category name (undergraduate, graduate, doctoral, diplomas, professional)

**Headers:**

- `X-API-Key`: Your API key (required)

**Example:**

```bash
curl -H "X-API-Key: your_api_key" \
     "https://job-potal-skill-api.vercel.app/api/degrees/categories/undergraduate"
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

// Search degrees
api
  .get('/api/degrees/search?q=computer')
  .then(response => console.log(response.data));
```

---

## 🎓 Degree Database

The API includes **400+ academic degrees and professional certifications**:

### Categories

- **Undergraduate** (70+): Bachelor's degrees (BSc, BA, BEng, BTech, BBA, etc.)
- **Graduate** (80+): Master's degrees (MSc, MA, MBA, MEng, MCA, etc.)
- **Doctoral** (20+): PhD, MD, DBA, EdD, and other professional doctorates
- **Diplomas** (50+): Various diploma and certificate programs
- **Professional** (40+): CA, CPA, PMP, CFA, CISSP, AWS, etc.
- **Associate** (8+): AA, AS, AAS degrees
- **International** (10+): A-Levels, IB, Baccalauréat, etc.

### Fields Covered

- Computer Science & IT
- Engineering (All disciplines)
- Business & Management
- Finance & Accounting
- Health Sciences
- Law
- Education
- Arts & Humanities
- Science & Research

📖 **[View Complete Degrees API Documentation](./API_DEGREES.md)**

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
