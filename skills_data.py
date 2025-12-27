"""
Job positions and their relevant skills database
Contains 40-50 skills for each job position
"""

# List of common job positions
common_positions = [
    'Software Developer',
    'Software Engineer',
    'Full Stack Developer',
    'Frontend Developer',
    'Backend Developer',
    'Mobile Developer',
    'DevOps Engineer',
    'Data Scientist',
    'Data Analyst',
    'Data Engineer',
    'Machine Learning Engineer',
    'AI Engineer',
    'Product Manager',
    'Project Manager',
    'UI/UX Designer',
    'Graphic Designer',
    'Web Designer',
    'Business Analyst',
    'Quality Assurance Engineer',
    'QA Tester',
    'System Administrator',
    'Network Engineer',
    'Security Engineer',
    'Cloud Engineer',
    'Database Administrator',
    'Technical Writer',
    'Scrum Master',
    'Marketing Manager',
    'Sales Manager',
    'Customer Success Manager',
    'HR Manager',
    'Financial Analyst',
    'Accountant',
    'Content Writer',
    'SEO Specialist',
    'Digital Marketing Specialist',
]

# Skills database for each job position (40-50 skills each)
job_skills = {
    'software developer': [
        # Programming Languages
        'JavaScript', 'TypeScript', 'Python', 'Java', 'C++', 'C#', 'Go', 'Ruby', 'PHP', 'Swift',
        'Kotlin', 'Rust', 'Scala', 'Dart',
        # Frontend Frameworks & Libraries
        'React', 'Next.js', 'React Native', 'Angular', 'Vue.js', 'Nuxt.js', 'Svelte', 'SvelteKit',
        'Solid.js', 'Remix', 'Astro', 'Qwik',
        # Backend Frameworks
        'Node.js', 'Express.js', 'NestJS', 'Fastify', 'Django', 'Flask', 'FastAPI', 'Spring Boot',
        'ASP.NET Core', 'Ruby on Rails', 'Laravel', 'Symfony',
        # Version Control & Collaboration
        'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Git Flow', 'GitHub Actions', 'GitLab CI',
        # Containerization & Orchestration
        'Docker', 'Docker Compose', 'Kubernetes', 'Helm', 'Podman',
        # Cloud Platforms
        'AWS', 'Azure', 'Google Cloud', 'Vercel', 'Netlify', 'Railway', 'Render', 'Fly.io',
        'DigitalOcean', 'Heroku', 'Cloudflare',
        # APIs & Communication
        'REST APIs', 'GraphQL', 'gRPC', 'WebSockets', 'Socket.io', 'tRPC', 'Swagger', 'OpenAPI',
        # Databases
        'SQL', 'PostgreSQL', 'MySQL', 'MongoDB', 'Redis', 'Elasticsearch', 'SQLite', 'Supabase',
        'Firebase', 'PlanetScale', 'Neon', 'Prisma', 'TypeORM', 'Sequelize', 'Mongoose',
        # Frontend Tools & Build Tools
        'Webpack', 'Vite', 'Turbopack', 'esbuild', 'Rollup', 'Parcel', 'npm', 'Yarn', 'pnpm', 'Bun',
        # Testing
        'Jest', 'Vitest', 'Mocha', 'Chai', 'Cypress', 'Playwright', 'Puppeteer', 'Selenium',
        'Testing Library', 'Pytest', 'JUnit', 'TestNG', 'TDD', 'BDD', 'Unit Testing',
        # CSS & Styling
        'HTML5', 'CSS3', 'Sass', 'SCSS', 'Less', 'Tailwind CSS', 'Bootstrap', 'Material-UI',
        'Chakra UI', 'shadcn/ui', 'DaisyUI', 'Styled Components', 'CSS Modules', 'PostCSS',
        # State Management
        'Redux', 'Redux Toolkit', 'Zustand', 'Recoil', 'Jotai', 'MobX', 'Context API', 'Pinia', 'Vuex',
        # DevOps & CI/CD
        'CI/CD', 'Jenkins', 'CircleCI', 'Travis CI', 'GitHub Actions', 'GitLab CI/CD', 'Azure DevOps',
        # Monitoring & Logging
        'Sentry', 'LogRocket', 'Datadog', 'New Relic', 'Prometheus', 'Grafana',
        # Methodologies
        'Agile', 'Scrum', 'Kanban', 'TDD', 'Clean Code', 'SOLID Principles', 'Design Patterns',
        'Microservices', 'Serverless', 'Monorepos', 'Turborepo', 'Nx',
    ],

    'software engineer': [
        # Programming Languages
        'JavaScript', 'TypeScript', 'Python', 'Java', 'C++', 'C#', 'Go', 'Rust', 'Scala', 'Kotlin',
        # Algorithms & CS Fundamentals
        'Algorithms', 'Data Structures', 'Big O Notation', 'Time Complexity', 'Space Complexity',
        'Binary Trees', 'Graphs', 'Hash Tables', 'Dynamic Programming', 'Recursion', 'Sorting Algorithms',
        # System Design
        'System Design', 'Distributed Systems', 'Scalability', 'High Availability', 'CAP Theorem',
        'Load Balancing', 'Caching Strategies', 'Database Sharding', 'Microservices Architecture',
        'Event-Driven Architecture', 'Message Queues', 'API Gateway', 'Service Mesh',
        # Programming Paradigms
        'Object-Oriented Programming', 'Functional Programming', 'Reactive Programming',
        # Design Patterns & Principles
        'Design Patterns', 'SOLID Principles', 'DRY Principle', 'KISS Principle', 'YAGNI',
        'Clean Code', 'Clean Architecture', 'Domain-Driven Design', 'Hexagonal Architecture',
        # Version Control
        'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Git Flow', 'Trunk-Based Development',
        'Code Review', 'Pull Requests', 'Merge Strategies', 'Git Rebase',
        # Testing
        'Testing', 'Unit Testing', 'Integration Testing', 'E2E Testing', 'TDD', 'BDD',
        'Test Coverage', 'Mocking', 'Jest', 'Vitest', 'Pytest', 'JUnit', 'TestNG', 'Mockito',
        'Cypress', 'Playwright', 'Selenium',
        # Cloud & Infrastructure
        'AWS', 'EC2', 'S3', 'Lambda', 'Azure', 'Google Cloud', 'Cloud Architecture',
        'Docker', 'Kubernetes', 'Helm', 'Container Orchestration', 'Serverless',
        # CI/CD & DevOps
        'CI/CD', 'Jenkins', 'GitHub Actions', 'GitLab CI', 'CircleCI', 'Travis CI',
        'DevOps', 'Infrastructure as Code', 'Terraform', 'Ansible',
        # Databases
        'SQL', 'PostgreSQL', 'MySQL', 'NoSQL', 'MongoDB', 'Redis', 'Elasticsearch',
        'Database Design', 'Database Optimization', 'Indexing', 'Query Optimization',
        # APIs
        'REST APIs', 'GraphQL', 'gRPC', 'WebSockets', 'API Design', 'API Versioning',
        'Swagger', 'OpenAPI', 'Postman',
        # Performance & Optimization
        'Performance Optimization', 'Profiling', 'Memory Management', 'Garbage Collection',
        'Concurrency', 'Multithreading', 'Async/Await', 'Parallelism',
        # Security
        'Security Best Practices', 'OWASP', 'Authentication', 'Authorization', 'Encryption',
        'SSL/TLS', 'JWT', 'OAuth', 'Security Auditing',
        # Monitoring & Logging
        'Monitoring', 'Logging', 'Observability', 'Prometheus', 'Grafana', 'ELK Stack',
        'Sentry', 'Datadog', 'New Relic',
        # Methodologies & Practices
        'Agile', 'Scrum', 'Kanban', 'Extreme Programming', 'Pair Programming',
        'Code Documentation', 'Technical Writing', 'Technical Communication',
        'Debugging', 'Troubleshooting', 'Problem Solving', 'Critical Thinking',
        'Refactoring', 'Code Smells', 'Legacy Code Management',
        # Collaboration
        'Team Collaboration', 'Cross-Functional Teams', 'Mentoring', 'Leadership',
        'Communication Skills', 'Presentation Skills',
    ],

    'full stack developer': [
        # Programming Languages
        'JavaScript', 'TypeScript', 'Python', 'Java', 'Go', 'Ruby', 'PHP',
        # Frontend Technologies
        'HTML5', 'CSS3', 'React', 'Next.js', 'Vue.js', 'Nuxt.js', 'Angular', 'Svelte', 'SvelteKit',
        'Remix', 'Astro', 'Solid.js',
        # Frontend Styling & UI
        'Tailwind CSS', 'Bootstrap', 'Material-UI', 'Chakra UI', 'shadcn/ui', 'Ant Design',
        'Styled Components', 'CSS Modules', 'Sass', 'SCSS', 'Responsive Design', 'Mobile-First Design',
        # Backend Frameworks
        'Node.js', 'Express.js', 'NestJS', 'Fastify', 'Koa', 'Django', 'Flask', 'FastAPI',
        'Spring Boot', 'ASP.NET Core', 'Ruby on Rails', 'Laravel',
        # Databases & ORM
        'PostgreSQL', 'MySQL', 'MongoDB', 'Redis', 'SQLite', 'Prisma', 'TypeORM', 'Sequelize',
        'Mongoose', 'Drizzle', 'Supabase', 'Firebase', 'PlanetScale', 'Neon',
        # APIs
        'REST APIs', 'GraphQL', 'Apollo', 'tRPC', 'WebSockets', 'Socket.io', 'Server-Sent Events',
        'Swagger', 'OpenAPI',
        # Authentication & Security
        'JWT', 'OAuth', 'OAuth2', 'NextAuth', 'Auth0', 'Clerk', 'Supabase Auth', 'Firebase Auth',
        'Passport.js', 'bcrypt', 'Security Best Practices',
        # Version Control & Git
        'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Git Flow', 'Pull Requests', 'Code Review',
        # Cloud & Deployment
        'AWS', 'S3', 'EC2', 'Lambda', 'Azure', 'Google Cloud', 'Vercel', 'Netlify', 'Railway',
        'Render', 'Fly.io', 'DigitalOcean', 'Heroku', 'Cloudflare Pages',
        # DevOps & Containers
        'Docker', 'Docker Compose', 'Kubernetes', 'CI/CD', 'GitHub Actions', 'GitLab CI',
        'Jenkins', 'Nginx', 'Apache', 'PM2',
        # Testing
        'Jest', 'Vitest', 'Cypress', 'Playwright', 'Testing Library', 'Postman', 'Insomnia',
        'Unit Testing', 'Integration Testing', 'E2E Testing', 'TDD',
        # Build Tools & Package Managers
        'Webpack', 'Vite', 'Turbopack', 'esbuild', 'npm', 'Yarn', 'pnpm', 'Bun', 'Turborepo', 'Nx',
        # State Management
        'Redux', 'Redux Toolkit', 'Zustand', 'Recoil', 'Context API', 'React Query', 'SWR',
        # Real-time & Messaging
        'WebSockets', 'Socket.io', 'Pub/Sub', 'Message Queues', 'RabbitMQ', 'Apache Kafka',
        # Methodologies
        'Agile', 'Scrum', 'Microservices', 'Serverless', 'JAMstack', 'API-First Design',
        'Performance Optimization', 'SEO', 'Web Vitals', 'Accessibility', 'WCAG',
    ],

    'frontend developer': [
        # Core Technologies
        'JavaScript', 'TypeScript', 'HTML5', 'CSS3', 'Web APIs', 'DOM Manipulation',
        # Frontend Frameworks & Libraries
        'React', 'React 18', 'React 19', 'Next.js 14', 'Next.js 15', 'App Router', 'Server Components',
        'Vue.js', 'Vue 3', 'Nuxt.js', 'Nuxt 3', 'Angular', 'Angular 17', 'Svelte', 'SvelteKit',
        'Solid.js', 'Remix', 'Astro', 'Qwik', 'Preact',
        # State Management
        'Redux', 'Redux Toolkit', 'Zustand', 'Recoil', 'Jotai', 'MobX', 'XState', 'Context API',
        'React Query', 'TanStack Query', 'SWR', 'Apollo Client', 'Relay', 'Pinia', 'Vuex',
        # CSS Frameworks & Libraries
        'Tailwind CSS', 'Bootstrap', 'Material-UI (MUI)', 'Chakra UI', 'Ant Design', 'shadcn/ui',
        'Radix UI', 'Headless UI', 'DaisyUI', 'Mantine', 'PrimeReact', 'Semantic UI',
        # CSS Preprocessors & Tools
        'Sass', 'SCSS', 'Less', 'Stylus', 'PostCSS', 'CSS Modules', 'Styled Components',
        'Emotion', 'styled-jsx', 'Vanilla Extract', 'Linaria',
        # CSS Techniques
        'Flexbox', 'CSS Grid', 'Responsive Design', 'Mobile-First Design', 'CSS Animations',
        'CSS Transitions', 'CSS Variables', 'Custom Properties',
        # Build Tools & Bundlers
        'Webpack', 'Vite', 'Turbopack', 'esbuild', 'Rollup', 'Parcel', 'SWC', 'Babel',
        # Package Managers & Monorepos
        'npm', 'Yarn', 'pnpm', 'Bun', 'Turborepo', 'Nx', 'Lerna', 'Monorepo Management',
        # Testing
        'Jest', 'Vitest', 'React Testing Library', 'Vue Test Utils', 'Cypress', 'Playwright',
        'Puppeteer', 'Storybook', 'Chromatic', 'Visual Regression Testing', 'Unit Testing', 'E2E Testing',
        # Performance & Optimization
        'Web Performance', 'Core Web Vitals', 'Lighthouse', 'LCP', 'FID', 'CLS', 'Code Splitting',
        'Lazy Loading', 'Image Optimization', 'Caching Strategies', 'Bundle Optimization',
        # Accessibility
        'Accessibility', 'WCAG', 'ARIA', 'Screen Readers', 'Keyboard Navigation', 'Color Contrast',
        # SEO
        'SEO', 'Meta Tags', 'Structured Data', 'Schema.org', 'Open Graph', 'Twitter Cards',
        # Progressive Web Apps
        'PWA', 'Service Workers', 'Web Workers', 'Workbox', 'App Manifest', 'Offline Support',
        # Version Control
        'Git', 'GitHub', 'GitLab', 'Pull Requests', 'Code Review', 'Git Flow',
        # Browser DevTools & Debugging
        'Chrome DevTools', 'React DevTools', 'Vue DevTools', 'Redux DevTools', 'Debugging',
        # Linters & Formatters
        'ESLint', 'Prettier', 'Stylelint', 'TypeScript Compiler', 'Husky', 'lint-staged',
        # Design Systems
        'Design Systems', 'Component Libraries', 'Atomic Design', 'Design Tokens',
        # UI/UX Principles
        'UI/UX Principles', 'User Experience', 'Figma', 'Adobe XD', 'Sketch',
        # Cross-Platform
        'Cross-Browser Compatibility', 'Browser APIs', 'Polyfills', 'Can I Use',
        # Methodologies
        'Agile', 'Component-Driven Development', 'Atomic Design', 'BEM', 'Mobile-First',
    ],

    'backend developer': [
        # Programming Languages
        'Node.js', 'Python', 'Java', 'C#', 'Go', 'Rust', 'Ruby', 'PHP', 'Scala', 'Kotlin',
        # Node.js Frameworks
        'Express.js', 'NestJS', 'Fastify', 'Koa', 'Hapi', 'AdonisJS', 'Sails.js',
        # Python Frameworks
        'Django', 'Flask', 'FastAPI', 'Tornado', 'Pyramid', 'Sanic', 'Bottle',
        # Java Frameworks
        'Spring Boot', 'Spring Framework', 'Hibernate', 'Micronaut', 'Quarkus',
        # Other Frameworks
        'ASP.NET Core', '.NET', 'Ruby on Rails', 'Sinatra', 'Laravel', 'Symfony', 'CodeIgniter',
        # Databases - SQL
        'SQL', 'PostgreSQL', 'MySQL', 'Microsoft SQL Server', 'Oracle Database', 'MariaDB', 'SQLite',
        # Databases - NoSQL
        'MongoDB', 'Redis', 'Cassandra', 'DynamoDB', 'CouchDB', 'Neo4j', 'InfluxDB',
        # ORM & Query Builders
        'Prisma', 'TypeORM', 'Sequelize', 'Mongoose', 'Drizzle', 'Knex.js', 'SQLAlchemy',
        'Hibernate', 'Entity Framework', 'Active Record',
        # Database Design
        'Database Design', 'Database Modeling', 'Normalization', 'Indexing', 'Query Optimization',
        'Database Sharding', 'Replication', 'Partitioning',
        # APIs & Communication
        'REST APIs', 'RESTful Services', 'GraphQL', 'Apollo Server', 'gRPC', 'Protocol Buffers',
        'WebSockets', 'Socket.io', 'Server-Sent Events', 'Webhooks', 'API Gateway',
        # API Documentation
        'Swagger', 'OpenAPI', 'Postman', 'Insomnia', 'API Documentation',
        # Authentication & Authorization
        'Authentication', 'Authorization', 'OAuth', 'OAuth2', 'JWT', 'Passport.js', 'bcrypt',
        'Argon2', 'Session Management', 'RBAC', 'ABAC', 'Auth0', 'Keycloak',
        # Caching
        'Caching', 'Redis', 'Memcached', 'Varnish', 'CDN', 'Cache Strategies', 'Cache Invalidation',
        # Message Queues & Streaming
        'Message Queues', 'RabbitMQ', 'Apache Kafka', 'Amazon SQS', 'Redis Pub/Sub', 'NATS',
        'Apache Pulsar', 'Event-Driven Architecture',
        # Microservices
        'Microservices', 'Microservices Architecture', 'Service Mesh', 'Istio', 'Consul',
        'API Gateway', 'Service Discovery', 'Circuit Breaker', 'Load Balancing',
        # Serverless
        'Serverless', 'AWS Lambda', 'Azure Functions', 'Google Cloud Functions', 'Cloudflare Workers',
        'Vercel Functions', 'Netlify Functions',
        # Cloud Platforms
        'AWS', 'EC2', 'S3', 'RDS', 'DynamoDB', 'Lambda', 'API Gateway', 'Azure', 'Google Cloud',
        'GCP', 'Cloud Run', 'App Engine', 'Heroku', 'Railway', 'Render',
        # Containerization
        'Docker', 'Docker Compose', 'Kubernetes', 'Helm', 'Container Orchestration', 'Podman',
        # CI/CD & DevOps
        'CI/CD', 'Jenkins', 'GitHub Actions', 'GitLab CI', 'CircleCI', 'Travis CI', 'Azure Pipelines',
        'DevOps', 'Infrastructure as Code', 'Terraform', 'Ansible', 'CloudFormation',
        # Version Control
        'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Git Flow', 'Code Review', 'Pull Requests',
        # Testing
        'Unit Testing', 'Integration Testing', 'E2E Testing', 'TDD', 'BDD', 'Jest', 'Mocha',
        'Chai', 'Pytest', 'JUnit', 'NUnit', 'RSpec', 'Supertest', 'API Testing',
        # Monitoring & Logging
        'Logging', 'Monitoring', 'Application Performance Monitoring', 'Sentry', 'New Relic',
        'Datadog', 'Prometheus', 'Grafana', 'ELK Stack', 'Elasticsearch', 'Logstash', 'Kibana',
        'Winston', 'Pino', 'Log4j',
        # Security
        'Security', 'OWASP', 'Security Best Practices', 'SQL Injection Prevention', 'XSS Prevention',
        'CSRF Protection', 'Rate Limiting', 'DDoS Protection', 'Encryption', 'SSL/TLS',
        # Performance
        'Performance Optimization', 'Profiling', 'Load Testing', 'Apache JMeter', 'k6', 'Gatling',
        'Locust', 'Artillery',
        # Web Servers
        'Nginx', 'Apache', 'Caddy', 'IIS', 'Reverse Proxy', 'Load Balancer',
        # Methodologies
        'Agile', 'Scrum', 'API-First Design', 'Domain-Driven Design', 'SOLID Principles',
        'Clean Architecture', 'Design Patterns', 'Twelve-Factor App',
    ],

    'mobile developer': [
        # Cross-Platform Frameworks
        'React Native', 'Flutter', 'Dart', 'Expo', 'Ionic', 'Capacitor', 'Xamarin', '.NET MAUI',
        # iOS Development
        'Swift', 'SwiftUI', 'UIKit', 'Objective-C', 'iOS Development', 'Xcode', 'CocoaPods',
        'Swift Package Manager', 'Core Data', 'Core Animation', 'Core Location', 'HealthKit',
        'ARKit', 'RealityKit', 'Combine', 'Core ML', 'Vision Framework',
        # Android Development
        'Kotlin', 'Java', 'Android Development', 'Android Studio', 'Jetpack Compose', 'XML Layouts',
        'Material Design 3', 'Android Architecture Components', 'Room Database', 'WorkManager',
        'Data Binding', 'View Binding', 'Retrofit', 'OkHttp', 'Gradle', 'Coroutines', 'Flow',
        # Design Guidelines
        'Material Design', 'Human Interface Guidelines', 'Mobile UI/UX', 'Responsive Design',
        'Adaptive Layouts', 'Dark Mode', 'Accessibility', 'Touch Gestures', 'Animations',
        # State Management
        'State Management', 'Redux', 'Redux Toolkit', 'MobX', 'Zustand', 'Provider', 'Riverpod',
        'Bloc', 'Cubit', 'GetX', 'React Context', 'Recoil',
        # Backend & APIs
        'REST APIs', 'GraphQL', 'WebSockets', 'Firebase', 'Supabase', 'AWS Amplify',
        'API Integration', 'HTTP Client', 'Axios', 'Fetch API',
        # Local Storage
        'SQLite', 'Realm', 'Hive', 'SharedPreferences', 'UserDefaults', 'AsyncStorage',
        'MMKV', 'Watermelon DB', 'Core Data', 'Keychain Services',
        # Firebase Services
        'Firebase Authentication', 'Firestore', 'Firebase Realtime Database', 'Firebase Storage',
        'Firebase Cloud Messaging', 'Firebase Analytics', 'Firebase Crashlytics',
        'Firebase Remote Config', 'Firebase App Distribution',
        # Push Notifications
        'Push Notifications', 'FCM', 'Apple Push Notification Service', 'APNS', 'OneSignal',
        'Notification Channels', 'Local Notifications',
        # App Features
        'Deep Linking', 'Universal Links', 'App Links', 'In-App Purchases', 'App Store Connect',
        'Google Play Console', 'Subscriptions', 'Payment Integration', 'Stripe', 'RevenueCat',
        # Device Features
        'Camera Integration', 'Photo Library', 'Location Services', 'GPS', 'Maps Integration',
        'Google Maps', 'Apple Maps', 'Mapbox', 'Bluetooth', 'BLE', 'NFC', 'Biometrics',
        'Face ID', 'Touch ID', 'Fingerprint', 'Sensors', 'Gyroscope', 'Accelerometer',
        # Testing
        'Testing', 'Unit Testing', 'Integration Testing', 'UI Testing', 'E2E Testing',
        'Jest', 'Detox', 'XCTest', 'XCUITest', 'Espresso', 'JUnit', 'Appium',
        'TestFlight', 'Firebase Test Lab',
        # Performance & Optimization
        'Performance Optimization', 'Memory Management', 'Battery Optimization',
        'App Size Optimization', 'Network Optimization', 'Image Optimization',
        'Code Splitting', 'Lazy Loading', 'Profiling', 'Instruments',
        # Analytics & Monitoring
        'Mobile Analytics', 'Google Analytics', 'Firebase Analytics', 'Mixpanel', 'Amplitude',
        'Crash Reporting', 'Crashlytics', 'Sentry', 'Bugsnag', 'App Center',
        # Native Modules
        'Native Modules', 'Native Bridge', 'Platform-Specific Code', 'Kotlin Multiplatform',
        'Native APIs', 'Bridge Communication',
        # Build & Deployment
        'App Store Deployment', 'Google Play Deployment', 'TestFlight', 'Internal Testing',
        'Beta Testing', 'Code Signing', 'Provisioning Profiles', 'App Signing',
        'Fastlane', 'CI/CD', 'GitHub Actions', 'Bitrise', 'CircleCI', 'App Center',
        # Version Control & Tools
        'Git', 'GitHub', 'GitLab', 'Xcode', 'Android Studio', 'VS Code', 'Flipper',
        'React Native Debugger', 'Charles Proxy',
        # Programming Concepts
        'Threading', 'Multithreading', 'Async Programming', 'Concurrency', 'Background Tasks',
        'Memory Leaks', 'Debugging', 'Reactive Programming', 'MVVM', 'MVI', 'Clean Architecture',
    ],

    'data scientist': [
        # Programming Languages
        'Python', 'R', 'SQL', 'Julia', 'Scala', 'Java',
        # Machine Learning
        'Machine Learning', 'Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning',
        'Semi-Supervised Learning', 'Transfer Learning', 'Active Learning', 'Online Learning',
        # Deep Learning
        'Deep Learning', 'Neural Networks', 'CNNs', 'RNNs', 'LSTMs', 'GRUs', 'Transformers',
        'Attention Mechanism', 'BERT', 'GPT', 'Vision Transformers', 'Autoencoders', 'GANs',
        # ML Frameworks & Libraries
        'TensorFlow', 'TensorFlow 2.x', 'Keras', 'PyTorch', 'PyTorch Lightning', 'JAX',
        'Scikit-learn', 'XGBoost', 'LightGBM', 'CatBoost', 'H2O.ai', 'Rapids', 'Fast.ai',
        # Data Manipulation & Analysis
        'Pandas', 'NumPy', 'SciPy', 'Polars', 'Dask', 'Modin', 'Vaex', 'Arrow', 'Koalas',
        # Data Visualization
        'Data Visualization', 'Matplotlib', 'Seaborn', 'Plotly', 'Bokeh', 'Altair', 'Dash',
        'Streamlit', 'Gradio', 'Panel', 'ggplot2', 'Tableau', 'Power BI', 'Looker',
        # Statistical Analysis
        'Statistics', 'Probability', 'Statistical Inference', 'Hypothesis Testing', 'A/B Testing',
        'Bayesian Statistics', 'Time Series Analysis', 'ARIMA', 'Prophet', 'statsmodels',
        # Mathematics
        'Linear Algebra', 'Calculus', 'Multivariate Calculus', 'Optimization', 'Numerical Methods',
        # Feature Engineering
        'Feature Engineering', 'Feature Selection', 'Dimensionality Reduction', 'PCA', 't-SNE',
        'UMAP', 'Feature Scaling', 'Feature Encoding', 'One-Hot Encoding', 'Label Encoding',
        # Model Development
        'Model Selection', 'Model Training', 'Hyperparameter Tuning', 'Grid Search', 'Random Search',
        'Bayesian Optimization', 'Optuna', 'Ray Tune', 'Cross-Validation', 'K-Fold Validation',
        'Stratified Sampling', 'Model Evaluation', 'Metrics', 'Confusion Matrix', 'ROC Curve',
        'Precision', 'Recall', 'F1 Score', 'AUC', 'RMSE', 'MAE', 'R-squared',
        # ML Algorithms
        'Regression', 'Linear Regression', 'Logistic Regression', 'Ridge', 'Lasso', 'ElasticNet',
        'Classification', 'Decision Trees', 'Random Forest', 'Gradient Boosting', 'SVM',
        'K-Nearest Neighbors', 'Naive Bayes', 'Clustering', 'K-Means', 'DBSCAN', 'Hierarchical Clustering',
        'Gaussian Mixture Models', 'Dimensionality Reduction', 'Ensemble Methods', 'Bagging', 'Boosting',
        # NLP (Natural Language Processing)
        'NLP', 'Natural Language Processing', 'Text Mining', 'Text Processing', 'Tokenization',
        'Word Embeddings', 'Word2Vec', 'GloVe', 'FastText', 'BERT', 'RoBERTa', 'GPT', 'T5',
        'Transformers', 'Hugging Face', 'spaCy', 'NLTK', 'Gensim', 'Sentiment Analysis',
        'Named Entity Recognition', 'Topic Modeling', 'LDA', 'Text Classification',
        # Computer Vision
        'Computer Vision', 'Image Processing', 'Image Classification', 'Object Detection', 'YOLO',
        'R-CNN', 'Faster R-CNN', 'Image Segmentation', 'Semantic Segmentation', 'Instance Segmentation',
        'OpenCV', 'Pillow', 'scikit-image', 'Albumentations', 'imgaug',
        # Time Series
        'Time Series Analysis', 'Time Series Forecasting', 'ARIMA', 'SARIMA', 'Prophet',
        'LSTM for Time Series', 'Exponential Smoothing', 'Seasonal Decomposition',
        # Big Data
        'Big Data', 'Apache Spark', 'PySpark', 'Spark MLlib', 'Hadoop', 'Hive', 'Presto',
        'Dask', 'Distributed Computing', 'Parallel Processing',
        # Databases
        'SQL', 'PostgreSQL', 'MySQL', 'NoSQL', 'MongoDB', 'Redis', 'Elasticsearch',
        'Snowflake', 'BigQuery', 'Redshift', 'Data Warehousing',
        # Development Tools
        'Jupyter Notebooks', 'JupyterLab', 'Google Colab', 'Kaggle Notebooks', 'VS Code',
        'PyCharm', 'RStudio', 'Spyder',
        # MLOps & Deployment
        'MLOps', 'Model Deployment', 'Model Serving', 'MLflow', 'Weights & Biases', 'Neptune.ai',
        'Comet', 'Kubeflow', 'Seldon', 'BentoML', 'TorchServe', 'TensorFlow Serving',
        'FastAPI', 'Flask', 'Docker', 'Kubernetes', 'AWS SageMaker', 'Azure ML', 'Google Vertex AI',
        # Experiment Tracking
        'Experiment Tracking', 'Model Versioning', 'Data Versioning', 'DVC', 'Git', 'GitHub',
        # Cloud Platforms
        'AWS', 'S3', 'SageMaker', 'EMR', 'Glue', 'Azure', 'Azure ML', 'Databricks',
        'Google Cloud', 'BigQuery', 'Vertex AI', 'Cloud AI Platform',
        # AutoML
        'AutoML', 'Auto-sklearn', 'TPOT', 'H2O AutoML', 'Google AutoML', 'Azure AutoML',
        # Data Collection & Cleaning
        'Data Cleaning', 'Data Preprocessing', 'Data Wrangling', 'Missing Data Imputation',
        'Outlier Detection', 'Data Quality', 'Exploratory Data Analysis', 'EDA', 'Data Profiling',
        # APIs & Web Scraping
        'REST APIs', 'Web Scraping', 'Beautiful Soup', 'Scrapy', 'Selenium', 'API Integration',
        # Soft Skills
        'Communication', 'Data Storytelling', 'Presentation Skills', 'Business Acumen',
        'Problem Solving', 'Critical Thinking', 'Collaboration', 'Stakeholder Management',
        # Ethics & Responsibility
        'AI Ethics', 'Responsible AI', 'Bias Detection', 'Fairness', 'Model Interpretability',
        'Explainable AI', 'XAI', 'SHAP', 'LIME', 'Feature Importance',
    ],

    'data analyst': [
        # Database & Query Languages
        'SQL', 'PostgreSQL', 'MySQL', 'SQL Server', 'BigQuery', 'Snowflake', 'Redshift',
        'NoSQL', 'MongoDB', 'Advanced SQL', 'SQL Joins', 'Subqueries', 'CTEs', 'Window Functions',
        'Query Optimization', 'Database Design', 'Data Modeling',
        # Programming Languages
        'Python', 'R', 'DAX', 'M Language', 'VBA', 'JavaScript',
        # Python Libraries
        'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Plotly', 'SciPy', 'statsmodels',
        # Excel & Spreadsheets
        'Excel', 'Advanced Excel', 'Pivot Tables', 'VLOOKUP', 'XLOOKUP', 'INDEX-MATCH',
        'Power Query', 'Power Pivot', 'Macros', 'VBA', 'Google Sheets', 'Formulas', 'Charts',
        # Business Intelligence Tools
        'Tableau', 'Tableau Desktop', 'Tableau Prep', 'Tableau Server', 'Power BI', 'Power BI Desktop',
        'Power BI Service', 'DAX', 'Power Query', 'Looker', 'Looker Studio', 'Google Data Studio',
        'Qlik Sense', 'QlikView', 'Sisense', 'Domo', 'Metabase', 'Redash', 'Apache Superset',
        # Data Visualization
        'Data Visualization', 'Dashboard Creation', 'Dashboard Design', 'Interactive Dashboards',
        'Storytelling with Data', 'Visual Analytics', 'Chart Selection', 'Color Theory',
        'Data Presentation', 'Infographics',
        # Statistics & Analysis
        'Statistics', 'Descriptive Statistics', 'Inferential Statistics', 'Statistical Analysis',
        'Probability', 'Hypothesis Testing', 'A/B Testing', 'T-Tests', 'Chi-Square Tests',
        'Correlation Analysis', 'Regression Analysis', 'Linear Regression', 'Logistic Regression',
        'ANOVA', 'Statistical Significance', 'Confidence Intervals', 'P-Values',
        # Data Processing
        'Data Cleaning', 'Data Preprocessing', 'Data Wrangling', 'Data Transformation',
        'Data Validation', 'Data Quality', 'Missing Data Handling', 'Outlier Detection',
        'ETL', 'ELT', 'Data Integration', 'Data Migration',
        # Data Warehousing
        'Data Warehousing', 'Data Marts', 'OLAP', 'OLTP', 'Star Schema', 'Snowflake Schema',
        'Dimensional Modeling', 'Fact Tables', 'Dimension Tables',
        # Analytics Platforms
        'Google Analytics', 'GA4', 'Google Analytics 4', 'Adobe Analytics', 'Mixpanel',
        'Amplitude', 'Segment', 'Heap Analytics', 'Hotjar', 'Web Analytics',
        'Product Analytics', 'Marketing Analytics', 'Customer Analytics',
        # Reporting
        'Reporting', 'Report Creation', 'Automated Reporting', 'Scheduled Reports',
        'Ad-hoc Reporting', 'KPI Reporting', 'Executive Dashboards', 'Operational Dashboards',
        # Business Intelligence
        'Business Intelligence', 'BI Strategy', 'KPI Development', 'KPI Tracking', 'Metrics Analysis',
        'Business Metrics', 'Key Performance Indicators', 'OKRs', 'Scorecards', 'Benchmarking',
        # Data Analysis Techniques
        'Exploratory Data Analysis', 'EDA', 'Cohort Analysis', 'Funnel Analysis', 'RFM Analysis',
        'Customer Segmentation', 'Churn Analysis', 'Trend Analysis', 'Time Series Analysis',
        'Forecasting', 'Predictive Analytics', 'Prescriptive Analytics', 'Diagnostic Analytics',
        # Cloud Platforms
        'AWS', 'S3', 'Redshift', 'Athena', 'QuickSight', 'Azure', 'Azure Synapse', 'Azure Analysis Services',
        'Google Cloud', 'BigQuery', 'Looker', 'Data Studio',
        # Development Tools
        'Jupyter Notebooks', 'VS Code', 'Git', 'GitHub', 'Version Control', 'Anaconda',
        # CRM & Business Tools
        'Salesforce', 'HubSpot', 'Zendesk', 'Jira', 'Confluence', 'Asana', 'Monday.com',
        'Notion', 'Microsoft Teams', 'Slack',
        # Database Tools
        'DBeaver', 'pgAdmin', 'MySQL Workbench', 'SQL Server Management Studio', 'DataGrip',
        'Navicat', 'Azure Data Studio',
        # Project Management
        'Agile', 'Scrum', 'Project Management', 'Requirements Gathering', 'Stakeholder Management',
        # Soft Skills
        'Communication', 'Presentation Skills', 'Data Storytelling', 'Business Acumen',
        'Problem Solving', 'Critical Thinking', 'Analytical Skills', 'Attention to Detail',
        'Time Management', 'Collaboration', 'Cross-Functional Collaboration',
        # Domain Knowledge
        'Business Analysis', 'Business Process Understanding', 'Domain Expertise',
        'Financial Analysis', 'Marketing Analysis', 'Sales Analysis', 'Operations Analysis',
        # Data Governance
        'Data Governance', 'Data Privacy', 'GDPR', 'Data Security', 'Data Documentation',
        'Data Dictionary', 'Metadata Management',
    ],

    'data engineer': [
        'Python', 'Java', 'Scala', 'SQL', 'Apache Spark', 'Apache Kafka', 'Apache Airflow', 'Hadoop',
        'Hive', 'Presto', 'ETL', 'ELT', 'Data Pipelines', 'Data Warehousing', 'Data Lakes', 'AWS',
        'S3', 'Redshift', 'Glue', 'EMR', 'Azure', 'Azure Data Factory', 'Synapse', 'Google Cloud',
        'BigQuery', 'Dataflow', 'Pub/Sub', 'Docker', 'Kubernetes', 'Git', 'Data Modeling',
        'Dimensional Modeling', 'Star Schema', 'Snowflake Schema', 'PostgreSQL', 'MySQL', 'MongoDB',
        'Cassandra', 'Redis', 'Elasticsearch', 'Data Quality', 'Data Governance', 'Performance Optimization',
        'Query Optimization', 'Indexing', 'Partitioning', 'Streaming Data', 'Batch Processing', 'CI/CD',
    ],

    'machine learning engineer': [
        'Python', 'C++', 'Java', 'TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn', 'Machine Learning',
        'Deep Learning', 'Neural Networks', 'CNNs', 'RNNs', 'LSTMs', 'Transformers', 'GANs', 'NLP',
        'Computer Vision', 'Reinforcement Learning', 'Model Training', 'Model Optimization', 'Hyperparameter Tuning',
        'Feature Engineering', 'Model Deployment', 'MLOps', 'Docker', 'Kubernetes', 'AWS', 'SageMaker',
        'Azure ML', 'Google Cloud AI', 'Git', 'CI/CD', 'REST APIs', 'Model Serving', 'Model Monitoring',
        'A/B Testing', 'Statistics', 'Linear Algebra', 'Calculus', 'Probability', 'Data Structures',
        'Algorithms', 'Distributed Computing', 'Spark', 'GPU Programming', 'CUDA', 'Model Compression',
        'Quantization', 'Pruning', 'Transfer Learning', 'AutoML', 'Experiment Tracking', 'MLflow', 'Weights & Biases',
    ],

    'ai engineer': [
        'Python', 'TensorFlow', 'PyTorch', 'Keras', 'Machine Learning', 'Deep Learning', 'Neural Networks',
        'NLP', 'Natural Language Processing', 'BERT', 'GPT', 'Transformers', 'Computer Vision', 'CNNs',
        'Object Detection', 'Image Segmentation', 'Reinforcement Learning', 'Generative AI', 'GANs',
        'Diffusion Models', 'LLMs', 'Prompt Engineering', 'Fine-Tuning', 'RAG', 'Vector Databases',
        'Embeddings', 'AI Ethics', 'Responsible AI', 'Model Interpretability', 'XAI', 'Model Optimization',
        'Model Deployment', 'MLOps', 'Cloud Computing', 'AWS', 'Azure', 'Google Cloud', 'Docker',
        'Kubernetes', 'Git', 'Statistics', 'Mathematics', 'Linear Algebra', 'Calculus', 'Probability',
        'Research', 'Paper Reading', 'Experiment Design', 'Data Preprocessing', 'Feature Engineering',
    ],

    'product manager': [
        # Product Strategy
        'Product Strategy', 'Product Vision', 'Product Roadmap', 'Roadmap Planning', 'Strategic Planning',
        'Product Lifecycle', 'Product Positioning', 'Value Proposition', 'Competitive Advantage',
        'Market Analysis', 'Market Research', 'Competitive Analysis', 'SWOT Analysis',
        # Product Discovery
        'Product Discovery', 'Problem Discovery', 'Solution Discovery', 'Customer Development',
        'Customer Interviews', 'User Research', 'User Interviews', 'Surveys', 'Focus Groups',
        'Contextual Inquiry', 'User Testing', 'Usability Testing', 'Beta Testing',
        # User Understanding
        'User Personas', 'Customer Personas', 'Jobs to be Done', 'JTBD', 'User Stories',
        'User Journey Mapping', 'Customer Journey Maps', 'Empathy Mapping', 'Use Cases',
        # Requirements & Specifications
        'Requirements Gathering', 'Requirements Management', 'PRD', 'Product Requirements Document',
        'Feature Specification', 'Technical Specifications', 'Acceptance Criteria', 'User Story Mapping',
        # Prioritization
        'Prioritization', 'Backlog Management', 'Backlog Grooming', 'Backlog Refinement',
        'RICE Framework', 'MoSCoW Method', 'Kano Model', 'Value vs Effort', 'Impact vs Effort',
        'Weighted Scoring', 'Cost of Delay', 'Opportunity Scoring',
        # Agile & Methodologies
        'Agile', 'Scrum', 'Kanban', 'Lean', 'Lean Startup', 'Sprint Planning', 'Sprint Review',
        'Sprint Retrospective', 'Daily Standup', 'Agile Ceremonies', 'Release Planning',
        # Metrics & Analytics
        'Product Metrics', 'KPIs', 'Key Performance Indicators', 'OKRs', 'Objectives and Key Results',
        'North Star Metric', 'AARRR', 'Pirate Metrics', 'Acquisition', 'Activation', 'Retention',
        'Revenue', 'Referral', 'Engagement Metrics', 'Retention Metrics', 'Churn Rate', 'LTV',
        'CAC', 'Unit Economics', 'Product-Market Fit', 'PMF Metrics',
        # Analytics Tools
        'Data Analysis', 'SQL', 'Analytics Tools', 'Google Analytics', 'GA4', 'Mixpanel',
        'Amplitude', 'Heap', 'Segment', 'Looker', 'Tableau', 'Power BI', 'Pendo', 'FullStory',
        'Hotjar', 'Google Tag Manager', 'Firebase Analytics',
        # Experimentation
        'A/B Testing', 'Multivariate Testing', 'Split Testing', 'Experimentation', 'Hypothesis Testing',
        'Feature Flags', 'LaunchDarkly', 'Optimizely', 'VWO', 'Google Optimize',
        # Product Design & UX
        'UX Principles', 'UI/UX Basics', 'Design Thinking', 'User-Centered Design', 'Wireframing',
        'Mockups', 'Prototyping', 'Figma', 'Adobe XD', 'Sketch', 'InVision', 'Miro', 'FigJam',
        'Design Systems', 'Usability Principles', 'Accessibility', 'WCAG',
        # Technical Understanding
        'Technical Fluency', 'Software Development Lifecycle', 'SDLC', 'APIs', 'REST APIs',
        'GraphQL', 'System Architecture', 'Database Basics', 'Cloud Computing', 'AWS', 'Azure',
        'Technical Documentation', 'API Documentation', 'Swagger', 'OpenAPI',
        # Product Tools - Project Management
        'Jira', 'Jira Software', 'Jira Product Discovery', 'Confluence', 'Asana', 'Monday.com',
        'Trello', 'ClickUp', 'Notion', 'Linear', 'Aha!', 'ProductBoard', 'Productboard',
        'Roadmunk', 'ProdPad', 'Airfocus', 'Craft.io',
        # Communication & Documentation
        'Confluence', 'Notion', 'Google Docs', 'Microsoft Office', 'Presentations', 'Slide Decks',
        'Documentation', 'Technical Writing', 'Storytelling', 'Data Storytelling',
        # Stakeholder Management
        'Stakeholder Management', 'Stakeholder Communication', 'Executive Communication',
        'Cross-Functional Leadership', 'Leadership', 'Influence', 'Negotiation',
        'Conflict Resolution', 'Decision Making', 'Trade-off Analysis',
        # Go-to-Market
        'Go-to-Market Strategy', 'GTM Strategy', 'Launch Planning', 'Product Launch',
        'Product Marketing', 'Positioning', 'Messaging', 'Pricing Strategy', 'Pricing Models',
        'Freemium', 'SaaS Pricing', 'Value-Based Pricing',
        # Customer Feedback
        'Customer Feedback', 'Feedback Analysis', 'User Feedback', 'Feature Requests',
        'Customer Support Insights', 'NPS', 'CSAT', 'Customer Satisfaction', 'Voice of Customer',
        'Intercom', 'Zendesk', 'UserVoice', 'Canny', 'ProductBoard Insights',
        # Business Skills
        'Business Acumen', 'Business Model', 'Business Model Canvas', 'Revenue Models',
        'Unit Economics', 'Financial Analysis', 'ROI Analysis', 'Cost-Benefit Analysis',
        'Budget Management', 'Resource Planning', 'Risk Management',
        # Soft Skills
        'Communication', 'Verbal Communication', 'Written Communication', 'Presentation Skills',
        'Public Speaking', 'Active Listening', 'Empathy', 'Critical Thinking', 'Problem Solving',
        'Analytical Thinking', 'Strategic Thinking', 'Creativity', 'Innovation', 'Adaptability',
        'Time Management', 'Organization', 'Multitasking', 'Collaboration', 'Teamwork',
        # Product Growth
        'Product Growth', 'Growth Strategy', 'Growth Hacking', 'Viral Loops', 'Network Effects',
        'Growth Metrics', 'Conversion Optimization', 'Funnel Analysis', 'Retention Strategy',
        # Modern PM Concepts
        'Product-Led Growth', 'PLG', 'Continuous Discovery', 'Dual-Track Agile',
        'Shape Up', 'Opportunity Solution Trees', 'Outcome-Based Roadmaps',
        'Now-Next-Later Roadmap', 'Theme-Based Roadmap',
    ],

    'project manager': [
        'Project Planning', 'Project Scheduling', 'Agile', 'Scrum', 'Kanban', 'Waterfall', 'Hybrid Methodologies',
        'Risk Management', 'Risk Assessment', 'Mitigation Strategies', 'Budget Management', 'Cost Estimation',
        'Resource Allocation', 'Resource Planning', 'Stakeholder Communication', 'Stakeholder Management',
        'Team Leadership', 'Team Building', 'Conflict Resolution', 'Negotiation', 'Microsoft Project',
        'Jira', 'Confluence', 'Asana', 'Trello', 'Monday.com', 'Timeline Management', 'Gantt Charts',
        'Critical Path Method', 'Earned Value Management', 'Change Management', 'Problem Solving',
        'Decision Making', 'Documentation', 'Reporting', 'Status Reports', 'Quality Assurance',
        'Process Improvement', 'Continuous Improvement', 'Communication', 'Presentation Skills', 'Time Management',
        'PMP Certification', 'PRINCE2', 'Lean', 'Six Sigma', 'Meeting Facilitation', 'Sprint Planning',
    ],

    'ui/ux designer': [
        # Design Tools
        'Figma', 'FigJam', 'Adobe XD', 'Sketch', 'InVision', 'InVision Studio', 'Framer',
        'Principle', 'ProtoPie', 'Origami Studio', 'Marvel', 'Axure RP', 'Balsamiq',
        'Zeplin', 'Abstract', 'Maze', 'Optimal Workshop', 'Penpot', 'Lunacy',
        # Prototyping
        'Prototyping', 'Interactive Prototyping', 'High-Fidelity Prototypes', 'Low-Fidelity Prototypes',
        'Wireframing', 'Wireframes', 'Lo-Fi Wireframes', 'Hi-Fi Wireframes', 'Mockups',
        'Clickable Prototypes', 'Animated Prototypes', 'Rapid Prototyping',
        # User Research
        'User Research', 'User Interviews', 'User Testing', 'Usability Testing', 'Remote Testing',
        'Moderated Testing', 'Unmoderated Testing', 'Surveys', 'Questionnaires', 'User Personas',
        'Buyer Personas', 'User Journey Mapping', 'Customer Journey Maps', 'Empathy Mapping',
        'Affinity Mapping', 'Card Sorting', 'Tree Testing', 'First Click Testing',
        # UX Research Tools
        'UserTesting', 'Hotjar', 'Crazy Egg', 'FullStory', 'Lookback', 'UsabilityHub',
        'Google Forms', 'Typeform', 'SurveyMonkey', 'Qualtrics', 'Dovetail',
        # Information Architecture
        'Information Architecture', 'IA', 'Sitemaps', 'User Flows', 'Task Flows', 'User Flow Diagrams',
        'Navigation Design', 'Content Strategy', 'Content Hierarchy', 'Taxonomy',
        # Interaction Design
        'Interaction Design', 'IxD', 'Micro-interactions', 'Animation', 'Motion Design',
        'Transitions', 'Loading States', 'Error States', 'Empty States', 'Feedback Mechanisms',
        'Gestures', 'Touch Interactions',
        # Visual Design
        'Visual Design', 'Typography', 'Type Hierarchy', 'Font Pairing', 'Type Scale',
        'Color Theory', 'Color Systems', 'Color Palettes', 'Visual Hierarchy', 'Layout Design',
        'Grid Systems', 'Spacing Systems', '8pt Grid', 'Golden Ratio', 'Rule of Thirds',
        'Composition', 'Balance', 'Contrast', 'Alignment', 'Proximity', 'White Space',
        # Design Systems
        'Design Systems', 'Component Libraries', 'Pattern Libraries', 'Style Guides',
        'Design Tokens', 'Atomic Design', 'Design System Documentation', 'Component Variants',
        'Material Design', 'Human Interface Guidelines', 'Fluent Design', 'Carbon Design System',
        # Responsive & Adaptive Design
        'Responsive Design', 'Adaptive Design', 'Mobile Design', 'Mobile-First Design',
        'Web Design', 'Desktop Design', 'Tablet Design', 'Breakpoints', 'Fluid Layouts',
        # Accessibility
        'Accessibility', 'A11y', 'WCAG', 'WCAG 2.1', 'WCAG 2.2', 'Section 508', 'ARIA',
        'ARIA Labels', 'Screen Readers', 'Keyboard Navigation', 'Color Contrast', 'Alt Text',
        'Inclusive Design', 'Universal Design', 'Accessibility Testing', 'WAVE', 'axe DevTools',
        # Testing & Validation
        'A/B Testing', 'Multivariate Testing', 'Split Testing', 'User Testing', 'Heuristic Evaluation',
        'Cognitive Walkthrough', 'Expert Review', 'Design Critique', 'Iteration',
        # UX Metrics
        'UX Metrics', 'Analytics', 'Google Analytics', 'Mixpanel', 'Amplitude', 'Heap',
        'User Engagement', 'Task Success Rate', 'Time on Task', 'Error Rate', 'NPS',
        'CSAT', 'SUS', 'System Usability Scale',
        # Front-end Basics
        'HTML', 'CSS', 'HTML/CSS Basics', 'Responsive Web Design', 'Flexbox', 'CSS Grid',
        'JavaScript Basics', 'SVG', 'Web Standards', 'Browser DevTools',
        # Collaboration & Handoff
        'Collaboration', 'Design Handoff', 'Developer Handoff', 'Redlining', 'Annotations',
        'Design Specs', 'Design Documentation', 'Design Reviews', 'Stakeholder Presentations',
        # Methodologies
        'Design Thinking', 'Human-Centered Design', 'HCD', 'Lean UX', 'Agile/UX', 'Scrum',
        'Design Sprints', 'Google Design Sprint', 'Jobs to be Done', 'JTBD',
        # Version Control & Assets
        'Version Control', 'Git', 'GitHub', 'Design Version Control', 'Asset Management',
        # Communication & Soft Skills
        'Communication', 'Presentation Skills', 'Storytelling', 'Stakeholder Management',
        'Client Communication', 'Critique', 'Feedback', 'Collaboration', 'Teamwork',
        'Problem Solving', 'Critical Thinking', 'Empathy', 'Active Listening',
        # Industry Knowledge
        'UX Best Practices', 'UI Patterns', 'Design Patterns', 'Mobile Patterns', 'Web Patterns',
        'Dark Patterns', 'Progressive Disclosure', 'Affordances', 'Signifiers',
        # Emerging Technologies
        'Voice UI', 'VUI', 'Conversational Design', 'Chatbot Design', 'AR Design', 'VR Design',
        'Mixed Reality', 'Wearables', 'IoT Design', 'AI/UX Integration',
    ],

    'graphic designer': [
        'Adobe Photoshop', 'Adobe Illustrator', 'Adobe InDesign', 'CorelDRAW', 'Affinity Designer', 'Figma',
        'Typography', 'Font Selection', 'Kerning', 'Leading', 'Color Theory', 'Color Harmony', 'Branding',
        'Brand Identity', 'Logo Design', 'Layout Design', 'Composition', 'Visual Hierarchy', 'Print Design',
        'Digital Design', 'Web Design', 'Social Media Graphics', 'Marketing Materials', 'Packaging Design',
        'Illustration', 'Vector Graphics', 'Raster Graphics', 'Image Editing', 'Photo Manipulation',
        'Creative Thinking', 'Conceptualization', 'Attention to Detail', 'Communication', 'Client Relations',
        'Presentation Skills', 'Time Management', 'Project Management', 'Portfolio Development', 'Trend Awareness',
        'Print Production', 'File Preparation', 'Color Profiles', 'Resolution', 'Bleed & Margins', 'Grid Systems',
    ],

    'web designer': [
        'HTML5', 'CSS3', 'JavaScript', 'Responsive Design', 'Mobile-First Design', 'Figma', 'Adobe XD',
        'Sketch', 'Photoshop', 'Illustrator', 'Wireframing', 'Prototyping', 'UI/UX Principles', 'Typography',
        'Color Theory', 'Layout Design', 'Grid Systems', 'Flexbox', 'CSS Grid', 'Animations', 'CSS Transitions',
        'WordPress', 'CMS', 'Webflow', 'Squarespace', 'Web Standards', 'W3C Guidelines', 'Accessibility',
        'WCAG', 'SEO Basics', 'Meta Tags', 'Performance Optimization', 'Image Optimization', 'Cross-browser Compatibility',
        'Browser DevTools', 'Version Control', 'Git', 'Collaboration', 'Communication', 'Client Relations',
        'Time Management', 'Problem Solving', 'Attention to Detail', 'Branding', 'Visual Design', 'User Experience',
    ],

    'devops engineer': [
        # Operating Systems
        'Linux', 'Ubuntu', 'Debian', 'CentOS', 'Red Hat', 'RHEL', 'Alpine Linux', 'Amazon Linux',
        'Rocky Linux', 'Unix', 'Windows Server',
        # Scripting & Programming
        'Bash', 'Shell Scripting', 'Python', 'Go', 'PowerShell', 'Ruby', 'Perl', 'YAML', 'JSON',
        # Containerization
        'Docker', 'Docker Compose', 'Podman', 'Buildah', 'Containerd', 'Docker Swarm',
        'Container Images', 'Multi-stage Builds', 'Dockerfile', 'Container Registry',
        # Kubernetes
        'Kubernetes', 'K8s', 'kubectl', 'Helm', 'Kustomize', 'K9s', 'Lens', 'Rancher',
        'Kubernetes Operators', 'StatefulSets', 'DaemonSets', 'ConfigMaps', 'Secrets',
        'Ingress Controllers', 'Service Mesh', 'Istio', 'Linkerd', 'Calico', 'Flannel',
        # Cloud Platforms - AWS
        'AWS', 'EC2', 'S3', 'ECS', 'EKS', 'Lambda', 'CloudFormation', 'CloudWatch',
        'IAM', 'VPC', 'Route 53', 'RDS', 'DynamoDB', 'ElastiCache', 'SNS', 'SQS',
        'API Gateway', 'Elastic Beanstalk', 'EBS', 'EFS', 'ECR', 'AWS CLI',
        # Cloud Platforms - Azure
        'Azure', 'Azure DevOps', 'Azure Kubernetes Service', 'Azure Functions',
        'Azure Container Instances', 'Azure Container Registry', 'Azure Monitor',
        'Azure Resource Manager', 'Azure CLI', 'Azure Pipelines',
        # Cloud Platforms - GCP
        'Google Cloud', 'GCP', 'GKE', 'Cloud Run', 'Cloud Functions', 'Cloud Build',
        'Cloud Storage', 'Compute Engine', 'Container Registry', 'Cloud SQL',
        'Cloud Monitoring', 'Cloud Logging', 'gcloud CLI',
        # Infrastructure as Code
        'Infrastructure as Code', 'IaC', 'Terraform', 'Terraform Cloud', 'Terragrunt',
        'Pulumi', 'CloudFormation', 'ARM Templates', 'Bicep', 'CDK', 'AWS CDK',
        # Configuration Management
        'Configuration Management', 'Ansible', 'Ansible Tower', 'AWX', 'Puppet', 'Chef',
        'SaltStack', 'CFEngine',
        # CI/CD
        'CI/CD', 'Continuous Integration', 'Continuous Deployment', 'Continuous Delivery',
        'Jenkins', 'Jenkins Pipeline', 'GitHub Actions', 'GitLab CI/CD', 'GitLab Runner',
        'CircleCI', 'Travis CI', 'Azure Pipelines', 'Bamboo', 'TeamCity', 'Drone CI',
        'Spinnaker', 'Harness', 'Tekton',
        # GitOps
        'GitOps', 'ArgoCD', 'Flux', 'FluxCD', 'Argo Rollouts', 'Argo Workflows',
        # Version Control
        'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Git Flow', 'Trunk-Based Development',
        # Monitoring & Observability
        'Monitoring', 'Observability', 'Prometheus', 'Grafana', 'Alertmanager',
        'Thanos', 'Cortex', 'VictoriaMetrics', 'Datadog', 'New Relic', 'Dynatrace',
        'AppDynamics', 'Splunk', 'Nagios', 'Zabbix', 'Icinga',
        # Logging
        'Logging', 'ELK Stack', 'Elasticsearch', 'Logstash', 'Kibana', 'Fluentd',
        'Fluent Bit', 'Loki', 'Graylog', 'CloudWatch Logs', 'Azure Monitor Logs',
        # Service Mesh & API Gateway
        'Service Mesh', 'Istio', 'Linkerd', 'Consul', 'Envoy', 'API Gateway',
        'Kong', 'Traefik', 'HAProxy', 'Ambassador',
        # Networking
        'Networking', 'TCP/IP', 'DNS', 'DHCP', 'VPN', 'Load Balancing', 'Reverse Proxy',
        'CDN', 'CloudFlare', 'Nginx', 'Apache', 'HAProxy', 'Traefik', 'Caddy',
        'SSL/TLS', 'Certificates', "Let's Encrypt", 'ACM',
        # Security
        'Security', 'DevSecOps', 'Container Security', 'Image Scanning', 'Trivy', 'Clair',
        'Snyk', 'Aqua Security', 'Falco', 'OPA', 'Open Policy Agent', 'Vault',
        'HashiCorp Vault', 'Secrets Management', 'SOPS', 'sealed-secrets',
        'SSL/TLS', 'Firewalls', 'Security Groups', 'Network Policies', 'RBAC',
        'IAM', 'Identity Management', 'SSO', 'OAuth', 'OIDC',
        # Databases & Storage
        'Database Management', 'PostgreSQL', 'MySQL', 'MongoDB', 'Redis', 'Elasticsearch',
        'Database Backups', 'Database Migrations', 'Backup Strategies', 'Disaster Recovery',
        # Artifact Management
        'Artifact Management', 'Nexus', 'Artifactory', 'Harbor', 'Docker Registry',
        'JFrog', 'Package Management',
        # Performance & Optimization
        'Performance Optimization', 'Performance Tuning', 'Auto Scaling', 'Horizontal Scaling',
        'Vertical Scaling', 'Cost Optimization', 'Resource Optimization', 'Capacity Planning',
        # Testing & Quality
        'Load Testing', 'Stress Testing', 'Apache JMeter', 'k6', 'Gatling', 'Locust',
        'Chaos Engineering', 'Chaos Monkey', 'Litmus', 'Gremlin',
        # Incident Management
        'Incident Management', 'Incident Response', 'Troubleshooting', 'Root Cause Analysis',
        'Post-Mortem', 'On-Call', 'PagerDuty', 'Opsgenie', 'VictorOps',
        # Documentation & Collaboration
        'Documentation', 'Runbooks', 'Technical Writing', 'Confluence', 'Wiki',
        'Diagrams', 'Architecture Diagrams', 'Communication', 'Team Collaboration',
        # Methodologies
        'Agile', 'Scrum', 'DevOps Culture', 'Site Reliability Engineering', 'SRE',
        'Automation', 'Process Improvement', 'Best Practices',
    ],

    'cloud engineer': [
        # AWS Services - Compute
        'AWS', 'EC2', 'ECS', 'EKS', 'Lambda', 'Fargate', 'Lightsail', 'Batch', 'Elastic Beanstalk',
        'App Runner', 'Serverless', 'Auto Scaling', 'EC2 Image Builder',
        # AWS Services - Storage
        'S3', 'EBS', 'EFS', 'FSx', 'Storage Gateway', 'Glacier', 'S3 Glacier', 'Snow Family',
        'DataSync', 'Transfer Family', 'Backup',
        # AWS Services - Database
        'RDS', 'Aurora', 'DynamoDB', 'ElastiCache', 'Neptune', 'Redshift', 'DocumentDB',
        'Timestream', 'QLDB', 'Keyspaces', 'MemoryDB',
        # AWS Services - Networking
        'VPC', 'Route 53', 'CloudFront', 'API Gateway', 'Direct Connect', 'Transit Gateway',
        'VPN', 'Elastic Load Balancing', 'ALB', 'NLB', 'GLB', 'PrivateLink', 'Global Accelerator',
        # AWS Services - Security
        'IAM', 'Cognito', 'Secrets Manager', 'KMS', 'CloudHSM', 'Certificate Manager', 'ACM',
        'WAF', 'Shield', 'GuardDuty', 'Inspector', 'Macie', 'Security Hub', 'Detective',
        # AWS Services - Management
        'CloudFormation', 'CDK', 'CloudWatch', 'CloudTrail', 'Config', 'Systems Manager',
        'OpsWorks', 'Service Catalog', 'Control Tower', 'Organizations', 'Trusted Advisor',
        'AWS CLI', 'AWS SDK', 'AWS Console',
        # AWS Services - DevOps
        'CodePipeline', 'CodeBuild', 'CodeDeploy', 'CodeCommit', 'CodeArtifact', 'X-Ray',
        # AWS Services - Messaging & Queuing
        'SQS', 'SNS', 'EventBridge', 'Kinesis', 'MQ', 'MSK', 'Step Functions',
        # Azure Services - Compute
        'Azure', 'Azure VMs', 'Azure App Service', 'Azure Functions', 'Azure Container Instances',
        'Azure Kubernetes Service', 'AKS', 'Azure Batch', 'Azure Spring Apps',
        # Azure Services - Storage
        'Azure Storage', 'Blob Storage', 'File Storage', 'Queue Storage', 'Table Storage',
        'Azure Data Lake', 'Azure Backup', 'Azure Site Recovery',
        # Azure Services - Database
        'Azure SQL Database', 'Azure Cosmos DB', 'Azure Database for PostgreSQL',
        'Azure Database for MySQL', 'Azure Cache for Redis', 'Azure Synapse Analytics',
        # Azure Services - Networking
        'Azure Virtual Network', 'Azure VPN Gateway', 'Azure ExpressRoute', 'Azure Load Balancer',
        'Azure Application Gateway', 'Azure Front Door', 'Azure CDN', 'Azure DNS',
        'Azure Firewall', 'Azure Bastion',
        # Azure Services - Security
        'Azure AD', 'Azure AD B2C', 'Azure Key Vault', 'Azure Security Center', 'Azure Sentinel',
        'Azure DDoS Protection', 'Azure Information Protection',
        # Azure Services - Management
        'Azure Monitor', 'Azure Log Analytics', 'Azure DevOps', 'Azure Resource Manager',
        'ARM Templates', 'Bicep', 'Azure Policy', 'Azure Blueprints', 'Azure CLI', 'Azure PowerShell',
        # Google Cloud - Compute
        'Google Cloud', 'GCP', 'Compute Engine', 'GKE', 'Cloud Run', 'Cloud Functions',
        'App Engine', 'Cloud Build', 'Anthos',
        # Google Cloud - Storage
        'Cloud Storage', 'Persistent Disk', 'Filestore', 'Archive Storage',
        # Google Cloud - Database
        'Cloud SQL', 'Cloud Spanner', 'Cloud Bigtable', 'Firestore', 'Memorystore',
        'BigQuery', 'Cloud Datastore',
        # Google Cloud - Networking
        'Cloud VPC', 'Cloud Load Balancing', 'Cloud CDN', 'Cloud DNS', 'Cloud VPN',
        'Cloud Interconnect', 'Cloud NAT', 'Cloud Armor',
        # Google Cloud - Security
        'Cloud IAM', 'Identity Platform', 'Secret Manager', 'Cloud KMS', 'Security Command Center',
        # Google Cloud - Management
        'Cloud Monitoring', 'Cloud Logging', 'Cloud Trace', 'Cloud Profiler', 'Cloud Deployment Manager',
        'gcloud CLI',
        # Infrastructure as Code
        'Infrastructure as Code', 'IaC', 'Terraform', 'Terraform Cloud', 'Pulumi',
        'CloudFormation', 'ARM Templates', 'Bicep', 'CDK', 'Ansible',
        # Containerization & Orchestration
        'Docker', 'Kubernetes', 'Helm', 'Docker Compose', 'Container Registry',
        'ECR', 'ACR', 'GCR', 'Harbor',
        # Cloud Architecture
        'Cloud Architecture', 'Solution Architecture', 'Multi-Cloud', 'Hybrid Cloud',
        'Cloud Migration', 'Lift and Shift', 'Re-platforming', 'Refactoring',
        'Well-Architected Framework', 'Cloud Design Patterns', '12-Factor App',
        # Networking
        'Networking', 'VPC', 'Subnets', 'CIDR', 'NAT Gateway', 'Internet Gateway',
        'Security Groups', 'Network ACLs', 'Routing Tables', 'Peering', 'Transit Gateway',
        'Load Balancing', 'CDN', 'DNS', 'SSL/TLS', 'Private Endpoints',
        # Security & Compliance
        'Security', 'IAM', 'RBAC', 'Identity Management', 'Encryption', 'Encryption at Rest',
        'Encryption in Transit', 'Key Management', 'Secrets Management', 'Compliance',
        'GDPR', 'HIPAA', 'PCI DSS', 'SOC 2', 'ISO 27001', 'Security Auditing',
        'Vulnerability Scanning', 'Penetration Testing', 'Security Best Practices',
        # Cost Management
        'Cost Optimization', 'Cost Management', 'Reserved Instances', 'Spot Instances',
        'Savings Plans', 'Cost Explorer', 'Billing Alerts', 'Budgets', 'Cost Allocation Tags',
        'FinOps', 'Right-sizing', 'Resource Tagging',
        # High Availability & Disaster Recovery
        'High Availability', 'Fault Tolerance', 'Disaster Recovery', 'Backup and Restore',
        'Pilot Light', 'Warm Standby', 'Multi-Region', 'Multi-AZ', 'Replication',
        'Failover', 'RTO', 'RPO', 'Business Continuity',
        # Performance & Scalability
        'Performance Optimization', 'Scalability', 'Auto Scaling', 'Horizontal Scaling',
        'Vertical Scaling', 'Caching', 'CDN', 'Load Balancing', 'Database Optimization',
        'Content Delivery', 'Edge Computing',
        # Monitoring & Logging
        'Monitoring', 'CloudWatch', 'Azure Monitor', 'Cloud Monitoring', 'Logging',
        'Log Analytics', 'Metrics', 'Alarms', 'Dashboards', 'Alerting', 'Tracing',
        'Distributed Tracing', 'APM', 'Observability',
        # CI/CD & DevOps
        'CI/CD', 'Jenkins', 'GitHub Actions', 'GitLab CI', 'Azure Pipelines',
        'CodePipeline', 'Cloud Build', 'Automation', 'GitOps', 'ArgoCD',
        # Scripting & Programming
        'Linux', 'Bash', 'Shell Scripting', 'Python', 'PowerShell', 'Go', 'YAML', 'JSON',
        # Serverless
        'Serverless Architecture', 'Function as a Service', 'FaaS', 'Event-Driven Architecture',
        'Lambda', 'Azure Functions', 'Cloud Functions', 'API Gateway', 'EventBridge',
        # Databases & Data
        'Database Management', 'SQL', 'NoSQL', 'Database Migration', 'Database Replication',
        'Database Backup', 'Data Transfer', 'ETL', 'Data Pipeline',
        # Troubleshooting & Support
        'Troubleshooting', 'Problem Solving', 'Root Cause Analysis', 'Performance Tuning',
        'Capacity Planning', 'Technical Documentation', 'Runbooks',
        # Certifications & Best Practices
        'AWS Certified Solutions Architect', 'Azure Solutions Architect', 'GCP Professional Cloud Architect',
        'Cloud Best Practices', 'Cloud Native', 'Cloud Security', 'Communication', 'Team Collaboration',
    ],

    'security engineer': [
        'Cybersecurity', 'Information Security', 'Network Security', 'Application Security', 'Cloud Security',
        'Penetration Testing', 'Ethical Hacking', 'Vulnerability Assessment', 'Security Auditing', 'Threat Modeling',
        'Risk Assessment', 'Encryption', 'Cryptography', 'SSL/TLS', 'PKI', 'Firewalls', 'IDS/IPS', 'SIEM',
        'Splunk', 'ELK Stack', 'Security Operations', 'Incident Response', 'Forensics', 'Malware Analysis',
        'Threat Intelligence', 'Threat Hunting', 'Compliance', 'GDPR', 'HIPAA', 'PCI DSS', 'ISO 27001',
        'NIST', 'Security Frameworks', 'Linux', 'Windows', 'Networking', 'TCP/IP', 'Python', 'Bash',
        'PowerShell', 'Metasploit', 'Burp Suite', 'Wireshark', 'Nmap', 'OWASP Top 10', 'Web Application Security',
        'API Security', 'Container Security', 'Kubernetes Security', 'Security Tools', 'Identity Management',
    ],

    'network engineer': [
        'Networking', 'TCP/IP', 'OSI Model', 'Routing', 'Switching', 'VLANs', 'BGP', 'OSPF', 'EIGRP',
        'RIP', 'Static Routing', 'Dynamic Routing', 'Firewalls', 'VPN', 'IPSec', 'SSL VPN', 'Network Security',
        'Access Control Lists', 'Cisco', 'Cisco IOS', 'Juniper', 'Fortinet', 'Palo Alto', 'Network Design',
        'Network Architecture', 'LAN', 'WAN', 'SD-WAN', 'Network Troubleshooting', 'Packet Analysis', 'Wireshark',
        'DNS', 'DHCP', 'NAT', 'Load Balancing', 'QoS', 'Traffic Shaping', 'Network Monitoring', 'SNMP',
        'SolarWinds', 'PRTG', 'Wireless Networking', 'Wi-Fi', 'Network Automation', 'Python', 'Ansible',
        'Documentation', 'Network Diagrams', 'Problem Solving', 'Communication', 'Project Management', 'Certifications',
    ],

    'system administrator': [
        'Linux', 'Ubuntu', 'CentOS', 'Red Hat', 'SUSE', 'Windows Server', 'Windows 10/11', 'Active Directory',
        'Group Policy', 'User Management', 'Networking', 'TCP/IP', 'DNS', 'DHCP', 'Firewalls', 'Bash',
        'Shell Scripting', 'PowerShell', 'Python', 'Virtualization', 'VMware', 'Hyper-V', 'VirtualBox',
        'Backup & Recovery', 'Disaster Recovery', 'Monitoring', 'Nagios', 'Zabbix', 'Security', 'Patch Management',
        'Antivirus', 'Troubleshooting', 'Hardware', 'Servers', 'Storage', 'SAN', 'NAS', 'Cloud Computing',
        'AWS', 'Azure', 'Automation', 'Ansible', 'Documentation', 'Ticketing Systems', 'Email Systems',
        'Exchange', 'Office 365', 'Database Management', 'MySQL', 'PostgreSQL', 'Performance Tuning', 'Capacity Planning',
    ],

    'database administrator': [
        'SQL', 'MySQL', 'PostgreSQL', 'Oracle', 'SQL Server', 'MongoDB', 'Cassandra', 'Redis', 'Database Design',
        'Normalization', 'Denormalization', 'ER Diagrams', 'Schema Design', 'Indexing', 'Query Optimization',
        'Performance Tuning', 'Execution Plans', 'Backup & Recovery', 'Point-in-Time Recovery', 'Replication',
        'Master-Slave', 'Master-Master', 'High Availability', 'Clustering', 'Sharding', 'Partitioning', 'Security',
        'User Management', 'Permissions', 'Encryption', 'Auditing', 'Monitoring', 'Database Monitoring Tools',
        'Troubleshooting', 'Data Migration', 'ETL', 'Data Integrity', 'Constraints', 'Triggers', 'Stored Procedures',
        'Functions', 'Views', 'Transactions', 'ACID', 'Concurrency', 'Locking', 'Cloud Databases', 'AWS RDS',
        'Azure SQL', 'Documentation', 'Disaster Recovery', 'Capacity Planning', 'Linux', 'Bash', 'Python',
    ],

    'quality assurance engineer': [
        'Manual Testing', 'Automated Testing', 'Test Automation', 'Selenium', 'WebDriver', 'Appium', 'Cypress',
        'Playwright', 'JUnit', 'TestNG', 'PyTest', 'Jest', 'Mocha', 'Test Planning', 'Test Strategy',
        'Test Cases', 'Test Scenarios', 'Test Scripts', 'Bug Tracking', 'Defect Management', 'Jira', 'Bugzilla',
        'TestRail', 'API Testing', 'Postman', 'REST Assured', 'SoapUI', 'Regression Testing', 'Smoke Testing',
        'Sanity Testing', 'Integration Testing', 'System Testing', 'UAT', 'Performance Testing', 'Load Testing',
        'Stress Testing', 'JMeter', 'LoadRunner', 'Agile', 'Scrum', 'CI/CD', 'Jenkins', 'Git', 'SQL',
        'Attention to Detail', 'Problem Solving', 'Analytical Skills', 'Communication', 'Documentation', 'Test Reports',
    ],

    'qa engineer': [
        'Manual Testing', 'Automated Testing', 'Selenium', 'WebDriver', 'Cypress', 'Playwright', 'Puppeteer',
        'Jest', 'Mocha', 'Chai', 'PyTest', 'Test Cases', 'Test Scenarios', 'Bug Reporting', 'Jira', 'Confluence',
        'API Testing', 'Postman', 'REST APIs', 'GraphQL Testing', 'Regression Testing', 'Smoke Testing',
        'Integration Testing', 'End-to-End Testing', 'Unit Testing', 'TDD', 'BDD', 'Cucumber', 'Gherkin',
        'CI/CD', 'GitHub Actions', 'GitLab CI', 'Jenkins', 'Agile', 'Scrum', 'Sprint Testing', 'Git',
        'Version Control', 'Test Automation Frameworks', 'Page Object Model', 'Data-Driven Testing',
        'Keyword-Driven Testing', 'Cross-Browser Testing', 'Mobile Testing', 'Responsive Testing', 'Accessibility Testing',
        'Performance Testing', 'Attention to Detail', 'Communication', 'Problem Solving', 'Documentation', 'SQL',
    ],

    'qa tester': [
        'Manual Testing', 'Test Cases', 'Test Execution', 'Bug Reporting', 'Defect Lifecycle', 'Regression Testing',
        'Smoke Testing', 'Sanity Testing', 'Exploratory Testing', 'Ad-hoc Testing', 'User Acceptance Testing',
        'Functional Testing', 'Non-Functional Testing', 'UI Testing', 'Usability Testing', 'Jira', 'Bugzilla',
        'TestRail', 'Test Management', 'Test Plans', 'Test Scenarios', 'Test Documentation', 'Requirements Analysis',
        'Agile', 'Scrum', 'Sprint Testing', 'Communication', 'Attention to Detail', 'Problem Solving',
        'Critical Thinking', 'Analytical Skills', 'API Testing', 'Postman', 'Mobile Testing', 'Web Testing',
        'Cross-Browser Testing', 'Responsive Testing', 'Database Testing', 'SQL', 'Basic Automation', 'Selenium Basics',
        'Git Basics', 'Version Control', 'Test Metrics', 'Test Reports', 'Collaboration', 'Team Player',
    ],

    'technical writer': [
        'Technical Writing', 'Documentation', 'API Documentation', 'User Guides', 'User Manuals', 'How-To Guides',
        'Tutorials', 'Release Notes', 'README Files', 'Knowledge Base Articles', 'Markdown', 'reStructuredText',
        'AsciiDoc', 'Git', 'GitHub', 'GitLab', 'Docs as Code', 'Static Site Generators', 'MkDocs', 'Docusaurus',
        'Sphinx', 'Jekyll', 'Hugo', 'Communication', 'Technical Communication', 'Audience Analysis', 'Information Architecture',
        'Content Organization', 'Attention to Detail', 'Research', 'Subject Matter Experts', 'Interviewing',
        'Editing', 'Proofreading', 'Grammar', 'Style Guides', 'Microsoft Style Guide', 'Google Developer Style Guide',
        'Content Management', 'CMS', 'Confluence', 'SharePoint', 'Screenshots', 'Screen Recording', 'Diagrams',
        'Flowcharts', 'UML', 'Lucidchart', 'Draw.io', 'Collaboration', 'Agile', 'Scrum', 'JIRA', 'Basic HTML/CSS',
    ],

    'scrum master': [
        'Scrum', 'Scrum Framework', 'Agile', 'Agile Methodologies', 'Kanban', 'Lean', 'Sprint Planning',
        'Sprint Review', 'Sprint Retrospective', 'Daily Standup', 'Backlog Management', 'Product Backlog',
        'Sprint Backlog', 'User Stories', 'Story Points', 'Velocity', 'Burndown Charts', 'Facilitation',
        'Meeting Facilitation', 'Stakeholder Management', 'Communication', 'Active Listening', 'Conflict Resolution',
        'Problem Solving', 'Impediment Removal', 'Coaching', 'Team Coaching', 'Agile Coaching', 'Mentoring',
        'Servant Leadership', 'Team Building', 'Team Dynamics', 'Jira', 'Confluence', 'Azure DevOps', 'Trello',
        'Miro', 'Metrics & Reporting', 'Agile Metrics', 'Team Performance', 'Continuous Improvement', 'Change Management',
        'Process Improvement', 'Collaboration', 'Cross-Functional Teams', 'Self-Organization', 'Empowerment', 'Motivation',
        'Transparency', 'Inspection', 'Adaptation', 'Scrum Values', 'CSM Certification', 'PSM Certification',
    ],

    'business analyst': [
        'Requirements Gathering', 'Requirements Analysis', 'Requirements Documentation', 'Elicitation Techniques',
        'User Stories', 'Use Cases', 'Acceptance Criteria', 'Business Process Modeling', 'BPMN', 'Process Mapping',
        'Workflow Analysis', 'Gap Analysis', 'Stakeholder Analysis', 'Stakeholder Management', 'Communication',
        'Data Analysis', 'SQL', 'Excel', 'Advanced Excel', 'Pivot Tables', 'VLOOKUP', 'Power Query', 'Tableau',
        'Power BI', 'Data Visualization', 'Documentation', 'Functional Specifications', 'Technical Specifications',
        'Jira', 'Confluence', 'Agile', 'Scrum', 'Waterfall', 'SDLC', 'Problem Solving', 'Critical Thinking',
        'Analytical Skills', 'Presentation Skills', 'Wireframing', 'Mockups', 'Figma', 'Lucidchart', 'Visio',
        'Process Improvement', 'Change Management', 'Testing', 'UAT', 'Test Cases', 'Project Management Basics',
    ],

    'marketing manager': [
        'Marketing Strategy', 'Brand Strategy', 'Campaign Management', 'Digital Marketing', 'Content Marketing',
        'Email Marketing', 'Social Media Marketing', 'SEO', 'Search Engine Optimization', 'SEM', 'PPC',
        'Google Ads', 'Facebook Ads', 'Instagram Ads', 'LinkedIn Ads', 'Marketing Analytics', 'Google Analytics',
        'Data Analysis', 'ROI Analysis', 'KPI Tracking', 'A/B Testing', 'Market Research', 'Competitive Analysis',
        'Customer Segmentation', 'Target Audience', 'Buyer Personas', 'Marketing Automation', 'HubSpot', 'Marketo',
        'Mailchimp', 'CRM', 'Salesforce', 'Budget Management', 'Budget Planning', 'Team Leadership', 'Team Management',
        'Vendor Management', 'Communication', 'Presentation Skills', 'Creativity', 'Copywriting', 'Content Creation',
        'Brand Management', 'Product Marketing', 'Go-to-Market Strategy', 'Event Marketing', 'PR', 'Influencer Marketing',
    ],

    'digital marketing specialist': [
        'Digital Marketing', 'SEO', 'Search Engine Optimization', 'On-Page SEO', 'Off-Page SEO', 'Technical SEO',
        'Keyword Research', 'SEM', 'PPC', 'Google Ads', 'Display Ads', 'Search Ads', 'Shopping Ads', 'Facebook Ads',
        'Instagram Ads', 'LinkedIn Ads', 'Twitter Ads', 'Social Media Marketing', 'Social Media Management',
        'Content Marketing', 'Content Creation', 'Copywriting', 'Email Marketing', 'Email Campaigns', 'Newsletter',
        'Marketing Automation', 'Google Analytics', 'GA4', 'Google Tag Manager', 'Facebook Pixel', 'Analytics',
        'Data Analysis', 'Reporting', 'A/B Testing', 'Conversion Rate Optimization', 'Landing Pages', 'WordPress',
        'CMS', 'HTML Basics', 'Canva', 'Adobe Creative Suite', 'Communication', 'Creativity', 'Strategy',
        'Campaign Management', 'Budget Management', 'ROI Analysis', 'Trend Analysis', 'Competitor Analysis',
    ],

    'seo specialist': [
        'SEO', 'Search Engine Optimization', 'On-Page SEO', 'Off-Page SEO', 'Technical SEO', 'Keyword Research',
        'Keyword Analysis', 'Competitive Analysis', 'SEO Audit', 'Site Audit', 'Link Building', 'Backlink Analysis',
        'Content Optimization', 'Meta Tags', 'Title Tags', 'Meta Descriptions', 'Header Tags', 'Schema Markup',
        'Structured Data', 'Google Analytics', 'GA4', 'Google Search Console', 'Bing Webmaster Tools', 'SEO Tools',
        'SEMrush', 'Ahrefs', 'Moz', 'Screaming Frog', 'Google PageSpeed Insights', 'Core Web Vitals', 'Page Speed',
        'Mobile Optimization', 'Mobile-First Indexing', 'Local SEO', 'Google My Business', 'HTML', 'CSS Basics',
        'JavaScript Basics', 'WordPress', 'Yoast SEO', 'Rank Math', 'Analytics', 'Reporting', 'Data Analysis',
        'Communication', 'Content Writing', 'Copywriting', 'Strategy', 'Algorithm Updates', 'Trend Awareness',
    ],

    'content writer': [
        'Content Writing', 'Copywriting', 'Creative Writing', 'Blog Writing', 'Article Writing', 'Web Content',
        'SEO Writing', 'SEO Content', 'Keyword Integration', 'Keyword Research', 'Research', 'Research Skills',
        'Fact-Checking', 'Editing', 'Proofreading', 'Grammar', 'Punctuation', 'Spelling', 'Style Guides',
        'AP Style', 'Chicago Style', 'Storytelling', 'Narrative', 'Engagement', 'Readability', 'Tone of Voice',
        'Brand Voice', 'Audience Understanding', 'WordPress', 'CMS', 'Content Management', 'Social Media Writing',
        'Email Writing', 'Newsletter Writing', 'Product Descriptions', 'Landing Pages', 'White Papers', 'Case Studies',
        'Creativity', 'Originality', 'Communication', 'Time Management', 'Deadline Management', 'Adaptability',
        'Versatility', 'Attention to Detail', 'Collaboration', 'Feedback Implementation', 'Google Docs', 'Microsoft Word',
    ],

    'sales manager': [
        'Sales Strategy', 'Sales Planning', 'Territory Management', 'Account Management', 'Key Account Management',
        'Team Leadership', 'Team Management', 'Coaching', 'Mentoring', 'Performance Management', 'Sales Training',
        'CRM', 'Salesforce', 'HubSpot', 'Pipedrive', 'Pipeline Management', 'Sales Forecasting', 'Quota Management',
        'Target Setting', 'Lead Generation', 'Prospecting', 'Cold Calling', 'Negotiation', 'Closing', 'Deal Closing',
        'Client Relations', 'Relationship Building', 'Customer Service', 'Communication', 'Presentation Skills',
        'Persuasion', 'Problem Solving', 'Objection Handling', 'Consultative Selling', 'Solution Selling', 'Value Selling',
        'B2B Sales', 'B2C Sales', 'Sales Metrics', 'Analytics', 'Reporting', 'Business Development', 'Market Analysis',
        'Competitive Analysis', 'Networking', 'Motivation', 'Time Management', 'Strategic Thinking', 'Microsoft Office',
    ],

    'customer success manager': [
        'Customer Success', 'Customer Relations', 'Customer Relationship Management', 'Account Management', 'Client Management',
        'Onboarding', 'Customer Onboarding', 'User Onboarding', 'Training', 'Customer Training', 'Product Knowledge',
        'Product Expertise', 'CRM', 'Salesforce', 'HubSpot', 'Zendesk', 'Intercom', 'Communication', 'Active Listening',
        'Empathy', 'Problem Solving', 'Conflict Resolution', 'Issue Resolution', 'Escalation Management', 'Retention',
        'Customer Retention', 'Churn Reduction', 'Upselling', 'Cross-Selling', 'Expansion', 'Account Growth',
        'Customer Advocacy', 'Customer Feedback', 'Surveys', 'NPS', 'CSAT', 'Analytics', 'Data Analysis', 'Metrics',
        'Customer Health Scores', 'Engagement Tracking', 'Reporting', 'Presentation Skills', 'Time Management',
        'Organization', 'Collaboration', 'Cross-Functional Collaboration', 'Relationship Building', 'Trust Building',
        'Strategic Thinking', 'Business Acumen', 'Consultative Approach', 'Proactive Support', 'Documentation',
    ],

    'hr manager': [
        'Human Resources', 'HR Management', 'Recruitment', 'Talent Acquisition', 'Sourcing', 'Screening', 'Interviewing',
        'Behavioral Interviewing', 'Selection', 'Offer Negotiation', 'Onboarding', 'Employee Onboarding', 'Orientation',
        'Employee Relations', 'Employee Engagement', 'Performance Management', 'Performance Reviews', 'Goal Setting',
        'Feedback', 'Coaching', 'Conflict Resolution', 'Mediation', 'Disciplinary Actions', 'HR Policies',
        'Policy Development', 'Compliance', 'Labor Law', 'Employment Law', 'FMLA', 'ADA', 'EEOC', 'Compensation',
        'Benefits', 'Benefits Administration', 'Payroll', 'HRIS', 'Workday', 'BambooHR', 'ADP', 'Training & Development',
        'Learning & Development', 'Career Development', 'Succession Planning', 'Workforce Planning', 'Organizational Development',
        'Change Management', 'Culture Building', 'Communication', 'Leadership', 'Strategic Planning', 'Analytics',
        'HR Metrics', 'Reporting', 'Microsoft Office', 'Excel', 'Confidentiality', 'Ethics',
    ],

    'financial analyst': [
        'Financial Analysis', 'Financial Modeling', 'Excel', 'Advanced Excel', 'Financial Statements', 'Income Statement',
        'Balance Sheet', 'Cash Flow Statement', 'Ratio Analysis', 'Profitability Ratios', 'Liquidity Ratios',
        'Valuation', 'DCF', 'Comparable Company Analysis', 'Precedent Transactions', 'Data Analysis', 'Statistical Analysis',
        'Forecasting', 'Financial Forecasting', 'Budgeting', 'Budget Analysis', 'Variance Analysis', 'Financial Reporting',
        'Management Reporting', 'Presentation Skills', 'SQL', 'Database Querying', 'Bloomberg Terminal', 'Capital IQ',
        'FactSet', 'Accounting', 'GAAP', 'IFRS', 'Corporate Finance', 'Investment Analysis', 'Risk Analysis',
        'Sensitivity Analysis', 'Scenario Analysis', 'Business Intelligence', 'Tableau', 'Power BI', 'VBA',
        'Python', 'R', 'Communication', 'Attention to Detail', 'Problem Solving', 'Critical Thinking',
        'Analytical Skills', 'Time Management', 'Deadline Management', 'Collaboration', 'PowerPoint',
    ],

    'accountant': [
        'Accounting', 'Bookkeeping', 'Financial Reporting', 'Financial Statements', 'Income Statement', 'Balance Sheet',
        'Cash Flow Statement', 'General Ledger', 'Journal Entries', 'Accounts Payable', 'Accounts Receivable',
        'Reconciliation', 'Bank Reconciliation', 'Account Reconciliation', 'Tax Preparation', 'Tax Filing',
        'Tax Compliance', 'Payroll', 'Payroll Processing', 'Excel', 'QuickBooks', 'Xero', 'Sage', 'SAP',
        'Oracle Financials', 'GAAP', 'Generally Accepted Accounting Principles', 'IFRS', 'Auditing', 'Internal Controls',
        'Compliance', 'Financial Analysis', 'Budget Preparation', 'Month-End Close', 'Year-End Close', 'Cost Accounting',
        'Variance Analysis', 'Fixed Assets', 'Depreciation', 'Accruals', 'Attention to Detail', 'Accuracy',
        'Problem Solving', 'Analytical Skills', 'Communication', 'Time Management', 'Ethics', 'Integrity',
        'Organization', 'Documentation', 'Microsoft Office', 'CPA', 'Certification',
    ],
}
